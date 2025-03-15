"""add redirector+userdata

Revision ID: eefb1c66dcfe
Revises: c335441a4bf8
Create Date: 2025-03-15 19:31:49.023516

"""

import os

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = 'eefb1c66dcfe'
down_revision = 'c335441a4bf8'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table_schema("STG_REDIRECTOR")
    op.create_table(
        'union_member_card',
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('card_id', sa.Integer(), nullable=True),
        sa.Column(
            'card_number', sa.String(), nullable=True, comment="card number - number of user's card from ODS.user.info"
        ),
        sa.PrimaryKeyConstraint('user_id'),
        schema='DM_USER',
        info={'sensitive': False},
    )
    op.create_table(
        'link',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('url_from', sa.String(), nullable=False),
        sa.Column('url_to', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('url_from'),
        schema='STG_REDIRECTOR',
        info={'sensitive': False},
    )
    op.create_table(
        'redirect_fact',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('link_id', sa.Integer(), nullable=False),
        sa.Column('method', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('user_agent', sa.String(), nullable=False),
        sa.Column('browser_family', sa.String(), nullable=True),
        sa.Column('browser_version', sa.String(), nullable=True),
        sa.Column('os_family', sa.String(), nullable=True),
        sa.Column('os_version', sa.String(), nullable=True),
        sa.Column('device_family', sa.String(), nullable=True),
        sa.Column('device_brand', sa.String(), nullable=True),
        sa.Column('device_model', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_REDIRECTOR',
        info={'sensitive': False},
    )
    op.create_group(
        "test_dwh_stg_redirector_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_redirector_read"
    )
    op.create_group(
        "test_dwh_stg_redirector_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_redirector_write"
    )
    op.create_group(
        "test_dwh_stg_redirector_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_redirector_all"
    )
    op.grant_on_schema(
        "test_dwh_stg_redirector_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_redirector_read",
        "STG_REDIRECTOR",
    )
    op.grant_on_schema(
        (
            "test_dwh_stg_redirector_write"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_redirector_write"
        ),
        "STG_REDIRECTOR",
    )
    op.grant_on_schema(
        "test_dwh_stg_redirector_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_redirector_all",
        "STG_REDIRECTOR",
    )
    op.grant_on_table(
        "test_dwh_stg_redirector_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_redirector_read",
        ['SELECT'],
        '"STG_REDIRECTOR".link',
    )
    op.grant_on_table(
        (
            "test_dwh_stg_redirector_write"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_redirector_write"
        ),
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_REDIRECTOR".link',
    )
    op.grant_on_table(
        "test_dwh_stg_redirector_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_redirector_all",
        ['ALL'],
        '"STG_REDIRECTOR".link',
    )
    op.grant_on_table(
        "test_dwh_stg_redirector_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_redirector_read",
        ['SELECT'],
        '"STG_REDIRECTOR".redirect_fact',
    )
    op.grant_on_table(
        (
            "test_dwh_stg_redirector_write"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_redirector_write"
        ),
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_REDIRECTOR".redirect_fact',
    )
    op.grant_on_table(
        "test_dwh_stg_redirector_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_redirector_all",
        ['ALL'],
        '"STG_REDIRECTOR".redirect_fact',
    )
    op.create_index(
        op.f('ix_DM_USER_union_member_card_user_id'), 'union_member_card', ['user_id'], unique=False, schema='DM_USER'
    )
    op.create_table_comment(
        'frontend_actions',
        '\n    Фронтендовые события\n    ',
        existing_comment='Фронтендовые события',
        schema='ODS_MARKETING',
    )
    op.create_table_comment(
        'printer_actions', '\n    Действия принтера\n    ', existing_comment='Действия принтера', schema='ODS_MARKETING'
    )
    op.create_table_comment(
        'printer_bots_actions',
        '\n    Действия ботов принтера в вк и тг\n    ',
        existing_comment='Действия ботов принтера в вк и тг',
        schema='ODS_MARKETING',
    )
    op.create_table_comment(
        'rating_actions',
        '\n    События в рейтинге\n    ',
        existing_comment='События в рейтинге',
        schema='ODS_MARKETING',
    )


def downgrade():
    op.create_table_comment(
        'rating_actions',
        'События в рейтинге',
        existing_comment='\n    События в рейтинге\n    ',
        schema='ODS_MARKETING',
    )
    op.create_table_comment(
        'printer_bots_actions',
        'Действия ботов принтера в вк и тг',
        existing_comment='\n    Действия ботов принтера в вк и тг\n    ',
        schema='ODS_MARKETING',
    )
    op.create_table_comment(
        'printer_actions', 'Действия принтера', existing_comment='\n    Действия принтера\n    ', schema='ODS_MARKETING'
    )
    op.create_table_comment(
        'frontend_actions',
        'Фронтендовые события',
        existing_comment='\n    Фронтендовые события\n    ',
        schema='ODS_MARKETING',
    )
    op.drop_index(op.f('ix_DM_USER_union_member_card_user_id'), table_name='union_member_card', schema='DM_USER')
    op.revoke_on_table(
        "test_dwh_stg_redirector_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_redirector_all",
        ['ALL'],
        '"STG_REDIRECTOR".redirect_fact',
    )
    op.revoke_on_table(
        (
            "test_dwh_stg_redirector_write"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_redirector_write"
        ),
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_REDIRECTOR".redirect_fact',
    )
    op.revoke_on_table(
        "test_dwh_stg_redirector_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_redirector_read",
        ['SELECT'],
        '"STG_REDIRECTOR".redirect_fact',
    )
    op.revoke_on_table(
        "test_dwh_stg_redirector_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_redirector_all",
        ['ALL'],
        '"STG_REDIRECTOR".link',
    )
    op.revoke_on_table(
        (
            "test_dwh_stg_redirector_write"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_redirector_write"
        ),
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_REDIRECTOR".link',
    )
    op.revoke_on_table(
        "test_dwh_stg_redirector_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_redirector_read",
        ['SELECT'],
        '"STG_REDIRECTOR".link',
    )
    op.revoke_on_schema(
        "test_dwh_stg_redirector_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_redirector_all",
        "STG_REDIRECTOR",
    )
    op.revoke_on_schema(
        (
            "test_dwh_stg_redirector_write"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_redirector_write"
        ),
        "STG_REDIRECTOR",
    )
    op.revoke_on_schema(
        "test_dwh_stg_redirector_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_redirector_read",
        "STG_REDIRECTOR",
    )
    op.drop_table('redirect_fact', schema='STG_REDIRECTOR')
    op.drop_table('link', schema='STG_REDIRECTOR')
    op.drop_table('union_member_card', schema='DM_USER')
    op.delete_group(
        "test_dwh_stg_redirector_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_redirector_all"
    )
    op.delete_group(
        "test_dwh_stg_redirector_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_redirector_write"
    )
    op.delete_group(
        "test_dwh_stg_redirector_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_redirector_read"
    )
    op.drop_table_schema("STG_REDIRECTOR")
