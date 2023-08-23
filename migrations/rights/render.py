from alembic.autogenerate import renderers

from .operations import CreateGroupOp, DeleteGroupOp


@renderers.dispatch_for(CreateGroupOp)
def render_create_group(autogen_context, op):
    return f'op.create_group("{op.group_name}")'


@renderers.dispatch_for(DeleteGroupOp)
def render_drop_group(autogen_context, op):
    return f'op.delete_group("{op.group_name}")'
