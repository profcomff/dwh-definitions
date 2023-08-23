from alembic.autogenerate import renderers

from .operations import CreateTableSchemaOp, DropTableSchemaOp


@renderers.dispatch_for(CreateTableSchemaOp)
def render_create_sequence(autogen_context, op):
    return f'op.create_table_schema("{op.table_schema_name}")'


@renderers.dispatch_for(DropTableSchemaOp)
def render_drop_sequence(autogen_context, op):
    return f'op.drop_table_schema("{op.table_schema_name}")'
