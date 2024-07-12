import os

from alembic.autogenerate import comparators
from sqlalchemy import text

from .operations_groups import CreateGroupOp, DeleteGroupOp, GrantOnSchemaOp, RevokeOnSchemaOp
from .operations_schemas import CreateTableSchemaOp, DropTableSchemaOp
from .operations_tables import GrantRightsOp, RevokeRightsOp


def add_table_schema_to_model(table_schema, metadata):
    metadata.info.setdefault("table_schemas", set()).add(table_schema)


@comparators.dispatch_for("schema")
def compare_schemas(autogen_context, upgrade_ops, schemas):
    all_conn_schemas = set()
    default_pg_schemas = ['pg_toast', 'information_schema', 'public', 'pg_catalog']
    query = text("select schema_name from information_schema.schemata")
    all_conn_schemas.update(
        [sch[0] for sch in autogen_context.connection.execute(query) if sch[0] not in default_pg_schemas]
    )

    metadata_schemas = autogen_context.metadata.info.setdefault("table_schemas", set())

    for sch in metadata_schemas - all_conn_schemas:
        upgrade_ops.ops.append(CreateTableSchemaOp(sch))
        for render_scope in ['read', 'write', 'all']:
            group_name = (
                f'test_dwh_{sch}_{render_scope}'.lower()
                if os.getenv("ENVIRONMENT") != "production"
                else f'prod_dwh_{sch}_{render_scope}'.lower()
            )
            upgrade_ops.ops.append(CreateGroupOp(group_name))
            upgrade_ops.ops.append(GrantOnSchemaOp(group_name, sch))

        tables = set([table for table in autogen_context.metadata.tables.values() if table.schema == sch])
        for table in tables:
            for render_scope in ['read', 'write', 'all']:
                scopes = []
                match render_scope:
                    case 'read':
                        scopes = ['SELECT']
                    case 'write':
                        scopes = ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT']
                    case 'all':
                        scopes = ['ALL']

                group_name = (
                    f'test_dwh_{sch}_{render_scope}'.lower()
                    if os.getenv("ENVIRONMENT") != "production"
                    else f'prod_dwh_{sch}_{render_scope}'.lower()
                )
                upgrade_ops.ops.append(GrantRightsOp(table_name=str(table), scopes=scopes, group_name=group_name))

    for sch in all_conn_schemas - metadata_schemas:
        upgrade_ops.ops.append(DropTableSchemaOp(sch))
        for render_scope in ['read', 'write', 'all']:
            group_name = (
                f'test_dwh_{sch}_{render_scope}'.lower()
                if os.getenv("ENVIRONMENT") != "production"
                else f'prod_dwh_{sch}_{render_scope}'.lower()
            )
            upgrade_ops.ops.append(DeleteGroupOp(group_name))
            upgrade_ops.ops.append(RevokeOnSchemaOp(group_name, sch))

        query = text(f"SELECT * FROM information_schema.tables WHERE table_schema='{sch}';")
        tables = set([".".join(table[1:3]) for table in autogen_context.connection.execute(query)])
        print(tables)
        for table in tables:
            for render_scope in ['read', 'write', 'all']:
                scopes = []
                match render_scope:
                    case 'read':
                        scopes = ['SELECT']
                    case 'write':
                        scopes = ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT']
                    case 'all':
                        scopes = ['ALL']

                group_name = (
                    f'test_dwh_{sch}_{render_scope}'.lower()
                    if os.getenv("ENVIRONMENT") != "production"
                    else f'prod_dwh_{sch}_{render_scope}'.lower()
                )
                upgrade_ops.ops.append(RevokeRightsOp(table_name=str(table), scopes=scopes, group_name=group_name))
