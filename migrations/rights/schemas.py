from alembic.autogenerate import comparators
from sqlalchemy import text

from .operations import CreateGroupOp, DeleteGroupOp


@comparators.dispatch_for("schema")
def compare_sequences(autogen_context, upgrade_ops, schemas):
    all_conn_groups = set()

    for sch in schemas:
        query = text(
            "SELECT relname FROM pg_class c join pg_namespace n on n.oid=c.relnamespace where relkind='S' and "
            "n.nspname=:nspname"
        )
        all_conn_groups.update(
            [
                sch
                for row in autogen_context.connection.execute(
                    query, {"nspname": autogen_context.dialect.default_schema_name if sch is None else sch}
                )
            ]
        )

    metadata_schemas = autogen_context.metadata.info.setdefault("table_schemas", set())
    for sch in metadata_schemas.difference(all_conn_groups):
        for scope in ['read', 'write', 'all']:
            group_name = f'dwh_{sch}_{scope}'
            upgrade_ops.ops.append(CreateGroupOp(group_name))

    for sch in all_conn_groups.difference(metadata_schemas):
        upgrade_ops.ops.append(DeleteGroupOp(sch))
