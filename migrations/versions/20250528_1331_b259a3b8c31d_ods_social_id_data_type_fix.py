"""ods_social_id_data_type_fix

Revision ID: b259a3b8c31d
Revises: 31293ac08820
Create Date: 2025-05-28 13:31:04.540947

"""

import os

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = 'b259a3b8c31d'
down_revision = '31293ac08820'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_column("git_hub", "issue_id", schema="ODS_SOCIAL")
    op.add_column("git_hub", sa.Column("issue_id", sa.String()), schema="ODS_SOCIAL")
    op.drop_column("git_hub", "user_id", schema="ODS_SOCIAL")
    op.add_column("git_hub", sa.Column("user_id", sa.String()), schema="ODS_SOCIAL")
    op.drop_column("git_hub", "repository_id", schema="ODS_SOCIAL")
    op.add_column("git_hub", sa.Column("repository_id", sa.String()), schema="ODS_SOCIAL"),
    op.drop_column("git_hub", "assignee_id", schema="ODS_SOCIAL")
    op.add_column("git_hub", sa.Column("assignee_id", sa.String()), schema="ODS_SOCIAL")
    op.drop_column("git_hub", "organization_id", schema="ODS_SOCIAL")
    op.add_column("git_hub", sa.Column("organization_id", sa.String()), schema="ODS_SOCIAL")


def downgrade():
    op.drop_column("git_hub", "issue_id", schema="ODS_SOCIAL")
    op.add_column("git_hub", sa.Column("issue_id", sa.Integer()), schema="ODS_SOCIAL")
    op.drop_column("git_hub", "user_id", schema="ODS_SOCIAL")
    op.add_column("git_hub", sa.Column("user_id", sa.Integer()), schema="ODS_SOCIAL")
    op.drop_column("git_hub", "repository_id", schema="ODS_SOCIAL")
    op.add_column("git_hub", sa.Column("repository_id", sa.Integer()), schema="ODS_SOCIAL"),
    op.drop_column("git_hub", "assignee_id", schema="ODS_SOCIAL")
    op.add_column("git_hub", sa.Column("assignee_id", sa.Integer()), schema="ODS_SOCIAL")
    op.drop_column("git_hub", "organization_id", schema="ODS_SOCIAL")
    op.add_column("git_hub", sa.Column("organization_id", sa.Integer()), schema="ODS_SOCIAL")
