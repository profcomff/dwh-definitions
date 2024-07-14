from alembic.autogenerate import renderers

from .operations_groups import CreateGroupOp, DeleteGroupOp, GrantOnSchemaOp, RevokeOnSchemaOp
from .operations_schemas import CreateTableSchemaOp, DropTableSchemaOp
from .operations_tables import GrantRightsOp, RevokeRightsOp


@renderers.dispatch_for(CreateTableSchemaOp)
def render_create_sequence(autogen_context, op):
    return f'op.create_table_schema("{op.table_schema_name}")'


@renderers.dispatch_for(DropTableSchemaOp)
def render_drop_sequence(autogen_context, op):
    return f'op.drop_table_schema("{op.table_schema_name}")'


@renderers.dispatch_for(CreateGroupOp)
def render_create_group(autogen_context, op):
    render_group = '_'.join(op.group_name.split('_')[1:])
    return (
        f'op.create_group("test_{render_group}" if os.getenv("ENVIRONMENT") != "production" else "prod_{render_group}")'
    )


@renderers.dispatch_for(DeleteGroupOp)
def render_drop_group(autogen_context, op):
    render_group = '_'.join(op.group_name.split('_')[1:])
    return (
        f'op.delete_group("test_{render_group}" if os.getenv("ENVIRONMENT") != "production" else "prod_{render_group}")'
    )


@renderers.dispatch_for(GrantOnSchemaOp)
def render_schema_grant(autogen_context, op):
    render_group = '_'.join(op.group_name.split('_')[1:])
    return (
        f'op.grant_on_schema("test_{render_group}" if os.getenv("ENVIRONMENT") != "production" else "prod_{render_group}", '
        f'"{op.schema}")'
    )


@renderers.dispatch_for(RevokeOnSchemaOp)
def render_schema_revoke(autogen_context, op):
    render_group = '_'.join(op.group_name.split('_')[1:])
    return (
        f'op.revoke_on_schema("test_{render_group}" if os.getenv("ENVIRONMENT") != "production" else "prod_{render_group}", '
        f'"{op.schema}")'
    )


@renderers.dispatch_for(GrantRightsOp)
def render_table_grant(autogen_context, op):
    table = f"""'"{op.table_name.split(".")[0]}".{op.table_name.split(".")[1]}'"""
    render_group = '_'.join(op.group_name.split('_')[1:])
    return (
        f'op.grant_on_table("test_{render_group}" if os.getenv("ENVIRONMENT") != "production" else "prod_{render_group}", '
        f'{op.scopes}, {table})'
    )


@renderers.dispatch_for(RevokeRightsOp)
def render_table_revoke(autogen_context, op):
    table = f"""'"{op.table_name.split(".")[0]}".{op.table_name.split(".")[1]}'"""
    render_group = '_'.join(op.group_name.split('_')[1:])
    return (
        f'op.revoke_on_table("test_{render_group}" if os.getenv("ENVIRONMENT") != "production" else "prod_{render_group}", '
        f'{op.scopes}, {table})'
    )
