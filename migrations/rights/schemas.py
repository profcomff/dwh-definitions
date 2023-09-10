import os

from alembic.autogenerate import comparators
from sqlalchemy import text

from .operations_groups import CreateGroupOp, DeleteGroupOp, GrantOnSchemaOp, RevokeOnSchemaOp  # noqa
from .operations_tables import GrantRightsOp, RevokeRightsOp


@comparators.dispatch_for("schema")
def compare_groups(autogen_context, upgrade_ops, schemas):
    default_pg_schemas = ['pg_toast', 'information_schema', 'public', 'pg_catalog']
    all_conn_schemas = set()

    for sch in schemas:
        query = text("select schema_name from information_schema.schemata")
        all_conn_schemas.update([sch[0] for sch in autogen_context.connection.execute(query)])

    for schema in default_pg_schemas:
        all_conn_schemas.remove(schema)

    metadata_schemas = autogen_context.metadata.info.setdefault("table_schemas", set())

    # Grant rights on new schemas
    for sch in metadata_schemas.difference(all_conn_schemas):
        tables = autogen_context.metadata.tables
        for render_scope in ['read', 'write', 'all']:
            group_name = f'dwh_{sch}_{render_scope}'.lower()

            # Group existing check
            if group_name not in [
                group[0][1:] for group in autogen_context.connection.execute(text(f'SELECT * FROM pg_group'))
            ]:
                upgrade_ops.ops.append(CreateGroupOp(group_name))
            group_name = (
                f'test_dwh_{sch}_{render_scope}'.lower()
                if os.getenv("ENVIRONMENT") != "production"
                else f'prod_dwh_{sch}_{render_scope}'.lower()
            )  # Так надо
            all_conn_schemas_rights = list(
                autogen_context.connection.execute(
                    text(
                        f"SELECT privilege_type FROM information_schema.usage_privileges WHERE object_schema='{sch}' "
                        f"and grantee='{group_name}'"
                    )
                )
            )
            if 'USAGE' not in all_conn_schemas_rights:
                upgrade_ops.ops.append(GrantOnSchemaOp("_".join(group_name.split("_")[1:]), sch))
            scopes = []
            match render_scope:
                case 'read':
                    scopes = ['SELECT']
                case 'write':
                    scopes = ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT']
                case 'all':
                    scopes = ['ALL']

            # Scopes check
            upgrade_scopes = []
            for table in tables:
                all_conn_scopes = list(
                    autogen_context.connection.execute(
                        text(
                            f"SELECT privilege_type FROM information_schema.role_table_grants WHERE "
                            f"table_schema='{sch}' and grantee='{group_name}'"  # Потому что тут сравнение по УЖЕ СУЩЕСТВУЮЩИМ группам идет
                        )
                    )
                )
                for scope in scopes:
                    if (scope not in all_conn_scopes or not all_conn_scopes) and (table.split(".")[0] == sch):
                        upgrade_scopes.append(scope)
                if table.split(".")[0] == sch:
                    group_name = f'dwh_{sch}_{render_scope}'.lower()
                    upgrade_ops.ops.append(GrantRightsOp(group_name, upgrade_scopes, table))
                    upgrade_scopes = []

    # Revoke rights from deleted schemas
    for sch in all_conn_schemas.difference(metadata_schemas):
        tables = autogen_context.metadata.tables
        for render_scope in ['read', 'write', 'all']:
            group_name = (
                f'test_dwh_{sch}_{render_scope}'.lower()
                if os.getenv("ENVIRONMENT") != "production"
                else f'prod_dwh_{sch}_{render_scope}'.lower()
            )
            upgrade_ops.ops.append(DeleteGroupOp(group_name))
            all_conn_scopes = list(
                autogen_context.connection.execute(
                    text(
                        f"SELECT privilege_type FROM information_schema.role_table_grants WHERE "
                        f"table_schema='{sch}' and grantee='{group_name}'"
                    )
                )
            )
            delete_scopes = [scope for scope in all_conn_scopes]
            for table in tables:
                if sch == table.split(".")[0]:
                    upgrade_ops.ops.append(RevokeRightsOp(group_name, delete_scopes, table))

    # Grant rights on new tables in existing schemas
    for sch in all_conn_schemas.intersection(metadata_schemas):
        metadata_tables = autogen_context.metadata.tables
        all_conn_tables = set()
        all_conn_tables.update(
            [
                table
                for table in autogen_context.connection.execute(
                    text(f"SELECT * FROM pg_tables WHERE schemaname='{sch}'")
                )
            ]
        )

        for new_table in metadata_tables:
            if new_table.split('.')[0] == sch and new_table.split('.')[1] not in [
                table[1] for table in all_conn_tables
            ]:
                for render_scope in ['read', 'write', 'all']:
                    render_group_name = f'dwh_{sch}_{render_scope}'.lower()
                    group_name = (
                        f'test_dwh_{sch}_{render_scope}'.lower()
                        if os.getenv("ENVIRONMENT") != "production"
                        else f'prod_dwh_{sch}_{render_scope}'.lower()
                    )
                    upgrade_scopes = []
                    all_conn_scopes = list(
                        autogen_context.connection.execute(
                            text(
                                f"SELECT privilege_type FROM information_schema.role_table_grants WHERE "
                                f"table_schema='{sch}' and grantee='{group_name}'"
                                # Потому что тут сравнение по УЖЕ СУЩЕСТВУЮЩИМ группам идет
                            )
                        )
                    )
                    if (render_scope not in all_conn_scopes or not all_conn_scopes) and (
                        new_table.split(".")[0] == sch
                    ):
                        upgrade_scopes.append(render_scope)
                    if new_table.split(".")[0] == sch:
                        group_name = f'dwh_{sch}_{render_scope}'.lower()
                        upgrade_ops.ops.append(GrantRightsOp(group_name, upgrade_scopes, new_table))
                        upgrade_scopes = []

    # Revoke rights on removed tables in existing schemas
    for sch in all_conn_schemas:
        metadata_tables = autogen_context.metadata.tables
        all_conn_tables = set()
        all_conn_tables.update(
            [
                table
                for table in autogen_context.connection.execute(
                    text(f"SELECT * FROM pg_tables WHERE schemaname='{sch}'")
                )
            ]
        )
        for removed_table in all_conn_tables:
            if removed_table[1] not in [table.split('.')[1] for table in metadata_tables]:
                for render_scope in ['read', 'write', 'all']:
                    group_name = (
                        f'test_dwh_{sch}_{render_scope}'.lower()
                        if os.getenv("ENVIRONMENT") != "production"
                        else f'prod_dwh_{sch}_{render_scope}'.lower()
                    )
                    all_conn_scopes = list(
                        autogen_context.connection.execute(
                            text(
                                f"SELECT privilege_type FROM information_schema.role_table_grants WHERE "
                                f"table_schema='{sch}' and grantee='{group_name}'"
                            )
                        )
                    )
                    delete_scopes = [scope for scope in all_conn_scopes]
                    upgrade_ops.ops.append(RevokeRightsOp(group_name, delete_scopes, ".".join(removed_table[0:2])))
