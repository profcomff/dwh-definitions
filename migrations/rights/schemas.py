from alembic.autogenerate import comparators
from sqlalchemy import text

from .operations_groups import CreateGroupOp, DeleteGroupOp
from .operations_tables import GrantRightsOp, RevokeRightsOp


@comparators.dispatch_for("schema")
def compare_groups(autogen_context, upgrade_ops, schemas):
    all_conn_schemas = set()

    for sch in schemas:
        query = text(
            "SELECT relname FROM pg_class c join pg_namespace n on n.oid=c.relnamespace where relkind='S' and "
            "n.nspname=:nspname"
        )
        all_conn_schemas.update(
            [
                sch
                for row in autogen_context.connection.execute(
                query, {"nspname": autogen_context.dialect.default_schema_name if sch is None else sch}
            )
            ]
        )

    metadata_schemas = autogen_context.metadata.info.setdefault("table_schemas", set())

    # Grant rights on new schemas
    for sch in metadata_schemas.difference(all_conn_schemas):
        tables = autogen_context.metadata.tables
        for scope in ['read', 'write', 'all']:
            group_name = f'dwh_{sch}_{scope}'
            upgrade_ops.ops.append(CreateGroupOp(group_name))
            for table in tables:
                if sch == table.split(".")[0]:
                    upgrade_ops.ops.append(GrantRightsOp(group_name, table))

    # Revoke rights from deleted schemas
    for sch in all_conn_schemas.difference(metadata_schemas):
        tables = autogen_context.metadata.tables
        for scope in ['read', 'write', 'all']:
            group_name = f'dwh_{sch}_{scope}'
            upgrade_ops.ops.append(DeleteGroupOp(sch))
            for table in tables:
                if sch == table.split(".")[0]:
                    upgrade_ops.ops.append(RevokeRightsOp(group_name, table))

    # Grant rights on new tables in existing schemas
    for sch in all_conn_schemas.intersection(metadata_schemas):
        metadata_tables = autogen_context.metadata.tables
        all_conn_tables = set()
        all_conn_tables.update(
            [
                table for table in autogen_context.connection.execute(text(f"SELECT * FROM pg_tables WHERE schemaname='{sch}'"))
            ]
        )

        for new_table in metadata_tables:
            if new_table.split('.')[0] == sch and new_table.split('.')[1] not in [table[1] for table in all_conn_tables]:
                for scope in ['read', 'write', 'all']:
                    group_name = f'dwh_{sch}_{scope}'
                    upgrade_ops.ops.append(GrantRightsOp(group_name, new_table))

    # Revoke rights on removed tables in existing schemas
    for sch in all_conn_schemas.intersection(metadata_schemas):
        metadata_tables = autogen_context.metadata.tables
        all_conn_tables = set()
        all_conn_tables.update(
            [
                table for table in autogen_context.connection.execute(text(f"SELECT * FROM pg_tables WHERE schemaname='{sch}'"))
            ]
        )
        for removed_table in all_conn_tables:
            if removed_table[1] not in [table.split('.')[1] for table in metadata_tables]:
                for scope in ['read', 'write', 'all']:
                    group_name = f'dwh_{sch}_{scope}'
                    upgrade_ops.ops.append(RevokeRightsOp(group_name, ".".join([removed_table[0], removed_table[1]])))

            # if removed_table.split('.')[0] == sch and removed_table.split('.')[1] not in [table[1] for table in all_conn_tables]:
            #     for scope in ['read', 'write', 'all']:
            #         group_name = f'dwh_{sch}_{scope}'
            #         upgrade_ops.ops.append(GrantRightsOp(group_name, new_table.split('.')[1]))
