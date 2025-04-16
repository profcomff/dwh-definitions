"""add ods telegram viribus

Revision ID: 2685b42bfef5
Revises: 066fd36bb01c
Create Date: 2025-04-15 21:40:45.903706

"""

from alembic import op
import sqlalchemy as sa
import os


# revision identifiers, used by Alembic.
revision = '2685b42bfef5'
down_revision = '066fd36bb01c'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table_schema("ODS_SOCIAL")
    op.create_table(
        'lecturer',
        sa.Column('uuid', sa.Uuid(), nullable=False, comment='Техническое поле в dwh'),
        sa.Column('thread_name', sa.String(), nullable=False, comment='Название ветки в сообществе, например Frontend'),
        sa.Column('message_text', sa.String(), nullable=False, comment='Текст сообщения в телеграме'),
        sa.Column('sender_telegram_login', sa.String(), nullable=False, comment='Логин пользователя в телеграме'),
        sa.Column('message_ts', sa.DateTime(), nullable=False, comment='Таймстемп записи в social-api'),
        sa.PrimaryKeyConstraint('uuid'),
        schema='ODS_SOCIAL',
        comment='\n    Преподаватели в rating-api\n    ',
        info={'sensitive': False},
    )
    op.create_group(
        "test_dwh_ods_social_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_social_read"
    )
    op.create_group(
        "test_dwh_ods_social_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_social_write"
    )
    op.create_group(
        "test_dwh_ods_social_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_social_all"
    )
    op.grant_on_schema(
        "test_dwh_ods_social_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_social_read",
        "ODS_SOCIAL",
    )
    op.grant_on_schema(
        "test_dwh_ods_social_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_social_write",
        "ODS_SOCIAL",
    )
    op.grant_on_schema(
        "test_dwh_ods_social_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_social_all",
        "ODS_SOCIAL",
    )
    op.grant_on_table(
        "test_dwh_ods_social_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_social_read",
        ['SELECT'],
        '"ODS_SOCIAL".lecturer',
    )
    op.grant_on_table(
        "test_dwh_ods_social_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_social_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_SOCIAL".lecturer',
    )
    op.grant_on_table(
        "test_dwh_ods_social_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_social_all",
        ['ALL'],
        '"ODS_SOCIAL".lecturer',
    )


def downgrade():
    op.revoke_on_table(
        "test_dwh_ods_social_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_social_all",
        ['ALL'],
        '"ODS_SOCIAL".lecturer',
    )
    op.revoke_on_table(
        "test_dwh_ods_social_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_social_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_SOCIAL".lecturer',
    )
    op.revoke_on_table(
        "test_dwh_ods_social_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_social_read",
        ['SELECT'],
        '"ODS_SOCIAL".lecturer',
    )
    op.revoke_on_schema(
        "test_dwh_ods_social_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_social_all",
        "ODS_SOCIAL",
    )
    op.revoke_on_schema(
        "test_dwh_ods_social_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_social_write",
        "ODS_SOCIAL",
    )
    op.revoke_on_schema(
        "test_dwh_ods_social_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_social_read",
        "ODS_SOCIAL",
    )
    op.drop_table('lecturer', schema='ODS_SOCIAL')
    op.delete_group(
        "test_dwh_ods_social_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_social_all"
    )
    op.delete_group(
        "test_dwh_ods_social_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_social_write"
    )
    op.delete_group(
        "test_dwh_ods_social_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_social_read"
    )
    op.drop_table_schema("ODS_SOCIAL")
