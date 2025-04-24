"""fix chat

Revision ID: d43d62fb3748
Revises: 40d72f2dd950
Create Date: 2025-04-16 08:27:47.916638

"""

import os

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = 'd43d62fb3748'
down_revision = '40d72f2dd950'
branch_labels = None
depends_on = None


def upgrade():
    op.grant_on_table(
        "test_dwh_ods_social_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_social_read",
        ['SELECT'],
        '"ODS_SOCIAL".viribus_chat',
    )
    op.grant_on_table(
        "test_dwh_ods_social_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_social_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_SOCIAL".viribus_chat',
    )
    op.grant_on_table(
        "test_dwh_ods_social_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_social_all",
        ['ALL'],
        '"ODS_SOCIAL".viribus_chat',
    )


def downgrade():
    op.revoke_on_table(
        "test_dwh_ods_social_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_social_all",
        ['ALL'],
        '"ODS_SOCIAL".viribus_chat',
    )
    op.revoke_on_table(
        "test_dwh_ods_social_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_social_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_SOCIAL".viribus_chat',
    )
    op.revoke_on_table(
        "test_dwh_ods_social_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_social_read",
        ['SELECT'],
        '"ODS_SOCIAL".viribus_chat',
    )
