from alembic.autogenerate import renderers

from .operations_groups import CreateGroupOp, DeleteGroupOp
from .operations_tables import GrantRightsOp, RevokeRightsOp


@renderers.dispatch_for(CreateGroupOp)
def render_create_group(autogen_context, op):
    return f'op.create_group("{op.group_name}")'


@renderers.dispatch_for(DeleteGroupOp)
def render_drop_group(autogen_context, op):
    return f'op.delete_group("{op.group_name}")'


@renderers.dispatch_for(GrantRightsOp)
def render_grant_rights(autogen_context, op):
    table = f"""'"{op.table_name.split(".")[0]}".{op.table_name.split(".")[1]}'"""
    return f'op.grant_rights("{op.group_name}", "{op.scopes}", {table})'


@renderers.dispatch_for(RevokeRightsOp)
def render_revoke_rights(autogen_context, op):
    table = f"""'"{op.table_name.split(".")[0]}".{op.table_name.split(".")[1]}'"""
    return f'op.revoke_rights("{op.group_name}", "{op.scopes}", {table})'
