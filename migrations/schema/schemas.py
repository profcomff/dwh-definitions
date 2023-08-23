from alembic.autogenerate import comparators
from sqlalchemy import text

from .operations import CreateTableSchemaOp, DropTableSchemaOp


def add_table_schema_to_model(table_schema, metadata):
    metadata.info.setdefault("table_schemas", set()).add(table_schema)


@comparators.dispatch_for("schema")
def compare_schemas(autogen_context, upgrade_ops, schemas):
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

    for sch in metadata_schemas.difference(all_conn_schemas):
        upgrade_ops.ops.append(CreateTableSchemaOp(sch))

    for sch in all_conn_schemas.difference(metadata_schemas):
        upgrade_ops.ops.append(DropTableSchemaOp(sch))
