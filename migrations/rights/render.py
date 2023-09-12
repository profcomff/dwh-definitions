from alembic.autogenerate import renderers

from .operations_groups import CreateGroupOp, DeleteGroupOp, GrantOnSchemaOp, RevokeOnSchemaOp
from .operations_tables import GrantRightsOp, RevokeRightsOp


@renderers.dispatch_for(CreateGroupOp)
def render_create_group(autogen_context, op):
    return f'op.create_group("test_{op.group_name}" if os.getenv("ENVIRONMENT") != "production" else "prod_{op.group_name}")'


@renderers.dispatch_for(DeleteGroupOp)
def render_drop_group(autogen_context, op):
    return f'op.delete_group("test_{op.group_name}" if os.getenv("ENVIRONMENT") != "production" else "prod_{op.group_name}")'


@renderers.dispatch_for(GrantOnSchemaOp)
def render_schema_grant(autogen_context, op):
    return (
        f'op.grant_on_schema("test_{op.group_name}" if os.getenv("ENVIRONMENT") != "production" else "prod_{op.group_name}", '
        f'"{op.schema}")'
    )


@renderers.dispatch_for(RevokeOnSchemaOp)
def render_schema_revoke(autogen_context, op):
    return (
        f'op.revoke_on_schema("test_{op.group_name}" if os.getenv("ENVIRONMENT") != "production" else "prod_{op.group_name}", '
        f'"{op.schema}")'
    )


@renderers.dispatch_for(GrantRightsOp)
def render_table_grant(autogen_context, op):
    table = f"""'"{op.table_name.split(".")[0]}".{op.table_name.split(".")[1]}'"""
    return (
        f'op.grant_on_table("test_{op.group_name}" if os.getenv("ENVIRONMENT") != "production" else "prod_{op.group_name}", '
        f'{op.scopes}, {table})'
    )


@renderers.dispatch_for(RevokeRightsOp)
def render_table_revoke(autogen_context, op):
    table = f"""'"{op.table_name.split(".")[0]}".{op.table_name.split(".")[1]}'"""
    return (
        f'op.revoke_on_table("test_{op.group_name}" if os.getenv("ENVIRONMENT") != "production" else "prod_{op.group_name}", '
        f'{op.scopes}, {table})'
    )
