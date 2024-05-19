"""Schema integrity fixes

Revision ID: a80b250420e4
Revises: 4892e78eb989
Create Date: 2024-05-05 00:10:07.530090

"""

import os

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = 'a80b250420e4'
down_revision = '1e868db5c6ea'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_table('vk_groups', schema='STG_SOCIAL')
    op.create_table_schema("STG_RASPHYSMSU")
    op.create_table_schema("STG_ACHIEVEMENT")
    op.create_table(
        'achievement',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('picture', sa.String(), nullable=True),
        sa.Column('owner_user_id', sa.Integer(), nullable=True),
        sa.Column('create_ts', sa.DateTime(), nullable=True),
        sa.Column('update_ts', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_ACHIEVEMENT',
    )
    op.create_table(
        'achievement_receiver',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.Column('achievement_id', sa.Integer(), nullable=True),
        sa.Column('create_ts', sa.DateTime(), nullable=True),
        sa.Column('update_ts', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_ACHIEVEMENT',
    )
    op.create_table(
        'dynamic_option',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('create_ts', sa.DateTime(), nullable=True),
        sa.Column('value_integer', sa.Integer(), nullable=True),
        sa.Column('value_string', sa.String(), nullable=True),
        sa.Column('value_double', sa.Float(), nullable=True),
        sa.Column('update_ts', sa.DateTime(), nullable=True),
        sa.Column('name', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_AUTH',
    )
    op.create_table(
        'raw_html',
        sa.Column('url', sa.String(), nullable=False),
        sa.Column('raw_html', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('url'),
        schema='STG_RASPHYSMSU',
    )
    op.create_table(
        'raw_html_old',
        sa.Column('url', sa.String(), nullable=False),
        sa.Column('raw_html', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('url'),
        schema='STG_RASPHYSMSU',
    )
    op.create_table(
        'create_group_request',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('valid_ts', sa.DateTime(), nullable=True),
        sa.Column('create_ts', sa.DateTime(), nullable=True),
        sa.Column('owner_id', sa.Integer(), nullable=True),
        sa.Column('mapped_group_id', sa.Integer(), nullable=True),
        sa.Column('secret_key', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_SOCIAL',
    )
    op.create_table(
        'group',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('update_ts', sa.DateTime(), nullable=True),
        sa.Column('create_ts', sa.DateTime(), nullable=True),
        sa.Column('last_active_ts', sa.DateTime(), nullable=True),
        sa.Column('owner_id', sa.Integer(), nullable=True),
        sa.Column('is_deleted', sa.Boolean(), nullable=True),
        sa.Column('type', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_SOCIAL',
    )
    op.create_table(
        'telegram_channel',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('channel_id', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_SOCIAL',
    )
    op.create_table(
        'telegram_chat',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('chat_id', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_SOCIAL',
    )
    op.create_table(
        'vk_chat',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('peer_id', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_SOCIAL',
    )
    op.create_table(
        'vk_group',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('group_id', sa.Integer(), nullable=True),
        sa.Column('confirmation_token', sa.String(), nullable=True),
        sa.Column('secret_key', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_SOCIAL',
    )
    op.create_group(
        "test_dwh_stg_rasphysmsu_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rasphysmsu_read"
    )
    op.create_group(
        "test_dwh_stg_rasphysmsu_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rasphysmsu_write"
    )
    op.create_group(
        "test_dwh_stg_rasphysmsu_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rasphysmsu_all"
    )
    op.create_group(
        "test_dwh_stg_achievement_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_achievement_read"
    )
    op.create_group(
        "test_dwh_stg_achievement_write"
        if os.getenv("ENVIRONMENT") != "production"
        else "prod_dwh_stg_achievement_write"
    )
    op.create_group(
        "test_dwh_stg_achievement_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_achievement_all"
    )
    op.grant_on_schema(
        "test_dwh_stg_rasphysmsu_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rasphysmsu_read",
        "STG_RASPHYSMSU",
    )
    op.grant_on_schema(
        (
            "test_dwh_stg_rasphysmsu_write"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_rasphysmsu_write"
        ),
        "STG_RASPHYSMSU",
    )
    op.grant_on_schema(
        "test_dwh_stg_rasphysmsu_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rasphysmsu_all",
        "STG_RASPHYSMSU",
    )
    op.grant_on_schema(
        (
            "test_dwh_stg_achievement_read"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_achievement_read"
        ),
        "STG_ACHIEVEMENT",
    )
    op.grant_on_schema(
        (
            "test_dwh_stg_achievement_write"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_achievement_write"
        ),
        "STG_ACHIEVEMENT",
    )
    op.grant_on_schema(
        "test_dwh_stg_achievement_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_achievement_all",
        "STG_ACHIEVEMENT",
    )
    op.grant_on_table(
        "test_dwh_stg_rasphysmsu_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rasphysmsu_read",
        ['SELECT'],
        '"STG_RASPHYSMSU".raw_html',
    )
    op.grant_on_table(
        "test_dwh_stg_rasphysmsu_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rasphysmsu_read",
        ['SELECT'],
        '"STG_RASPHYSMSU".raw_html_old',
    )
    op.grant_on_table(
        (
            "test_dwh_stg_rasphysmsu_write"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_rasphysmsu_write"
        ),
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_RASPHYSMSU".raw_html',
    )
    op.grant_on_table(
        (
            "test_dwh_stg_rasphysmsu_write"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_rasphysmsu_write"
        ),
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_RASPHYSMSU".raw_html_old',
    )
    op.grant_on_table(
        "test_dwh_stg_rasphysmsu_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rasphysmsu_all",
        ['ALL'],
        '"STG_RASPHYSMSU".raw_html',
    )
    op.grant_on_table(
        "test_dwh_stg_rasphysmsu_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rasphysmsu_all",
        ['ALL'],
        '"STG_RASPHYSMSU".raw_html_old',
    )
    op.grant_on_table(
        (
            "test_dwh_stg_achievement_read"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_achievement_read"
        ),
        ['SELECT'],
        '"STG_ACHIEVEMENT".achievement',
    )
    op.grant_on_table(
        (
            "test_dwh_stg_achievement_read"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_achievement_read"
        ),
        ['SELECT'],
        '"STG_ACHIEVEMENT".achievement_receiver',
    )
    op.grant_on_table(
        (
            "test_dwh_stg_achievement_write"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_achievement_write"
        ),
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_ACHIEVEMENT".achievement',
    )
    op.grant_on_table(
        (
            "test_dwh_stg_achievement_write"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_achievement_write"
        ),
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_ACHIEVEMENT".achievement_receiver',
    )
    op.grant_on_table(
        "test_dwh_stg_achievement_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_achievement_all",
        ['ALL'],
        '"STG_ACHIEVEMENT".achievement',
    )
    op.grant_on_table(
        "test_dwh_stg_achievement_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_achievement_all",
        ['ALL'],
        '"STG_ACHIEVEMENT".achievement_receiver',
    )
    op.grant_on_table(
        "test_dwh_stg_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_read",
        ['SELECT'],
        '"STG_AUTH".dynamic_option',
    )
    op.grant_on_table(
        "test_dwh_stg_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_AUTH".dynamic_option',
    )
    op.grant_on_table(
        "test_dwh_stg_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_all",
        ['ALL'],
        '"STG_AUTH".dynamic_option',
    )
    op.grant_on_table(
        "test_dwh_stg_social_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_read",
        ['SELECT'],
        '"STG_SOCIAL".group',
    )
    op.grant_on_table(
        "test_dwh_stg_social_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_SOCIAL".group',
    )
    op.grant_on_table(
        "test_dwh_stg_social_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_all",
        ['ALL'],
        '"STG_SOCIAL".group',
    )
    op.grant_on_table(
        "test_dwh_stg_social_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_read",
        ['SELECT'],
        '"STG_SOCIAL".create_group_request',
    )
    op.grant_on_table(
        "test_dwh_stg_social_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_SOCIAL".create_group_request',
    )
    op.grant_on_table(
        "test_dwh_stg_social_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_all",
        ['ALL'],
        '"STG_SOCIAL".create_group_request',
    )
    op.grant_on_table(
        "test_dwh_stg_social_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_read",
        ['SELECT'],
        '"STG_SOCIAL".vk_group',
    )
    op.grant_on_table(
        "test_dwh_stg_social_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_SOCIAL".vk_group',
    )
    op.grant_on_table(
        "test_dwh_stg_social_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_all",
        ['ALL'],
        '"STG_SOCIAL".vk_group',
    )
    op.grant_on_table(
        "test_dwh_stg_social_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_read",
        ['SELECT'],
        '"STG_SOCIAL".telegram_channel',
    )
    op.grant_on_table(
        "test_dwh_stg_social_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_SOCIAL".telegram_channel',
    )
    op.grant_on_table(
        "test_dwh_stg_social_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_all",
        ['ALL'],
        '"STG_SOCIAL".telegram_channel',
    )
    op.grant_on_table(
        "test_dwh_stg_social_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_read",
        ['SELECT'],
        '"STG_SOCIAL".telegram_chat',
    )
    op.grant_on_table(
        "test_dwh_stg_social_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_SOCIAL".telegram_chat',
    )
    op.grant_on_table(
        "test_dwh_stg_social_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_all",
        ['ALL'],
        '"STG_SOCIAL".telegram_chat',
    )
    op.grant_on_table(
        "test_dwh_stg_social_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_read",
        ['SELECT'],
        '"STG_SOCIAL".vk_chat',
    )
    op.grant_on_table(
        "test_dwh_stg_social_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_SOCIAL".vk_chat',
    )
    op.grant_on_table(
        "test_dwh_stg_social_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_all",
        ['ALL'],
        '"STG_SOCIAL".vk_chat',
    )
    op.alter_column('auth_method', 'user_id', existing_type=sa.INTEGER(), nullable=True, schema='STG_AUTH')
    op.alter_column('auth_method', 'auth_method', existing_type=sa.VARCHAR(), nullable=True, schema='STG_AUTH')
    op.alter_column('auth_method', 'param', existing_type=sa.VARCHAR(), nullable=True, schema='STG_AUTH')
    op.alter_column('auth_method', 'value', existing_type=sa.VARCHAR(), nullable=True, schema='STG_AUTH')
    op.alter_column('auth_method', 'create_ts', existing_type=postgresql.TIMESTAMP(), nullable=True, schema='STG_AUTH')
    op.alter_column('auth_method', 'update_ts', existing_type=postgresql.TIMESTAMP(), nullable=True, schema='STG_AUTH')
    op.alter_column('auth_method', 'is_deleted', existing_type=sa.BOOLEAN(), nullable=True, schema='STG_AUTH')
    op.alter_column('group', 'name', existing_type=sa.VARCHAR(), nullable=True, schema='STG_AUTH')
    op.alter_column('group', 'parent_id', existing_type=sa.INTEGER(), nullable=True, schema='STG_AUTH')
    op.alter_column('group', 'create_ts', existing_type=postgresql.TIMESTAMP(), nullable=True, schema='STG_AUTH')
    op.alter_column('group', 'update_ts', existing_type=postgresql.TIMESTAMP(), nullable=True, schema='STG_AUTH')
    op.alter_column('group', 'is_deleted', existing_type=sa.BOOLEAN(), nullable=True, schema='STG_AUTH')
    op.alter_column('group_scope', 'group_id', existing_type=sa.INTEGER(), nullable=True, schema='STG_AUTH')
    op.alter_column('group_scope', 'scope_id', existing_type=sa.INTEGER(), nullable=True, schema='STG_AUTH')
    op.alter_column('group_scope', 'is_deleted', existing_type=sa.BOOLEAN(), nullable=True, schema='STG_AUTH')
    op.alter_column('scope', 'creator_id', existing_type=sa.INTEGER(), nullable=True, schema='STG_AUTH')
    op.alter_column('scope', 'name', existing_type=sa.VARCHAR(), nullable=True, schema='STG_AUTH')
    op.alter_column('scope', 'comment', existing_type=sa.VARCHAR(), nullable=True, schema='STG_AUTH')
    op.alter_column('scope', 'is_deleted', existing_type=sa.BOOLEAN(), nullable=True, schema='STG_AUTH')
    op.alter_column('user', 'is_deleted', existing_type=sa.BOOLEAN(), nullable=True, schema='STG_AUTH')
    op.alter_column('user', 'create_ts', existing_type=postgresql.TIMESTAMP(), nullable=True, schema='STG_AUTH')
    op.alter_column('user', 'update_ts', existing_type=postgresql.TIMESTAMP(), nullable=True, schema='STG_AUTH')
    op.alter_column('user_group', 'user_id', existing_type=sa.INTEGER(), nullable=True, schema='STG_AUTH')
    op.alter_column('user_group', 'group_id', existing_type=sa.INTEGER(), nullable=True, schema='STG_AUTH')
    op.alter_column('user_group', 'is_deleted', existing_type=sa.BOOLEAN(), nullable=True, schema='STG_AUTH')
    op.alter_column(
        'user_message_delay', 'delay_time', existing_type=postgresql.TIMESTAMP(), nullable=True, schema='STG_AUTH'
    )
    op.alter_column('user_message_delay', 'user_email', existing_type=sa.VARCHAR(), nullable=True, schema='STG_AUTH')
    op.alter_column('user_message_delay', 'user_ip', existing_type=sa.VARCHAR(), nullable=True, schema='STG_AUTH')
    op.alter_column('user_session', 'session_name', existing_type=sa.VARCHAR(), nullable=True, schema='STG_AUTH')
    op.alter_column('user_session', 'user_id', existing_type=sa.INTEGER(), nullable=True, schema='STG_AUTH')
    op.alter_column('user_session', 'expires', existing_type=postgresql.TIMESTAMP(), nullable=True, schema='STG_AUTH')
    op.alter_column('user_session', 'token', existing_type=sa.VARCHAR(), nullable=True, schema='STG_AUTH')
    op.alter_column(
        'user_session', 'last_activity', existing_type=postgresql.TIMESTAMP(), nullable=True, schema='STG_AUTH'
    )
    op.alter_column('user_session', 'create_ts', existing_type=postgresql.TIMESTAMP(), nullable=True, schema='STG_AUTH')
    op.alter_column(
        'user_session_scope', 'user_session_id', existing_type=sa.INTEGER(), nullable=True, schema='STG_AUTH'
    )
    op.alter_column('user_session_scope', 'scope_id', existing_type=sa.INTEGER(), nullable=True, schema='STG_AUTH')
    op.alter_column('user_session_scope', 'is_deleted', existing_type=sa.BOOLEAN(), nullable=True, schema='STG_AUTH')
    op.alter_column(
        'contacts',
        'upload_ts',
        existing_type=postgresql.TIMESTAMP(),
        nullable=True,
        existing_server_default=sa.text('now()'),
        schema='STG_PHYSICS',
    )
    op.alter_column(
        'alert',
        'data',
        existing_type=postgresql.JSON(astext_type=sa.Text()),
        type_=sa.String(),
        existing_nullable=True,
        schema='STG_PINGER',
    )
    op.alter_column('fetcher', 'type', existing_type=sa.VARCHAR(), nullable=True, schema='STG_PINGER')
    op.alter_column('fetcher', 'address', existing_type=sa.VARCHAR(), nullable=True, schema='STG_PINGER')
    op.alter_column('fetcher', 'fetch_data', existing_type=sa.VARCHAR(), nullable=True, schema='STG_PINGER')
    op.alter_column('fetcher', 'delay_ok', existing_type=sa.INTEGER(), nullable=True, schema='STG_PINGER')
    op.alter_column('fetcher', 'delay_fail', existing_type=sa.INTEGER(), nullable=True, schema='STG_PINGER')
    op.alter_column('fetcher', 'create_ts', existing_type=postgresql.TIMESTAMP(), nullable=True, schema='STG_PINGER')
    op.alter_column('metric', 'name', existing_type=sa.VARCHAR(), nullable=True, schema='STG_PINGER')
    op.alter_column('metric', 'ok', existing_type=sa.BOOLEAN(), nullable=True, schema='STG_PINGER')
    op.alter_column(
        'metric', 'time_delta', existing_type=sa.DOUBLE_PRECISION(precision=53), nullable=True, schema='STG_PINGER'
    )
    op.alter_column('receiver', 'url', existing_type=sa.VARCHAR(), nullable=True, schema='STG_PINGER')
    op.alter_column('receiver', 'method', existing_type=sa.VARCHAR(), nullable=True, schema='STG_PINGER')
    op.alter_column(
        'receiver',
        'receiver_body',
        existing_type=postgresql.JSON(astext_type=sa.Text()),
        type_=sa.String(),
        nullable=True,
        schema='STG_PINGER',
    )
    op.alter_column('receiver', 'create_ts', existing_type=postgresql.TIMESTAMP(), nullable=True, schema='STG_PINGER')
    op.alter_column('tg_user', 'surname', existing_type=sa.VARCHAR(), nullable=True, schema='STG_PRINT')
    op.alter_column('tg_user', 'number', existing_type=sa.VARCHAR(), nullable=True, schema='STG_PRINT')
    op.alter_column('union_member', 'surname', existing_type=sa.VARCHAR(), nullable=True, schema='STG_PRINT')
    op.alter_column('union_member', 'union_number', existing_type=sa.VARCHAR(), nullable=True, schema='STG_PRINT')
    op.alter_column('union_member', 'student_number', existing_type=sa.VARCHAR(), nullable=True, schema='STG_PRINT')
    op.alter_column('vk_user', 'surname', existing_type=sa.VARCHAR(), nullable=True, schema='STG_PRINT')
    op.alter_column('vk_user', 'number', existing_type=sa.VARCHAR(), nullable=True, schema='STG_PRINT')
    op.alter_column('button', 'name', existing_type=sa.VARCHAR(), nullable=True, schema='STG_SERVICES')
    op.alter_column('button', 'order', existing_type=sa.INTEGER(), nullable=True, schema='STG_SERVICES')
    op.alter_column('button', 'category_id', existing_type=sa.INTEGER(), nullable=True, schema='STG_SERVICES')
    op.alter_column('button', 'icon', existing_type=sa.VARCHAR(), nullable=True, schema='STG_SERVICES')
    op.alter_column('button', 'link', existing_type=sa.VARCHAR(), nullable=True, schema='STG_SERVICES')
    op.alter_column('button', 'type', existing_type=sa.VARCHAR(), nullable=True, schema='STG_SERVICES')
    op.alter_column('category', 'order', existing_type=sa.INTEGER(), nullable=True, schema='STG_SERVICES')
    op.alter_column('category', 'name', existing_type=sa.VARCHAR(), nullable=True, schema='STG_SERVICES')
    op.alter_column('category', 'type', existing_type=sa.VARCHAR(), nullable=True, schema='STG_SERVICES')
    op.add_column('scope', sa.Column('button_id', sa.Integer(), nullable=True), schema='STG_SERVICES')
    op.add_column('scope', sa.Column('is_required', sa.Boolean(), nullable=True), schema='STG_SERVICES')
    op.alter_column('scope', 'name', existing_type=sa.VARCHAR(), nullable=True, schema='STG_SERVICES')
    op.alter_column('scope', 'category_id', existing_type=sa.INTEGER(), nullable=True, schema='STG_SERVICES')
    op.add_column('webhook_storage', sa.Column('event_ts', sa.DateTime(), nullable=True), schema='STG_SOCIAL')
    op.alter_column('webhook_storage', 'system', existing_type=sa.VARCHAR(), nullable=True, schema='STG_SOCIAL')
    op.alter_column(
        'webhook_storage',
        'message',
        existing_type=postgresql.JSON(astext_type=sa.Text()),
        type_=sa.String(),
        nullable=True,
        schema='STG_SOCIAL',
    )
    op.alter_column('comment_event', 'event_id', existing_type=sa.INTEGER(), nullable=True, schema='STG_TIMETABLE')
    op.alter_column('comment_event', 'author_name', existing_type=sa.VARCHAR(), nullable=True, schema='STG_TIMETABLE')
    op.alter_column('comment_event', 'text', existing_type=sa.VARCHAR(), nullable=True, schema='STG_TIMETABLE')
    op.alter_column(
        'comment_event', 'approve_status', existing_type=sa.VARCHAR(), nullable=True, schema='STG_TIMETABLE'
    )
    op.alter_column(
        'comment_event', 'create_ts', existing_type=postgresql.TIMESTAMP(), nullable=True, schema='STG_TIMETABLE'
    )
    op.alter_column(
        'comment_event', 'update_ts', existing_type=postgresql.TIMESTAMP(), nullable=True, schema='STG_TIMETABLE'
    )
    op.alter_column('comment_event', 'is_deleted', existing_type=sa.BOOLEAN(), nullable=True, schema='STG_TIMETABLE')
    op.alter_column(
        'comment_lecturer', 'lecturer_id', existing_type=sa.INTEGER(), nullable=True, schema='STG_TIMETABLE'
    )
    op.alter_column(
        'comment_lecturer', 'author_name', existing_type=sa.VARCHAR(), nullable=True, schema='STG_TIMETABLE'
    )
    op.alter_column('comment_lecturer', 'text', existing_type=sa.VARCHAR(), nullable=True, schema='STG_TIMETABLE')
    op.alter_column(
        'comment_lecturer', 'approve_status', existing_type=sa.VARCHAR(), nullable=True, schema='STG_TIMETABLE'
    )
    op.alter_column(
        'comment_lecturer', 'create_ts', existing_type=postgresql.TIMESTAMP(), nullable=True, schema='STG_TIMETABLE'
    )
    op.alter_column(
        'comment_lecturer', 'update_ts', existing_type=postgresql.TIMESTAMP(), nullable=True, schema='STG_TIMETABLE'
    )
    op.alter_column('comment_lecturer', 'is_deleted', existing_type=sa.BOOLEAN(), nullable=True, schema='STG_TIMETABLE')
    op.alter_column('credentials', 'group', existing_type=sa.VARCHAR(), nullable=True, schema='STG_TIMETABLE')
    op.alter_column('credentials', 'email', existing_type=sa.VARCHAR(), nullable=True, schema='STG_TIMETABLE')
    op.alter_column(
        'credentials',
        'scope',
        existing_type=postgresql.JSON(astext_type=sa.Text()),
        type_=sa.String(),
        nullable=True,
        schema='STG_TIMETABLE',
    )
    op.alter_column(
        'credentials',
        'token',
        existing_type=postgresql.JSON(astext_type=sa.Text()),
        type_=sa.String(),
        nullable=True,
        schema='STG_TIMETABLE',
    )
    op.alter_column(
        'credentials', 'create_ts', existing_type=postgresql.TIMESTAMP(), nullable=True, schema='STG_TIMETABLE'
    )
    op.alter_column(
        'credentials', 'update_ts', existing_type=postgresql.TIMESTAMP(), nullable=True, schema='STG_TIMETABLE'
    )
    op.alter_column('event', 'name', existing_type=sa.VARCHAR(), nullable=True, schema='STG_TIMETABLE')
    op.alter_column('event', 'start_ts', existing_type=postgresql.TIMESTAMP(), nullable=True, schema='STG_TIMETABLE')
    op.alter_column('event', 'end_ts', existing_type=postgresql.TIMESTAMP(), nullable=True, schema='STG_TIMETABLE')
    op.alter_column('event', 'is_deleted', existing_type=sa.BOOLEAN(), nullable=True, schema='STG_TIMETABLE')
    op.alter_column('events_groups', 'event_id', existing_type=sa.INTEGER(), nullable=True, schema='STG_TIMETABLE')
    op.alter_column('events_groups', 'group_id', existing_type=sa.INTEGER(), nullable=True, schema='STG_TIMETABLE')
    op.alter_column('events_lecturers', 'event_id', existing_type=sa.INTEGER(), nullable=True, schema='STG_TIMETABLE')
    op.alter_column(
        'events_lecturers', 'lecturer_id', existing_type=sa.INTEGER(), nullable=True, schema='STG_TIMETABLE'
    )
    op.alter_column('events_rooms', 'event_id', existing_type=sa.INTEGER(), nullable=True, schema='STG_TIMETABLE')
    op.alter_column('events_rooms', 'room_id', existing_type=sa.INTEGER(), nullable=True, schema='STG_TIMETABLE')
    op.alter_column('group', 'name', existing_type=sa.VARCHAR(), nullable=True, schema='STG_TIMETABLE')
    op.alter_column('group', 'number', existing_type=sa.VARCHAR(), nullable=True, schema='STG_TIMETABLE')
    op.alter_column('group', 'is_deleted', existing_type=sa.BOOLEAN(), nullable=True, schema='STG_TIMETABLE')
    op.alter_column('lecturer', 'first_name', existing_type=sa.VARCHAR(), nullable=True, schema='STG_TIMETABLE')
    op.alter_column('lecturer', 'middle_name', existing_type=sa.VARCHAR(), nullable=True, schema='STG_TIMETABLE')
    op.alter_column('lecturer', 'last_name', existing_type=sa.VARCHAR(), nullable=True, schema='STG_TIMETABLE')
    op.alter_column('lecturer', 'avatar_id', existing_type=sa.INTEGER(), nullable=True, schema='STG_TIMETABLE')
    op.alter_column(
        'lecturer', 'description', existing_type=sa.TEXT(), type_=sa.String(), nullable=True, schema='STG_TIMETABLE'
    )
    op.alter_column('lecturer', 'is_deleted', existing_type=sa.BOOLEAN(), nullable=True, schema='STG_TIMETABLE')
    op.alter_column('photo', 'lecturer_id', existing_type=sa.INTEGER(), nullable=True, schema='STG_TIMETABLE')
    op.alter_column('photo', 'link', existing_type=sa.VARCHAR(), nullable=True, schema='STG_TIMETABLE')
    op.alter_column('photo', 'approve_status', existing_type=sa.VARCHAR(), nullable=True, schema='STG_TIMETABLE')
    op.alter_column('photo', 'is_deleted', existing_type=sa.BOOLEAN(), nullable=True, schema='STG_TIMETABLE')
    op.alter_column('room', 'name', existing_type=sa.VARCHAR(), nullable=True, schema='STG_TIMETABLE')
    op.alter_column('room', 'direction', existing_type=sa.VARCHAR(), nullable=True, schema='STG_TIMETABLE')
    op.alter_column('room', 'building', existing_type=sa.VARCHAR(), nullable=True, schema='STG_TIMETABLE')
    op.alter_column('room', 'building_url', existing_type=sa.VARCHAR(), nullable=True, schema='STG_TIMETABLE')
    op.alter_column('room', 'is_deleted', existing_type=sa.BOOLEAN(), nullable=True, schema='STG_TIMETABLE')
    op.alter_column(
        'union_member', 'type_of_learning', existing_type=sa.VARCHAR(), nullable=True, schema='STG_UNION_MEMBER'
    )
    op.alter_column('union_member', 'rzd_status', existing_type=sa.VARCHAR(), nullable=True, schema='STG_UNION_MEMBER')
    op.alter_column(
        'union_member', 'academic_level', existing_type=sa.VARCHAR(), nullable=True, schema='STG_UNION_MEMBER'
    )
    op.alter_column('union_member', 'status', existing_type=sa.VARCHAR(), nullable=True, schema='STG_UNION_MEMBER')
    op.alter_column('union_member', 'faculty', existing_type=sa.VARCHAR(), nullable=True, schema='STG_UNION_MEMBER')
    op.alter_column('union_member', 'first_name', existing_type=sa.VARCHAR(), nullable=True, schema='STG_UNION_MEMBER')
    op.alter_column('union_member', 'last_name', existing_type=sa.VARCHAR(), nullable=True, schema='STG_UNION_MEMBER')
    op.alter_column('union_member', 'email', existing_type=sa.VARCHAR(), nullable=True, schema='STG_UNION_MEMBER')
    op.alter_column(
        'union_member', 'date_of_birth', existing_type=sa.VARCHAR(), nullable=True, schema='STG_UNION_MEMBER'
    )
    op.alter_column(
        'union_member', 'phone_number', existing_type=sa.VARCHAR(), nullable=True, schema='STG_UNION_MEMBER'
    )
    op.alter_column('union_member', 'image', existing_type=sa.VARCHAR(), nullable=True, schema='STG_UNION_MEMBER')
    op.alter_column(
        'union_member', 'rzd_datetime', existing_type=sa.VARCHAR(), nullable=True, schema='STG_UNION_MEMBER'
    )
    op.alter_column('union_member', 'rzd_number', existing_type=sa.VARCHAR(), nullable=True, schema='STG_UNION_MEMBER')
    op.alter_column('union_member', 'grade_level', existing_type=sa.INTEGER(), nullable=True, schema='STG_UNION_MEMBER')
    op.alter_column(
        'union_member', 'has_student_id', existing_type=sa.BOOLEAN(), nullable=True, schema='STG_UNION_MEMBER'
    )
    op.alter_column('union_member', 'entry_date', existing_type=sa.VARCHAR(), nullable=True, schema='STG_UNION_MEMBER')
    op.alter_column(
        'union_member', 'status_gain_date', existing_type=sa.VARCHAR(), nullable=True, schema='STG_UNION_MEMBER'
    )
    op.alter_column('union_member', 'card_id', existing_type=sa.INTEGER(), nullable=True, schema='STG_UNION_MEMBER')
    op.alter_column('union_member', 'card_status', existing_type=sa.VARCHAR(), nullable=True, schema='STG_UNION_MEMBER')
    op.alter_column('union_member', 'card_date', existing_type=sa.VARCHAR(), nullable=True, schema='STG_UNION_MEMBER')
    op.alter_column('union_member', 'card_number', existing_type=sa.VARCHAR(), nullable=True, schema='STG_UNION_MEMBER')
    op.alter_column('union_member', 'card', existing_type=sa.VARCHAR(), nullable=True, schema='STG_UNION_MEMBER')
    op.alter_column('category', 'name', existing_type=sa.VARCHAR(), nullable=True, schema='STG_USERDATA')
    op.alter_column('category', 'read_scope', existing_type=sa.VARCHAR(), nullable=True, schema='STG_USERDATA')
    op.alter_column('category', 'update_scope', existing_type=sa.VARCHAR(), nullable=True, schema='STG_USERDATA')
    op.alter_column('category', 'create_ts', existing_type=postgresql.TIMESTAMP(), nullable=True, schema='STG_USERDATA')
    op.alter_column('category', 'modify_ts', existing_type=postgresql.TIMESTAMP(), nullable=True, schema='STG_USERDATA')
    op.alter_column('category', 'is_deleted', existing_type=sa.BOOLEAN(), nullable=True, schema='STG_USERDATA')
    op.alter_column('info', 'param_id', existing_type=sa.INTEGER(), nullable=True, schema='STG_USERDATA')
    op.alter_column('info', 'source_id', existing_type=sa.INTEGER(), nullable=True, schema='STG_USERDATA')
    op.alter_column('info', 'owner_id', existing_type=sa.INTEGER(), nullable=True, schema='STG_USERDATA')
    op.alter_column('info', 'value', existing_type=sa.VARCHAR(), nullable=True, schema='STG_USERDATA')
    op.alter_column('info', 'create_ts', existing_type=postgresql.TIMESTAMP(), nullable=True, schema='STG_USERDATA')
    op.alter_column('info', 'modify_ts', existing_type=postgresql.TIMESTAMP(), nullable=True, schema='STG_USERDATA')
    op.alter_column('info', 'is_deleted', existing_type=sa.BOOLEAN(), nullable=True, schema='STG_USERDATA')
    op.alter_column('param', 'name', existing_type=sa.VARCHAR(), nullable=True, schema='STG_USERDATA')
    op.alter_column('param', 'category_id', existing_type=sa.INTEGER(), nullable=True, schema='STG_USERDATA')
    op.alter_column('param', 'is_required', existing_type=sa.BOOLEAN(), nullable=True, schema='STG_USERDATA')
    op.alter_column('param', 'changeable', existing_type=sa.BOOLEAN(), nullable=True, schema='STG_USERDATA')
    op.alter_column('param', 'type', existing_type=sa.VARCHAR(), nullable=True, schema='STG_USERDATA')
    op.alter_column('param', 'create_ts', existing_type=postgresql.TIMESTAMP(), nullable=True, schema='STG_USERDATA')
    op.alter_column('param', 'modify_ts', existing_type=postgresql.TIMESTAMP(), nullable=True, schema='STG_USERDATA')
    op.alter_column('param', 'is_deleted', existing_type=sa.BOOLEAN(), nullable=True, schema='STG_USERDATA')
    op.alter_column('source', 'name', existing_type=sa.VARCHAR(), nullable=True, schema='STG_USERDATA')
    op.alter_column('source', 'trust_level', existing_type=sa.INTEGER(), nullable=True, schema='STG_USERDATA')
    op.alter_column('source', 'create_ts', existing_type=postgresql.TIMESTAMP(), nullable=True, schema='STG_USERDATA')
    op.alter_column('source', 'modify_ts', existing_type=postgresql.TIMESTAMP(), nullable=True, schema='STG_USERDATA')
    op.alter_column('source', 'is_deleted', existing_type=sa.BOOLEAN(), nullable=True, schema='STG_USERDATA')


def downgrade():
    op.revoke_on_schema(
        "test_dwh_stg_achievement_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_achievement_all",
        "STG_ACHIEVEMENT",
    )
    op.revoke_on_schema(
        (
            "test_dwh_stg_achievement_write"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_achievement_write"
        ),
        "STG_ACHIEVEMENT",
    )
    op.revoke_on_schema(
        (
            "test_dwh_stg_achievement_read"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_achievement_read"
        ),
        "STG_ACHIEVEMENT",
    )
    op.revoke_on_schema(
        "test_dwh_stg_rasphysmsu_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rasphysmsu_all",
        "STG_RASPHYSMSU",
    )
    op.revoke_on_schema(
        (
            "test_dwh_stg_rasphysmsu_write"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_rasphysmsu_write"
        ),
        "STG_RASPHYSMSU",
    )
    op.revoke_on_schema(
        "test_dwh_stg_rasphysmsu_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rasphysmsu_read",
        "STG_RASPHYSMSU",
    )
    op.drop_table('vk_group', schema='STG_SOCIAL')
    op.drop_table('vk_chat', schema='STG_SOCIAL')
    op.drop_table('telegram_chat', schema='STG_SOCIAL')
    op.drop_table('telegram_channel', schema='STG_SOCIAL')
    op.drop_table('group', schema='STG_SOCIAL')
    op.drop_table('create_group_request', schema='STG_SOCIAL')
    op.drop_table('raw_html_old', schema='STG_RASPHYSMSU')
    op.drop_table('raw_html', schema='STG_RASPHYSMSU')
    op.drop_table('dynamic_option', schema='STG_AUTH')
    op.drop_table('achievement_receiver', schema='STG_ACHIEVEMENT')
    op.drop_table('achievement', schema='STG_ACHIEVEMENT')
    op.delete_group(
        "test_dwh_stg_achievement_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_achievement_all"
    )
    op.delete_group(
        "test_dwh_stg_achievement_write"
        if os.getenv("ENVIRONMENT") != "production"
        else "prod_dwh_stg_achievement_write"
    )
    op.delete_group(
        "test_dwh_stg_achievement_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_achievement_read"
    )
    op.delete_group(
        "test_dwh_stg_rasphysmsu_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rasphysmsu_all"
    )
    op.delete_group(
        "test_dwh_stg_rasphysmsu_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rasphysmsu_write"
    )
    op.delete_group(
        "test_dwh_stg_rasphysmsu_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rasphysmsu_read"
    )
    op.drop_table_schema("STG_ACHIEVEMENT")
    op.drop_table_schema("STG_RASPHYSMSU")
    op.create_table(
        'vk_groups',
        sa.Column('id', sa.INTEGER(), nullable=False),
        sa.Column('group_id', sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column('confirmation_token', sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column('secret_key', sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column('create_ts', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
        sa.Column('update_ts', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
        sa.PrimaryKeyConstraint('id', name='vk_groups_pkey'),
        schema='STG_SOCIAL',
    )
    op.grant_on_table(
        "test_dwh_stg_social_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_all",
        ['ALL'],
        '"STG_SOCIAL".vk_groups',
    )
    op.grant_on_table(
        ("test_dwh_stg_social_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_write"),
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_SOCIAL".vk_groups',
    )
    op.grant_on_table(
        ("test_dwh_stg_social_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_read"),
        ['SELECT'],
        '"STG_SOCIAL".vk_groups',
    )
    op.alter_column('source', 'is_deleted', existing_type=sa.BOOLEAN(), nullable=False, schema='STG_USERDATA')
    op.alter_column('source', 'modify_ts', existing_type=postgresql.TIMESTAMP(), nullable=False, schema='STG_USERDATA')
    op.alter_column('source', 'create_ts', existing_type=postgresql.TIMESTAMP(), nullable=False, schema='STG_USERDATA')
    op.alter_column('source', 'trust_level', existing_type=sa.INTEGER(), nullable=False, schema='STG_USERDATA')
    op.alter_column('source', 'name', existing_type=sa.VARCHAR(), nullable=False, schema='STG_USERDATA')
    op.alter_column('param', 'is_deleted', existing_type=sa.BOOLEAN(), nullable=False, schema='STG_USERDATA')
    op.alter_column('param', 'modify_ts', existing_type=postgresql.TIMESTAMP(), nullable=False, schema='STG_USERDATA')
    op.alter_column('param', 'create_ts', existing_type=postgresql.TIMESTAMP(), nullable=False, schema='STG_USERDATA')
    op.alter_column('param', 'type', existing_type=sa.VARCHAR(), nullable=False, schema='STG_USERDATA')
    op.alter_column('param', 'changeable', existing_type=sa.BOOLEAN(), nullable=False, schema='STG_USERDATA')
    op.alter_column('param', 'is_required', existing_type=sa.BOOLEAN(), nullable=False, schema='STG_USERDATA')
    op.alter_column('param', 'category_id', existing_type=sa.INTEGER(), nullable=False, schema='STG_USERDATA')
    op.alter_column('param', 'name', existing_type=sa.VARCHAR(), nullable=False, schema='STG_USERDATA')
    op.alter_column('info', 'is_deleted', existing_type=sa.BOOLEAN(), nullable=False, schema='STG_USERDATA')
    op.alter_column('info', 'modify_ts', existing_type=postgresql.TIMESTAMP(), nullable=False, schema='STG_USERDATA')
    op.alter_column('info', 'create_ts', existing_type=postgresql.TIMESTAMP(), nullable=False, schema='STG_USERDATA')
    op.alter_column('info', 'value', existing_type=sa.VARCHAR(), nullable=False, schema='STG_USERDATA')
    op.alter_column('info', 'owner_id', existing_type=sa.INTEGER(), nullable=False, schema='STG_USERDATA')
    op.alter_column('info', 'source_id', existing_type=sa.INTEGER(), nullable=False, schema='STG_USERDATA')
    op.alter_column('info', 'param_id', existing_type=sa.INTEGER(), nullable=False, schema='STG_USERDATA')
    op.alter_column('category', 'is_deleted', existing_type=sa.BOOLEAN(), nullable=False, schema='STG_USERDATA')
    op.alter_column(
        'category', 'modify_ts', existing_type=postgresql.TIMESTAMP(), nullable=False, schema='STG_USERDATA'
    )
    op.alter_column(
        'category', 'create_ts', existing_type=postgresql.TIMESTAMP(), nullable=False, schema='STG_USERDATA'
    )
    op.alter_column('category', 'update_scope', existing_type=sa.VARCHAR(), nullable=False, schema='STG_USERDATA')
    op.alter_column('category', 'read_scope', existing_type=sa.VARCHAR(), nullable=False, schema='STG_USERDATA')
    op.alter_column('category', 'name', existing_type=sa.VARCHAR(), nullable=False, schema='STG_USERDATA')
    op.alter_column('union_member', 'card', existing_type=sa.VARCHAR(), nullable=False, schema='STG_UNION_MEMBER')
    op.alter_column(
        'union_member', 'card_number', existing_type=sa.VARCHAR(), nullable=False, schema='STG_UNION_MEMBER'
    )
    op.alter_column('union_member', 'card_date', existing_type=sa.VARCHAR(), nullable=False, schema='STG_UNION_MEMBER')
    op.alter_column(
        'union_member', 'card_status', existing_type=sa.VARCHAR(), nullable=False, schema='STG_UNION_MEMBER'
    )
    op.alter_column('union_member', 'card_id', existing_type=sa.INTEGER(), nullable=False, schema='STG_UNION_MEMBER')
    op.alter_column(
        'union_member', 'status_gain_date', existing_type=sa.VARCHAR(), nullable=False, schema='STG_UNION_MEMBER'
    )
    op.alter_column('union_member', 'entry_date', existing_type=sa.VARCHAR(), nullable=False, schema='STG_UNION_MEMBER')
    op.alter_column(
        'union_member', 'has_student_id', existing_type=sa.BOOLEAN(), nullable=False, schema='STG_UNION_MEMBER'
    )
    op.alter_column(
        'union_member', 'grade_level', existing_type=sa.INTEGER(), nullable=False, schema='STG_UNION_MEMBER'
    )
    op.alter_column('union_member', 'rzd_number', existing_type=sa.VARCHAR(), nullable=False, schema='STG_UNION_MEMBER')
    op.alter_column(
        'union_member', 'rzd_datetime', existing_type=sa.VARCHAR(), nullable=False, schema='STG_UNION_MEMBER'
    )
    op.alter_column('union_member', 'image', existing_type=sa.VARCHAR(), nullable=False, schema='STG_UNION_MEMBER')
    op.alter_column(
        'union_member', 'phone_number', existing_type=sa.VARCHAR(), nullable=False, schema='STG_UNION_MEMBER'
    )
    op.alter_column(
        'union_member', 'date_of_birth', existing_type=sa.VARCHAR(), nullable=False, schema='STG_UNION_MEMBER'
    )
    op.alter_column('union_member', 'email', existing_type=sa.VARCHAR(), nullable=False, schema='STG_UNION_MEMBER')
    op.alter_column('union_member', 'last_name', existing_type=sa.VARCHAR(), nullable=False, schema='STG_UNION_MEMBER')
    op.alter_column('union_member', 'first_name', existing_type=sa.VARCHAR(), nullable=False, schema='STG_UNION_MEMBER')
    op.alter_column('union_member', 'faculty', existing_type=sa.VARCHAR(), nullable=False, schema='STG_UNION_MEMBER')
    op.alter_column('union_member', 'status', existing_type=sa.VARCHAR(), nullable=False, schema='STG_UNION_MEMBER')
    op.alter_column(
        'union_member', 'academic_level', existing_type=sa.VARCHAR(), nullable=False, schema='STG_UNION_MEMBER'
    )
    op.alter_column('union_member', 'rzd_status', existing_type=sa.VARCHAR(), nullable=False, schema='STG_UNION_MEMBER')
    op.alter_column(
        'union_member', 'type_of_learning', existing_type=sa.VARCHAR(), nullable=False, schema='STG_UNION_MEMBER'
    )
    op.alter_column('room', 'is_deleted', existing_type=sa.BOOLEAN(), nullable=False, schema='STG_TIMETABLE')
    op.alter_column('room', 'building_url', existing_type=sa.VARCHAR(), nullable=False, schema='STG_TIMETABLE')
    op.alter_column('room', 'building', existing_type=sa.VARCHAR(), nullable=False, schema='STG_TIMETABLE')
    op.alter_column('room', 'direction', existing_type=sa.VARCHAR(), nullable=False, schema='STG_TIMETABLE')
    op.alter_column('room', 'name', existing_type=sa.VARCHAR(), nullable=False, schema='STG_TIMETABLE')
    op.alter_column('photo', 'is_deleted', existing_type=sa.BOOLEAN(), nullable=False, schema='STG_TIMETABLE')
    op.alter_column('photo', 'approve_status', existing_type=sa.VARCHAR(), nullable=False, schema='STG_TIMETABLE')
    op.alter_column('photo', 'link', existing_type=sa.VARCHAR(), nullable=False, schema='STG_TIMETABLE')
    op.alter_column('photo', 'lecturer_id', existing_type=sa.INTEGER(), nullable=False, schema='STG_TIMETABLE')
    op.alter_column('lecturer', 'is_deleted', existing_type=sa.BOOLEAN(), nullable=False, schema='STG_TIMETABLE')
    op.alter_column(
        'lecturer', 'description', existing_type=sa.String(), type_=sa.TEXT(), nullable=False, schema='STG_TIMETABLE'
    )
    op.alter_column('lecturer', 'avatar_id', existing_type=sa.INTEGER(), nullable=False, schema='STG_TIMETABLE')
    op.alter_column('lecturer', 'last_name', existing_type=sa.VARCHAR(), nullable=False, schema='STG_TIMETABLE')
    op.alter_column('lecturer', 'middle_name', existing_type=sa.VARCHAR(), nullable=False, schema='STG_TIMETABLE')
    op.alter_column('lecturer', 'first_name', existing_type=sa.VARCHAR(), nullable=False, schema='STG_TIMETABLE')
    op.alter_column('group', 'is_deleted', existing_type=sa.BOOLEAN(), nullable=False, schema='STG_TIMETABLE')
    op.alter_column('group', 'number', existing_type=sa.VARCHAR(), nullable=False, schema='STG_TIMETABLE')
    op.alter_column('group', 'name', existing_type=sa.VARCHAR(), nullable=False, schema='STG_TIMETABLE')
    op.alter_column('events_rooms', 'room_id', existing_type=sa.INTEGER(), nullable=False, schema='STG_TIMETABLE')
    op.alter_column('events_rooms', 'event_id', existing_type=sa.INTEGER(), nullable=False, schema='STG_TIMETABLE')
    op.alter_column(
        'events_lecturers', 'lecturer_id', existing_type=sa.INTEGER(), nullable=False, schema='STG_TIMETABLE'
    )
    op.alter_column('events_lecturers', 'event_id', existing_type=sa.INTEGER(), nullable=False, schema='STG_TIMETABLE')
    op.alter_column('events_groups', 'group_id', existing_type=sa.INTEGER(), nullable=False, schema='STG_TIMETABLE')
    op.alter_column('events_groups', 'event_id', existing_type=sa.INTEGER(), nullable=False, schema='STG_TIMETABLE')
    op.alter_column('event', 'is_deleted', existing_type=sa.BOOLEAN(), nullable=False, schema='STG_TIMETABLE')
    op.alter_column('event', 'end_ts', existing_type=postgresql.TIMESTAMP(), nullable=False, schema='STG_TIMETABLE')
    op.alter_column('event', 'start_ts', existing_type=postgresql.TIMESTAMP(), nullable=False, schema='STG_TIMETABLE')
    op.alter_column('event', 'name', existing_type=sa.VARCHAR(), nullable=False, schema='STG_TIMETABLE')
    op.alter_column(
        'credentials', 'update_ts', existing_type=postgresql.TIMESTAMP(), nullable=False, schema='STG_TIMETABLE'
    )
    op.alter_column(
        'credentials', 'create_ts', existing_type=postgresql.TIMESTAMP(), nullable=False, schema='STG_TIMETABLE'
    )
    op.alter_column(
        'credentials',
        'token',
        existing_type=sa.String(),
        postgresql_using="token::json",
        type_=postgresql.JSON(astext_type=sa.Text()),
        nullable=False,
        schema='STG_TIMETABLE',
    )
    op.alter_column(
        'credentials',
        'scope',
        existing_type=sa.String(),
        postgresql_using="scope::json",
        type_=postgresql.JSON(astext_type=sa.Text()),
        nullable=False,
        schema='STG_TIMETABLE',
    )
    op.alter_column('credentials', 'email', existing_type=sa.VARCHAR(), nullable=False, schema='STG_TIMETABLE')
    op.alter_column('credentials', 'group', existing_type=sa.VARCHAR(), nullable=False, schema='STG_TIMETABLE')
    op.alter_column(
        'comment_lecturer', 'is_deleted', existing_type=sa.BOOLEAN(), nullable=False, schema='STG_TIMETABLE'
    )
    op.alter_column(
        'comment_lecturer', 'update_ts', existing_type=postgresql.TIMESTAMP(), nullable=False, schema='STG_TIMETABLE'
    )
    op.alter_column(
        'comment_lecturer', 'create_ts', existing_type=postgresql.TIMESTAMP(), nullable=False, schema='STG_TIMETABLE'
    )
    op.alter_column(
        'comment_lecturer', 'approve_status', existing_type=sa.VARCHAR(), nullable=False, schema='STG_TIMETABLE'
    )
    op.alter_column('comment_lecturer', 'text', existing_type=sa.VARCHAR(), nullable=False, schema='STG_TIMETABLE')
    op.alter_column(
        'comment_lecturer', 'author_name', existing_type=sa.VARCHAR(), nullable=False, schema='STG_TIMETABLE'
    )
    op.alter_column(
        'comment_lecturer', 'lecturer_id', existing_type=sa.INTEGER(), nullable=False, schema='STG_TIMETABLE'
    )
    op.alter_column('comment_event', 'is_deleted', existing_type=sa.BOOLEAN(), nullable=False, schema='STG_TIMETABLE')
    op.alter_column(
        'comment_event', 'update_ts', existing_type=postgresql.TIMESTAMP(), nullable=False, schema='STG_TIMETABLE'
    )
    op.alter_column(
        'comment_event', 'create_ts', existing_type=postgresql.TIMESTAMP(), nullable=False, schema='STG_TIMETABLE'
    )
    op.alter_column(
        'comment_event', 'approve_status', existing_type=sa.VARCHAR(), nullable=False, schema='STG_TIMETABLE'
    )
    op.alter_column('comment_event', 'text', existing_type=sa.VARCHAR(), nullable=False, schema='STG_TIMETABLE')
    op.alter_column('comment_event', 'author_name', existing_type=sa.VARCHAR(), nullable=False, schema='STG_TIMETABLE')
    op.alter_column('comment_event', 'event_id', existing_type=sa.INTEGER(), nullable=False, schema='STG_TIMETABLE')
    op.alter_column(
        'webhook_storage',
        'message',
        existing_type=sa.String(),
        postgresql_using="message::json",
        type_=postgresql.JSON(astext_type=sa.Text()),
        nullable=False,
        schema='STG_SOCIAL',
    )
    op.alter_column('webhook_storage', 'system', existing_type=sa.VARCHAR(), nullable=False, schema='STG_SOCIAL')
    op.drop_column('webhook_storage', 'event_ts', schema='STG_SOCIAL')
    op.alter_column('scope', 'category_id', existing_type=sa.INTEGER(), nullable=False, schema='STG_SERVICES')
    op.alter_column('scope', 'name', existing_type=sa.VARCHAR(), nullable=False, schema='STG_SERVICES')
    op.drop_column('scope', 'is_required', schema='STG_SERVICES')
    op.drop_column('scope', 'button_id', schema='STG_SERVICES')
    op.alter_column('category', 'type', existing_type=sa.VARCHAR(), nullable=False, schema='STG_SERVICES')
    op.alter_column('category', 'name', existing_type=sa.VARCHAR(), nullable=False, schema='STG_SERVICES')
    op.alter_column('category', 'order', existing_type=sa.INTEGER(), nullable=False, schema='STG_SERVICES')
    op.alter_column('button', 'type', existing_type=sa.VARCHAR(), nullable=False, schema='STG_SERVICES')
    op.alter_column('button', 'link', existing_type=sa.VARCHAR(), nullable=False, schema='STG_SERVICES')
    op.alter_column('button', 'icon', existing_type=sa.VARCHAR(), nullable=False, schema='STG_SERVICES')
    op.alter_column('button', 'category_id', existing_type=sa.INTEGER(), nullable=False, schema='STG_SERVICES')
    op.alter_column('button', 'order', existing_type=sa.INTEGER(), nullable=False, schema='STG_SERVICES')
    op.alter_column('button', 'name', existing_type=sa.VARCHAR(), nullable=False, schema='STG_SERVICES')
    op.alter_column('vk_user', 'number', existing_type=sa.VARCHAR(), nullable=False, schema='STG_PRINT')
    op.alter_column('vk_user', 'surname', existing_type=sa.VARCHAR(), nullable=False, schema='STG_PRINT')
    op.alter_column('union_member', 'student_number', existing_type=sa.VARCHAR(), nullable=False, schema='STG_PRINT')
    op.alter_column('union_member', 'union_number', existing_type=sa.VARCHAR(), nullable=False, schema='STG_PRINT')
    op.alter_column('union_member', 'surname', existing_type=sa.VARCHAR(), nullable=False, schema='STG_PRINT')
    op.alter_column('tg_user', 'number', existing_type=sa.VARCHAR(), nullable=False, schema='STG_PRINT')
    op.alter_column('tg_user', 'surname', existing_type=sa.VARCHAR(), nullable=False, schema='STG_PRINT')
    op.alter_column('receiver', 'create_ts', existing_type=postgresql.TIMESTAMP(), nullable=False, schema='STG_PINGER')
    op.alter_column(
        'receiver',
        'receiver_body',
        existing_type=sa.String(),
        postgresql_using="receiver_body::json",
        type_=postgresql.JSON(astext_type=sa.Text()),
        nullable=False,
        schema='STG_PINGER',
    )
    op.alter_column('receiver', 'method', existing_type=sa.VARCHAR(), nullable=False, schema='STG_PINGER')
    op.alter_column('receiver', 'url', existing_type=sa.VARCHAR(), nullable=False, schema='STG_PINGER')
    op.alter_column(
        'metric', 'time_delta', existing_type=sa.DOUBLE_PRECISION(precision=53), nullable=False, schema='STG_PINGER'
    )
    op.alter_column('metric', 'ok', existing_type=sa.BOOLEAN(), nullable=False, schema='STG_PINGER')
    op.alter_column('metric', 'name', existing_type=sa.VARCHAR(), nullable=False, schema='STG_PINGER')
    op.alter_column('fetcher', 'create_ts', existing_type=postgresql.TIMESTAMP(), nullable=False, schema='STG_PINGER')
    op.alter_column('fetcher', 'delay_fail', existing_type=sa.INTEGER(), nullable=False, schema='STG_PINGER')
    op.alter_column('fetcher', 'delay_ok', existing_type=sa.INTEGER(), nullable=False, schema='STG_PINGER')
    op.alter_column('fetcher', 'fetch_data', existing_type=sa.VARCHAR(), nullable=False, schema='STG_PINGER')
    op.alter_column('fetcher', 'address', existing_type=sa.VARCHAR(), nullable=False, schema='STG_PINGER')
    op.alter_column('fetcher', 'type', existing_type=sa.VARCHAR(), nullable=False, schema='STG_PINGER')
    op.alter_column(
        'alert',
        'data',
        existing_type=sa.String(),
        postgresql_using="data::json",
        type_=postgresql.JSON(astext_type=sa.Text()),
        existing_nullable=True,
        schema='STG_PINGER',
    )
    op.alter_column(
        'contacts',
        'upload_ts',
        existing_type=postgresql.TIMESTAMP(),
        nullable=False,
        existing_server_default=sa.text('now()'),
        schema='STG_PHYSICS',
    )
    op.alter_column('user_session_scope', 'is_deleted', existing_type=sa.BOOLEAN(), nullable=False, schema='STG_AUTH')
    op.alter_column('user_session_scope', 'scope_id', existing_type=sa.INTEGER(), nullable=False, schema='STG_AUTH')
    op.alter_column(
        'user_session_scope', 'user_session_id', existing_type=sa.INTEGER(), nullable=False, schema='STG_AUTH'
    )
    op.alter_column(
        'user_session', 'create_ts', existing_type=postgresql.TIMESTAMP(), nullable=False, schema='STG_AUTH'
    )
    op.alter_column(
        'user_session', 'last_activity', existing_type=postgresql.TIMESTAMP(), nullable=False, schema='STG_AUTH'
    )
    op.alter_column('user_session', 'token', existing_type=sa.VARCHAR(), nullable=False, schema='STG_AUTH')
    op.alter_column('user_session', 'expires', existing_type=postgresql.TIMESTAMP(), nullable=False, schema='STG_AUTH')
    op.alter_column('user_session', 'user_id', existing_type=sa.INTEGER(), nullable=False, schema='STG_AUTH')
    op.alter_column('user_session', 'session_name', existing_type=sa.VARCHAR(), nullable=False, schema='STG_AUTH')
    op.alter_column('user_message_delay', 'user_ip', existing_type=sa.VARCHAR(), nullable=False, schema='STG_AUTH')
    op.alter_column('user_message_delay', 'user_email', existing_type=sa.VARCHAR(), nullable=False, schema='STG_AUTH')
    op.alter_column(
        'user_message_delay', 'delay_time', existing_type=postgresql.TIMESTAMP(), nullable=False, schema='STG_AUTH'
    )
    op.alter_column('user_group', 'is_deleted', existing_type=sa.BOOLEAN(), nullable=False, schema='STG_AUTH')
    op.alter_column('user_group', 'group_id', existing_type=sa.INTEGER(), nullable=False, schema='STG_AUTH')
    op.alter_column('user_group', 'user_id', existing_type=sa.INTEGER(), nullable=False, schema='STG_AUTH')
    op.alter_column('user', 'update_ts', existing_type=postgresql.TIMESTAMP(), nullable=False, schema='STG_AUTH')
    op.alter_column('user', 'create_ts', existing_type=postgresql.TIMESTAMP(), nullable=False, schema='STG_AUTH')
    op.alter_column('user', 'is_deleted', existing_type=sa.BOOLEAN(), nullable=False, schema='STG_AUTH')
    op.alter_column('scope', 'is_deleted', existing_type=sa.BOOLEAN(), nullable=False, schema='STG_AUTH')
    op.alter_column('scope', 'comment', existing_type=sa.VARCHAR(), nullable=False, schema='STG_AUTH')
    op.alter_column('scope', 'name', existing_type=sa.VARCHAR(), nullable=False, schema='STG_AUTH')
    op.alter_column('scope', 'creator_id', existing_type=sa.INTEGER(), nullable=False, schema='STG_AUTH')
    op.alter_column('group_scope', 'is_deleted', existing_type=sa.BOOLEAN(), nullable=False, schema='STG_AUTH')
    op.alter_column('group_scope', 'scope_id', existing_type=sa.INTEGER(), nullable=False, schema='STG_AUTH')
    op.alter_column('group_scope', 'group_id', existing_type=sa.INTEGER(), nullable=False, schema='STG_AUTH')
    op.alter_column('group', 'is_deleted', existing_type=sa.BOOLEAN(), nullable=False, schema='STG_AUTH')
    op.alter_column('group', 'update_ts', existing_type=postgresql.TIMESTAMP(), nullable=False, schema='STG_AUTH')
    op.alter_column('group', 'create_ts', existing_type=postgresql.TIMESTAMP(), nullable=False, schema='STG_AUTH')
    op.alter_column('group', 'parent_id', existing_type=sa.INTEGER(), nullable=False, schema='STG_AUTH')
    op.alter_column('group', 'name', existing_type=sa.VARCHAR(), nullable=False, schema='STG_AUTH')
    op.alter_column('auth_method', 'is_deleted', existing_type=sa.BOOLEAN(), nullable=False, schema='STG_AUTH')
    op.alter_column('auth_method', 'update_ts', existing_type=postgresql.TIMESTAMP(), nullable=False, schema='STG_AUTH')
    op.alter_column('auth_method', 'create_ts', existing_type=postgresql.TIMESTAMP(), nullable=False, schema='STG_AUTH')
    op.alter_column('auth_method', 'value', existing_type=sa.VARCHAR(), nullable=False, schema='STG_AUTH')
    op.alter_column('auth_method', 'param', existing_type=sa.VARCHAR(), nullable=False, schema='STG_AUTH')
    op.alter_column('auth_method', 'auth_method', existing_type=sa.VARCHAR(), nullable=False, schema='STG_AUTH')
    op.alter_column('auth_method', 'user_id', existing_type=sa.INTEGER(), nullable=False, schema='STG_AUTH')
