import os
from pathlib import Path

import dotenv
from alembic.autogenerate import renderers

from .operations_groups import CreateGroupOp, DeleteGroupOp
from .operations_tables import GrantRightsOp, RevokeRightsOp


REPO_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent.parent.resolve()
dotenv.load_dotenv(REPO_ROOT / ".env")


@renderers.dispatch_for(CreateGroupOp)
def render_create_group(autogen_context, op):
    group_name = f"test_{op.group_name}" if os.getenv("ENVIRONMENT") != "production" else f"prod_{op.group_name}"
    return f'op.create_group("{group_name}")'


@renderers.dispatch_for(DeleteGroupOp)
def render_drop_group(autogen_context, op):
    group_name = f"test_{op.group_name}" if os.getenv("ENVIRONMENT") != "production" else f"prod_{op.group_name}"
    return f'op.delete_group("{group_name}")'


@renderers.dispatch_for(GrantRightsOp)
def render_grant_rights(autogen_context, op):
    table = f"""'"{op.table_name.split(".")[0]}".{op.table_name.split(".")[1]}'"""
    group_name = f"test_{op.group_name}" if os.getenv("ENVIRONMENT") != "production" else f"prod_{op.group_name}"
    return f'op.grant_rights("{group_name}", "{op.scopes}", {table})'


@renderers.dispatch_for(RevokeRightsOp)
def render_revoke_rights(autogen_context, op):
    table = f"""'"{op.table_name.split(".")[0]}".{op.table_name.split(".")[1]}'"""
    group_name = f"test_{op.group_name}" if os.getenv("ENVIRONMENT") != "production" else f"prod_{op.group_name}"
    return f'op.revoke_rights("{group_name}", "{op.scopes}", {table})'
