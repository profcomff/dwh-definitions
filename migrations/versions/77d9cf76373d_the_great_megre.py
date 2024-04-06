"""the_great_megre

Revision ID: 77d9cf76373d
Revises: fa6331fe4c72
Create Date: 2023-09-10 13:18:28.627484

"""

import os

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '77d9cf76373d'
down_revision = 'fa6331fe4c72'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table_schema("STG_TIMETABLE")
    op.create_table_schema("STG_MARKETING")
    op.create_table_schema("STG_SERVICES")
    op.create_table_schema("STG_SOCIAL")
    op.create_table_schema("STG_AUTH")
    op.create_table_schema("STG_PINGER")
    op.create_table_schema("STG_USERDATA")
    op.create_table_schema("STG_PRINT")
    op.create_table(
        'auth_method',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('auth_method', sa.String(), nullable=False),
        sa.Column('param', sa.String(), nullable=False),
        sa.Column('value', sa.String(), nullable=False),
        sa.Column('create_ts', sa.DateTime(), nullable=False),
        sa.Column('update_ts', sa.DateTime(), nullable=False),
        sa.Column('is_deleted', sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_AUTH',
    )
    op.create_table(
        'group',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('parent_id', sa.Integer(), nullable=False),
        sa.Column('create_ts', sa.DateTime(), nullable=False),
        sa.Column('update_ts', sa.DateTime(), nullable=False),
        sa.Column('is_deleted', sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_AUTH',
    )
    op.create_table(
        'group_scope',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('group_id', sa.Integer(), nullable=False),
        sa.Column('scope_id', sa.Integer(), nullable=False),
        sa.Column('is_deleted', sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_AUTH',
    )
    op.create_table(
        'scope',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('creator_id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('comment', sa.String(), nullable=False),
        sa.Column('is_deleted', sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_AUTH',
    )
    op.create_table(
        'user',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('is_deleted', sa.Boolean(), nullable=False),
        sa.Column('create_ts', sa.DateTime(), nullable=False),
        sa.Column('update_ts', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_AUTH',
    )
    op.create_table(
        'user_group',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('group_id', sa.Integer(), nullable=False),
        sa.Column('is_deleted', sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_AUTH',
    )
    op.create_table(
        'user_message_delay',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('delay_time', sa.DateTime(), nullable=False),
        sa.Column('user_email', sa.String(), nullable=False),
        sa.Column('user_ip', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_AUTH',
    )
    op.create_table(
        'user_session',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('session_name', sa.String(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('expires', sa.DateTime(), nullable=False),
        sa.Column('token', sa.String(), nullable=False),
        sa.Column('last_activity', sa.DateTime(), nullable=False),
        sa.Column('create_ts', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_AUTH',
    )
    op.create_table(
        'user_session_scope',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_session_id', sa.Integer(), nullable=False),
        sa.Column('scope_id', sa.Integer(), nullable=False),
        sa.Column('is_deleted', sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_AUTH',
    )
    op.create_table(
        'actions_info',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.Column('action', sa.String(), nullable=True),
        sa.Column('path_from', sa.String(), nullable=True),
        sa.Column('path_to', sa.String(), nullable=True),
        sa.Column('additional_data', sa.String(), nullable=True),
        sa.Column('create_ts', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_MARKETING',
    )
    op.create_table(
        'user',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('union_number', sa.String(), nullable=True),
        sa.Column('user_agent', sa.String(), nullable=True),
        sa.Column('auth_user_id', sa.Integer(), nullable=True),
        sa.Column('modify_ts', sa.DateTime(), nullable=True),
        sa.Column('create_ts', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_MARKETING',
    )
    op.create_table(
        'alert',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('data', sa.JSON(), nullable=True),
        sa.Column('filter', sa.String(), nullable=True),
        sa.Column('create_ts', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_PINGER',
    )
    op.create_table(
        'fetcher',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('type', sa.String(), nullable=False),
        sa.Column('address', sa.String(), nullable=False),
        sa.Column('fetch_data', sa.String(), nullable=False),
        sa.Column('delay_ok', sa.Integer(), nullable=False),
        sa.Column('delay_fail', sa.Integer(), nullable=False),
        sa.Column('create_ts', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_PINGER',
    )
    op.create_table(
        'metric',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('ok', sa.Boolean(), nullable=False),
        sa.Column('time_delta', sa.Float(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_PINGER',
    )
    op.create_table(
        'receiver',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('url', sa.String(), nullable=False),
        sa.Column('method', sa.String(), nullable=False),
        sa.Column('receiver_body', sa.JSON(), nullable=False),
        sa.Column('create_ts', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_PINGER',
    )
    op.create_table(
        'file',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('pin', sa.String(), nullable=True),
        sa.Column('file', sa.String(), nullable=True),
        sa.Column('owner_id', sa.Integer(), nullable=True),
        sa.Column('option_pages', sa.String(), nullable=True),
        sa.Column('option_copies', sa.Integer(), nullable=True),
        sa.Column('option_two_sided', sa.Boolean(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('number_of_pages', sa.Integer(), nullable=True),
        sa.Column('source', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_PRINT',
    )
    op.create_table(
        'print_fact',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('file_id', sa.Integer(), nullable=True),
        sa.Column('owner_id', sa.Integer(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('sheets_used', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_PRINT',
    )
    op.create_table(
        'tg_user',
        sa.Column('tg_id', sa.BIGINT(), nullable=False),
        sa.Column('surname', sa.String(), nullable=False),
        sa.Column('number', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('tg_id'),
        schema='STG_PRINT',
    )
    op.create_table(
        'union_member',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('surname', sa.String(), nullable=False),
        sa.Column('union_number', sa.String(), nullable=False),
        sa.Column('student_number', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_PRINT',
    )
    op.create_table(
        'vk_user',
        sa.Column('vk_id', sa.BIGINT(), nullable=False),
        sa.Column('surname', sa.String(), nullable=False),
        sa.Column('number', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('vk_id'),
        schema='STG_PRINT',
    )
    op.create_table(
        'button',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('order', sa.Integer(), nullable=False),
        sa.Column('category_id', sa.Integer(), nullable=False),
        sa.Column('icon', sa.String(), nullable=False),
        sa.Column('link', sa.String(), nullable=False),
        sa.Column('type', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_SERVICES',
    )
    op.create_table(
        'category',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('order', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('type', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_SERVICES',
    )
    op.create_table(
        'scope',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('category_id', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_SERVICES',
    )
    op.create_table(
        'vk_groups',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('group_id', sa.Integer(), nullable=False),
        sa.Column('confirmation_token', sa.String(), nullable=False),
        sa.Column('secret_key', sa.String(), nullable=False),
        sa.Column('create_ts', sa.DateTime(), nullable=False),
        sa.Column('update_ts', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_SOCIAL',
    )
    op.create_table(
        'webhook_storage',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('system', sa.String(), nullable=False),
        sa.Column('message', sa.JSON(none_as_null=True), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_SOCIAL',
    )
    op.create_table(
        'comment_event',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('event_id', sa.Integer(), nullable=False),
        sa.Column('author_name', sa.String(), nullable=False),
        sa.Column('text', sa.String(), nullable=False),
        sa.Column('approve_status', sa.String(), nullable=False),
        sa.Column('create_ts', sa.DateTime(), nullable=False),
        sa.Column('update_ts', sa.DateTime(), nullable=False),
        sa.Column('is_deleted', sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_TIMETABLE',
    )
    op.create_table(
        'comment_lecturer',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('lecturer_id', sa.Integer(), nullable=False),
        sa.Column('author_name', sa.String(), nullable=False),
        sa.Column('text', sa.String(), nullable=False),
        sa.Column('approve_status', sa.String(), nullable=False),
        sa.Column('create_ts', sa.DateTime(), nullable=False),
        sa.Column('update_ts', sa.DateTime(), nullable=False),
        sa.Column('is_deleted', sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_TIMETABLE',
    )
    op.create_table(
        'credentials',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('group', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('scope', sa.JSON(), nullable=False),
        sa.Column('token', sa.JSON(), nullable=False),
        sa.Column('create_ts', sa.DateTime(), nullable=False),
        sa.Column('update_ts', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_TIMETABLE',
    )
    op.create_table(
        'event',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('start_ts', sa.DateTime(), nullable=False),
        sa.Column('end_ts', sa.DateTime(), nullable=False),
        sa.Column('is_deleted', sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_TIMETABLE',
    )
    op.create_table(
        'events_groups',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('event_id', sa.Integer(), nullable=False),
        sa.Column('group_id', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_TIMETABLE',
    )
    op.create_table(
        'events_lecturers',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('event_id', sa.Integer(), nullable=False),
        sa.Column('lecturer_id', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_TIMETABLE',
    )
    op.create_table(
        'events_rooms',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('event_id', sa.Integer(), nullable=False),
        sa.Column('room_id', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_TIMETABLE',
    )
    op.create_table(
        'group',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('number', sa.String(), nullable=False),
        sa.Column('is_deleted', sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_TIMETABLE',
    )
    op.create_table(
        'lecturer',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('first_name', sa.String(), nullable=False),
        sa.Column('middle_name', sa.String(), nullable=False),
        sa.Column('last_name', sa.String(), nullable=False),
        sa.Column('avatar_id', sa.Integer(), nullable=False),
        sa.Column('description', sa.Text(), nullable=False),
        sa.Column('is_deleted', sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_TIMETABLE',
    )
    op.create_table(
        'photo',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('lecturer_id', sa.Integer(), nullable=False),
        sa.Column('link', sa.String(), nullable=False),
        sa.Column('approve_status', sa.String(), nullable=False),
        sa.Column('is_deleted', sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_TIMETABLE',
    )
    op.create_table(
        'room',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('direction', sa.String(), nullable=False),
        sa.Column('building', sa.String(), nullable=False),
        sa.Column('building_url', sa.String(), nullable=False),
        sa.Column('is_deleted', sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_TIMETABLE',
    )
    op.create_table(
        'category',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('read_scope', sa.String(), nullable=False),
        sa.Column('update_scope', sa.String(), nullable=False),
        sa.Column('create_ts', sa.DateTime(), nullable=False),
        sa.Column('modify_ts', sa.DateTime(), nullable=False),
        sa.Column('is_deleted', sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_USERDATA',
    )
    op.create_table(
        'info',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('param_id', sa.Integer(), nullable=False),
        sa.Column('source_id', sa.Integer(), nullable=False),
        sa.Column('owner_id', sa.Integer(), nullable=False),
        sa.Column('value', sa.String(), nullable=False),
        sa.Column('create_ts', sa.DateTime(), nullable=False),
        sa.Column('modify_ts', sa.DateTime(), nullable=False),
        sa.Column('is_deleted', sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_USERDATA',
    )
    op.create_table(
        'param',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('category_id', sa.Integer(), nullable=False),
        sa.Column('is_required', sa.Boolean(), nullable=False),
        sa.Column('changeable', sa.Boolean(), nullable=False),
        sa.Column('type', sa.String(), nullable=False),
        sa.Column('create_ts', sa.DateTime(), nullable=False),
        sa.Column('modify_ts', sa.DateTime(), nullable=False),
        sa.Column('is_deleted', sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_USERDATA',
    )
    op.create_table(
        'source',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('trust_level', sa.Integer(), nullable=False),
        sa.Column('create_ts', sa.DateTime(), nullable=False),
        sa.Column('modify_ts', sa.DateTime(), nullable=False),
        sa.Column('is_deleted', sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_USERDATA',
    )
    op.create_group(
        "test_dwh_stg_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_read"
    )
    op.create_group(
        "test_dwh_stg_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_write"
    )
    op.create_group(
        "test_dwh_stg_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_all"
    )
    op.create_group(
        "test_dwh_stg_marketing_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_marketing_read"
    )
    op.create_group(
        "test_dwh_stg_marketing_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_marketing_write"
    )
    op.create_group(
        "test_dwh_stg_marketing_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_marketing_all"
    )
    op.create_group(
        "test_dwh_stg_services_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_services_read"
    )
    op.create_group(
        "test_dwh_stg_services_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_services_write"
    )
    op.create_group(
        "test_dwh_stg_services_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_services_all"
    )
    op.create_group(
        "test_dwh_stg_social_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_read"
    )
    op.create_group(
        "test_dwh_stg_social_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_write"
    )
    op.create_group(
        "test_dwh_stg_social_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_all"
    )
    op.create_group("test_dwh_stg_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_read")
    op.create_group(
        "test_dwh_stg_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_write"
    )
    op.create_group("test_dwh_stg_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_all")
    op.create_group(
        "test_dwh_stg_pinger_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_pinger_read"
    )
    op.create_group(
        "test_dwh_stg_pinger_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_pinger_write"
    )
    op.create_group(
        "test_dwh_stg_pinger_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_pinger_all"
    )
    op.create_group(
        "test_dwh_stg_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_userdata_read"
    )
    op.create_group(
        "test_dwh_stg_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_userdata_write"
    )
    op.create_group(
        "test_dwh_stg_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_userdata_all"
    )
    op.create_group(
        "test_dwh_stg_print_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_print_read"
    )
    op.create_group(
        "test_dwh_stg_print_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_print_write"
    )
    op.create_group("test_dwh_stg_print_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_print_all")
    op.grant_on_schema(
        "test_dwh_stg_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_read",
        "STG_TIMETABLE",
    )
    op.grant_on_schema(
        "test_dwh_stg_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_write",
        "STG_TIMETABLE",
    )
    op.grant_on_schema(
        "test_dwh_stg_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_all",
        "STG_TIMETABLE",
    )
    op.grant_on_schema(
        "test_dwh_stg_marketing_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_marketing_read",
        "STG_MARKETING",
    )
    op.grant_on_schema(
        "test_dwh_stg_marketing_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_marketing_write",
        "STG_MARKETING",
    )
    op.grant_on_schema(
        "test_dwh_stg_marketing_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_marketing_all",
        "STG_MARKETING",
    )
    op.grant_on_schema(
        "test_dwh_stg_services_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_services_read",
        "STG_SERVICES",
    )
    op.grant_on_schema(
        "test_dwh_stg_services_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_services_write",
        "STG_SERVICES",
    )
    op.grant_on_schema(
        "test_dwh_stg_services_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_services_all",
        "STG_SERVICES",
    )
    op.grant_on_schema(
        "test_dwh_stg_social_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_read",
        "STG_SOCIAL",
    )
    op.grant_on_schema(
        "test_dwh_stg_social_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_write",
        "STG_SOCIAL",
    )
    op.grant_on_schema(
        "test_dwh_stg_social_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_all",
        "STG_SOCIAL",
    )
    op.grant_on_schema(
        "test_dwh_stg_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_read", "STG_AUTH"
    )
    op.grant_on_schema(
        "test_dwh_stg_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_write", "STG_AUTH"
    )
    op.grant_on_schema(
        "test_dwh_stg_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_all", "STG_AUTH"
    )
    op.grant_on_schema(
        "test_dwh_stg_pinger_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_pinger_read",
        "STG_PINGER",
    )
    op.grant_on_schema(
        "test_dwh_stg_pinger_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_pinger_write",
        "STG_PINGER",
    )
    op.grant_on_schema(
        "test_dwh_stg_pinger_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_pinger_all",
        "STG_PINGER",
    )
    op.grant_on_schema(
        "test_dwh_stg_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_userdata_read",
        "STG_USERDATA",
    )
    op.grant_on_schema(
        "test_dwh_stg_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_userdata_write",
        "STG_USERDATA",
    )
    op.grant_on_schema(
        "test_dwh_stg_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_userdata_all",
        "STG_USERDATA",
    )
    op.grant_on_schema(
        "test_dwh_stg_print_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_print_read",
        "STG_PRINT",
    )
    op.grant_on_schema(
        "test_dwh_stg_print_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_print_write",
        "STG_PRINT",
    )
    op.grant_on_schema(
        "test_dwh_stg_print_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_print_all", "STG_PRINT"
    )
    op.grant_on_table(
        "test_dwh_stg_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_read",
        ['SELECT'],
        '"STG_TIMETABLE".credentials',
    )
    op.grant_on_table(
        "test_dwh_stg_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_read",
        ['SELECT'],
        '"STG_TIMETABLE".room',
    )
    op.grant_on_table(
        "test_dwh_stg_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_read",
        ['SELECT'],
        '"STG_TIMETABLE".lecturer',
    )
    op.grant_on_table(
        "test_dwh_stg_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_read",
        ['SELECT'],
        '"STG_TIMETABLE".group',
    )
    op.grant_on_table(
        "test_dwh_stg_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_read",
        ['SELECT'],
        '"STG_TIMETABLE".event',
    )
    op.grant_on_table(
        "test_dwh_stg_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_read",
        ['SELECT'],
        '"STG_TIMETABLE".events_lecturers',
    )
    op.grant_on_table(
        "test_dwh_stg_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_read",
        ['SELECT'],
        '"STG_TIMETABLE".events_rooms',
    )
    op.grant_on_table(
        "test_dwh_stg_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_read",
        ['SELECT'],
        '"STG_TIMETABLE".events_groups',
    )
    op.grant_on_table(
        "test_dwh_stg_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_read",
        ['SELECT'],
        '"STG_TIMETABLE".photo',
    )
    op.grant_on_table(
        "test_dwh_stg_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_read",
        ['SELECT'],
        '"STG_TIMETABLE".comment_lecturer',
    )
    op.grant_on_table(
        "test_dwh_stg_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_read",
        ['SELECT'],
        '"STG_TIMETABLE".comment_event',
    )
    op.grant_on_table(
        "test_dwh_stg_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_TIMETABLE".credentials',
    )
    op.grant_on_table(
        "test_dwh_stg_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_TIMETABLE".room',
    )
    op.grant_on_table(
        "test_dwh_stg_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_TIMETABLE".lecturer',
    )
    op.grant_on_table(
        "test_dwh_stg_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_TIMETABLE".group',
    )
    op.grant_on_table(
        "test_dwh_stg_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_TIMETABLE".event',
    )
    op.grant_on_table(
        "test_dwh_stg_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_TIMETABLE".events_lecturers',
    )
    op.grant_on_table(
        "test_dwh_stg_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_TIMETABLE".events_rooms',
    )
    op.grant_on_table(
        "test_dwh_stg_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_TIMETABLE".events_groups',
    )
    op.grant_on_table(
        "test_dwh_stg_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_TIMETABLE".photo',
    )
    op.grant_on_table(
        "test_dwh_stg_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_TIMETABLE".comment_lecturer',
    )
    op.grant_on_table(
        "test_dwh_stg_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_TIMETABLE".comment_event',
    )
    op.grant_on_table(
        "test_dwh_stg_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_all",
        ['ALL'],
        '"STG_TIMETABLE".credentials',
    )
    op.grant_on_table(
        "test_dwh_stg_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_all",
        ['ALL'],
        '"STG_TIMETABLE".room',
    )
    op.grant_on_table(
        "test_dwh_stg_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_all",
        ['ALL'],
        '"STG_TIMETABLE".lecturer',
    )
    op.grant_on_table(
        "test_dwh_stg_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_all",
        ['ALL'],
        '"STG_TIMETABLE".group',
    )
    op.grant_on_table(
        "test_dwh_stg_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_all",
        ['ALL'],
        '"STG_TIMETABLE".event',
    )
    op.grant_on_table(
        "test_dwh_stg_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_all",
        ['ALL'],
        '"STG_TIMETABLE".events_lecturers',
    )
    op.grant_on_table(
        "test_dwh_stg_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_all",
        ['ALL'],
        '"STG_TIMETABLE".events_rooms',
    )
    op.grant_on_table(
        "test_dwh_stg_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_all",
        ['ALL'],
        '"STG_TIMETABLE".events_groups',
    )
    op.grant_on_table(
        "test_dwh_stg_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_all",
        ['ALL'],
        '"STG_TIMETABLE".photo',
    )
    op.grant_on_table(
        "test_dwh_stg_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_all",
        ['ALL'],
        '"STG_TIMETABLE".comment_lecturer',
    )
    op.grant_on_table(
        "test_dwh_stg_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_all",
        ['ALL'],
        '"STG_TIMETABLE".comment_event',
    )
    op.grant_on_table(
        "test_dwh_stg_marketing_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_marketing_read",
        ['SELECT'],
        '"STG_MARKETING".user',
    )
    op.grant_on_table(
        "test_dwh_stg_marketing_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_marketing_read",
        ['SELECT'],
        '"STG_MARKETING".actions_info',
    )
    op.grant_on_table(
        "test_dwh_stg_marketing_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_marketing_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_MARKETING".user',
    )
    op.grant_on_table(
        "test_dwh_stg_marketing_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_marketing_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_MARKETING".actions_info',
    )
    op.grant_on_table(
        "test_dwh_stg_marketing_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_marketing_all",
        ['ALL'],
        '"STG_MARKETING".user',
    )
    op.grant_on_table(
        "test_dwh_stg_marketing_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_marketing_all",
        ['ALL'],
        '"STG_MARKETING".actions_info',
    )
    op.grant_on_table(
        "test_dwh_stg_services_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_services_read",
        ['SELECT'],
        '"STG_SERVICES".category',
    )
    op.grant_on_table(
        "test_dwh_stg_services_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_services_read",
        ['SELECT'],
        '"STG_SERVICES".button',
    )
    op.grant_on_table(
        "test_dwh_stg_services_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_services_read",
        ['SELECT'],
        '"STG_SERVICES".scope',
    )
    op.grant_on_table(
        "test_dwh_stg_services_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_services_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_SERVICES".category',
    )
    op.grant_on_table(
        "test_dwh_stg_services_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_services_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_SERVICES".button',
    )
    op.grant_on_table(
        "test_dwh_stg_services_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_services_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_SERVICES".scope',
    )
    op.grant_on_table(
        "test_dwh_stg_services_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_services_all",
        ['ALL'],
        '"STG_SERVICES".category',
    )
    op.grant_on_table(
        "test_dwh_stg_services_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_services_all",
        ['ALL'],
        '"STG_SERVICES".button',
    )
    op.grant_on_table(
        "test_dwh_stg_services_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_services_all",
        ['ALL'],
        '"STG_SERVICES".scope',
    )
    op.grant_on_table(
        "test_dwh_stg_social_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_read",
        ['SELECT'],
        '"STG_SOCIAL".webhook_storage',
    )
    op.grant_on_table(
        "test_dwh_stg_social_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_read",
        ['SELECT'],
        '"STG_SOCIAL".vk_groups',
    )
    op.grant_on_table(
        "test_dwh_stg_social_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_SOCIAL".webhook_storage',
    )
    op.grant_on_table(
        "test_dwh_stg_social_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_SOCIAL".vk_groups',
    )
    op.grant_on_table(
        "test_dwh_stg_social_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_all",
        ['ALL'],
        '"STG_SOCIAL".webhook_storage',
    )
    op.grant_on_table(
        "test_dwh_stg_social_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_all",
        ['ALL'],
        '"STG_SOCIAL".vk_groups',
    )
    op.grant_on_table(
        "test_dwh_stg_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_read",
        ['SELECT'],
        '"STG_AUTH".user',
    )
    op.grant_on_table(
        "test_dwh_stg_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_read",
        ['SELECT'],
        '"STG_AUTH".group',
    )
    op.grant_on_table(
        "test_dwh_stg_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_read",
        ['SELECT'],
        '"STG_AUTH".user_group',
    )
    op.grant_on_table(
        "test_dwh_stg_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_read",
        ['SELECT'],
        '"STG_AUTH".auth_method',
    )
    op.grant_on_table(
        "test_dwh_stg_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_read",
        ['SELECT'],
        '"STG_AUTH".user_session',
    )
    op.grant_on_table(
        "test_dwh_stg_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_read",
        ['SELECT'],
        '"STG_AUTH".scope',
    )
    op.grant_on_table(
        "test_dwh_stg_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_read",
        ['SELECT'],
        '"STG_AUTH".group_scope',
    )
    op.grant_on_table(
        "test_dwh_stg_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_read",
        ['SELECT'],
        '"STG_AUTH".user_session_scope',
    )
    op.grant_on_table(
        "test_dwh_stg_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_read",
        ['SELECT'],
        '"STG_AUTH".user_message_delay',
    )
    op.grant_on_table(
        "test_dwh_stg_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_AUTH".user',
    )
    op.grant_on_table(
        "test_dwh_stg_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_AUTH".group',
    )
    op.grant_on_table(
        "test_dwh_stg_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_AUTH".user_group',
    )
    op.grant_on_table(
        "test_dwh_stg_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_AUTH".auth_method',
    )
    op.grant_on_table(
        "test_dwh_stg_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_AUTH".user_session',
    )
    op.grant_on_table(
        "test_dwh_stg_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_AUTH".scope',
    )
    op.grant_on_table(
        "test_dwh_stg_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_AUTH".group_scope',
    )
    op.grant_on_table(
        "test_dwh_stg_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_AUTH".user_session_scope',
    )
    op.grant_on_table(
        "test_dwh_stg_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_AUTH".user_message_delay',
    )
    op.grant_on_table(
        "test_dwh_stg_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_all",
        ['ALL'],
        '"STG_AUTH".user',
    )
    op.grant_on_table(
        "test_dwh_stg_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_all",
        ['ALL'],
        '"STG_AUTH".group',
    )
    op.grant_on_table(
        "test_dwh_stg_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_all",
        ['ALL'],
        '"STG_AUTH".user_group',
    )
    op.grant_on_table(
        "test_dwh_stg_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_all",
        ['ALL'],
        '"STG_AUTH".auth_method',
    )
    op.grant_on_table(
        "test_dwh_stg_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_all",
        ['ALL'],
        '"STG_AUTH".user_session',
    )
    op.grant_on_table(
        "test_dwh_stg_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_all",
        ['ALL'],
        '"STG_AUTH".scope',
    )
    op.grant_on_table(
        "test_dwh_stg_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_all",
        ['ALL'],
        '"STG_AUTH".group_scope',
    )
    op.grant_on_table(
        "test_dwh_stg_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_all",
        ['ALL'],
        '"STG_AUTH".user_session_scope',
    )
    op.grant_on_table(
        "test_dwh_stg_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_all",
        ['ALL'],
        '"STG_AUTH".user_message_delay',
    )
    op.grant_on_table(
        "test_dwh_stg_pinger_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_pinger_read",
        ['SELECT'],
        '"STG_PINGER".receiver',
    )
    op.grant_on_table(
        "test_dwh_stg_pinger_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_pinger_read",
        ['SELECT'],
        '"STG_PINGER".alert',
    )
    op.grant_on_table(
        "test_dwh_stg_pinger_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_pinger_read",
        ['SELECT'],
        '"STG_PINGER".fetcher',
    )
    op.grant_on_table(
        "test_dwh_stg_pinger_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_pinger_read",
        ['SELECT'],
        '"STG_PINGER".metric',
    )
    op.grant_on_table(
        "test_dwh_stg_pinger_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_pinger_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_PINGER".receiver',
    )
    op.grant_on_table(
        "test_dwh_stg_pinger_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_pinger_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_PINGER".alert',
    )
    op.grant_on_table(
        "test_dwh_stg_pinger_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_pinger_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_PINGER".fetcher',
    )
    op.grant_on_table(
        "test_dwh_stg_pinger_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_pinger_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_PINGER".metric',
    )
    op.grant_on_table(
        "test_dwh_stg_pinger_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_pinger_all",
        ['ALL'],
        '"STG_PINGER".receiver',
    )
    op.grant_on_table(
        "test_dwh_stg_pinger_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_pinger_all",
        ['ALL'],
        '"STG_PINGER".alert',
    )
    op.grant_on_table(
        "test_dwh_stg_pinger_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_pinger_all",
        ['ALL'],
        '"STG_PINGER".fetcher',
    )
    op.grant_on_table(
        "test_dwh_stg_pinger_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_pinger_all",
        ['ALL'],
        '"STG_PINGER".metric',
    )
    op.grant_on_table(
        "test_dwh_stg_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_userdata_read",
        ['SELECT'],
        '"STG_USERDATA".category',
    )
    op.grant_on_table(
        "test_dwh_stg_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_userdata_read",
        ['SELECT'],
        '"STG_USERDATA".param',
    )
    op.grant_on_table(
        "test_dwh_stg_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_userdata_read",
        ['SELECT'],
        '"STG_USERDATA".source',
    )
    op.grant_on_table(
        "test_dwh_stg_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_userdata_read",
        ['SELECT'],
        '"STG_USERDATA".info',
    )
    op.grant_on_table(
        "test_dwh_stg_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_USERDATA".category',
    )
    op.grant_on_table(
        "test_dwh_stg_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_USERDATA".param',
    )
    op.grant_on_table(
        "test_dwh_stg_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_USERDATA".source',
    )
    op.grant_on_table(
        "test_dwh_stg_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_USERDATA".info',
    )
    op.grant_on_table(
        "test_dwh_stg_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_userdata_all",
        ['ALL'],
        '"STG_USERDATA".category',
    )
    op.grant_on_table(
        "test_dwh_stg_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_userdata_all",
        ['ALL'],
        '"STG_USERDATA".param',
    )
    op.grant_on_table(
        "test_dwh_stg_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_userdata_all",
        ['ALL'],
        '"STG_USERDATA".source',
    )
    op.grant_on_table(
        "test_dwh_stg_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_userdata_all",
        ['ALL'],
        '"STG_USERDATA".info',
    )
    op.grant_on_table(
        "test_dwh_stg_print_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_print_read",
        ['SELECT'],
        '"STG_PRINT".union_member',
    )
    op.grant_on_table(
        "test_dwh_stg_print_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_print_read",
        ['SELECT'],
        '"STG_PRINT".file',
    )
    op.grant_on_table(
        "test_dwh_stg_print_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_print_read",
        ['SELECT'],
        '"STG_PRINT".print_fact',
    )
    op.grant_on_table(
        "test_dwh_stg_print_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_print_read",
        ['SELECT'],
        '"STG_PRINT".vk_user',
    )
    op.grant_on_table(
        "test_dwh_stg_print_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_print_read",
        ['SELECT'],
        '"STG_PRINT".tg_user',
    )
    op.grant_on_table(
        "test_dwh_stg_print_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_print_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_PRINT".union_member',
    )
    op.grant_on_table(
        "test_dwh_stg_print_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_print_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_PRINT".file',
    )
    op.grant_on_table(
        "test_dwh_stg_print_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_print_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_PRINT".print_fact',
    )
    op.grant_on_table(
        "test_dwh_stg_print_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_print_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_PRINT".vk_user',
    )
    op.grant_on_table(
        "test_dwh_stg_print_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_print_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_PRINT".tg_user',
    )
    op.grant_on_table(
        "test_dwh_stg_print_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_print_all",
        ['ALL'],
        '"STG_PRINT".union_member',
    )
    op.grant_on_table(
        "test_dwh_stg_print_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_print_all",
        ['ALL'],
        '"STG_PRINT".file',
    )
    op.grant_on_table(
        "test_dwh_stg_print_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_print_all",
        ['ALL'],
        '"STG_PRINT".print_fact',
    )
    op.grant_on_table(
        "test_dwh_stg_print_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_print_all",
        ['ALL'],
        '"STG_PRINT".vk_user',
    )
    op.grant_on_table(
        "test_dwh_stg_print_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_print_all",
        ['ALL'],
        '"STG_PRINT".tg_user',
    )


def downgrade():
    op.revoke_on_table(
        "test_dwh_stg_print_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_print_all",
        ['ALL'],
        '"STG_PRINT".tg_user',
    )
    op.revoke_on_table(
        "test_dwh_stg_print_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_print_all",
        ['ALL'],
        '"STG_PRINT".vk_user',
    )
    op.revoke_on_table(
        "test_dwh_stg_print_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_print_all",
        ['ALL'],
        '"STG_PRINT".print_fact',
    )
    op.revoke_on_table(
        "test_dwh_stg_print_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_print_all",
        ['ALL'],
        '"STG_PRINT".file',
    )
    op.revoke_on_table(
        "test_dwh_stg_print_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_print_all",
        ['ALL'],
        '"STG_PRINT".union_member',
    )
    op.revoke_on_table(
        "test_dwh_stg_print_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_print_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_PRINT".tg_user',
    )
    op.revoke_on_table(
        "test_dwh_stg_print_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_print_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_PRINT".vk_user',
    )
    op.revoke_on_table(
        "test_dwh_stg_print_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_print_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_PRINT".print_fact',
    )
    op.revoke_on_table(
        "test_dwh_stg_print_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_print_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_PRINT".file',
    )
    op.revoke_on_table(
        "test_dwh_stg_print_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_print_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_PRINT".union_member',
    )
    op.revoke_on_table(
        "test_dwh_stg_print_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_print_read",
        ['SELECT'],
        '"STG_PRINT".tg_user',
    )
    op.revoke_on_table(
        "test_dwh_stg_print_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_print_read",
        ['SELECT'],
        '"STG_PRINT".vk_user',
    )
    op.revoke_on_table(
        "test_dwh_stg_print_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_print_read",
        ['SELECT'],
        '"STG_PRINT".print_fact',
    )
    op.revoke_on_table(
        "test_dwh_stg_print_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_print_read",
        ['SELECT'],
        '"STG_PRINT".file',
    )
    op.revoke_on_table(
        "test_dwh_stg_print_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_print_read",
        ['SELECT'],
        '"STG_PRINT".union_member',
    )
    op.revoke_on_table(
        "test_dwh_stg_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_userdata_all",
        ['ALL'],
        '"STG_USERDATA".info',
    )
    op.revoke_on_table(
        "test_dwh_stg_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_userdata_all",
        ['ALL'],
        '"STG_USERDATA".source',
    )
    op.revoke_on_table(
        "test_dwh_stg_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_userdata_all",
        ['ALL'],
        '"STG_USERDATA".param',
    )
    op.revoke_on_table(
        "test_dwh_stg_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_userdata_all",
        ['ALL'],
        '"STG_USERDATA".category',
    )
    op.revoke_on_table(
        "test_dwh_stg_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_USERDATA".info',
    )
    op.revoke_on_table(
        "test_dwh_stg_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_USERDATA".source',
    )
    op.revoke_on_table(
        "test_dwh_stg_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_USERDATA".param',
    )
    op.revoke_on_table(
        "test_dwh_stg_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_USERDATA".category',
    )
    op.revoke_on_table(
        "test_dwh_stg_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_userdata_read",
        ['SELECT'],
        '"STG_USERDATA".info',
    )
    op.revoke_on_table(
        "test_dwh_stg_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_userdata_read",
        ['SELECT'],
        '"STG_USERDATA".source',
    )
    op.revoke_on_table(
        "test_dwh_stg_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_userdata_read",
        ['SELECT'],
        '"STG_USERDATA".param',
    )
    op.revoke_on_table(
        "test_dwh_stg_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_userdata_read",
        ['SELECT'],
        '"STG_USERDATA".category',
    )
    op.revoke_on_table(
        "test_dwh_stg_pinger_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_pinger_all",
        ['ALL'],
        '"STG_PINGER".metric',
    )
    op.revoke_on_table(
        "test_dwh_stg_pinger_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_pinger_all",
        ['ALL'],
        '"STG_PINGER".fetcher',
    )
    op.revoke_on_table(
        "test_dwh_stg_pinger_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_pinger_all",
        ['ALL'],
        '"STG_PINGER".alert',
    )
    op.revoke_on_table(
        "test_dwh_stg_pinger_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_pinger_all",
        ['ALL'],
        '"STG_PINGER".receiver',
    )
    op.revoke_on_table(
        "test_dwh_stg_pinger_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_pinger_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_PINGER".metric',
    )
    op.revoke_on_table(
        "test_dwh_stg_pinger_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_pinger_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_PINGER".fetcher',
    )
    op.revoke_on_table(
        "test_dwh_stg_pinger_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_pinger_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_PINGER".alert',
    )
    op.revoke_on_table(
        "test_dwh_stg_pinger_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_pinger_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_PINGER".receiver',
    )
    op.revoke_on_table(
        "test_dwh_stg_pinger_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_pinger_read",
        ['SELECT'],
        '"STG_PINGER".metric',
    )
    op.revoke_on_table(
        "test_dwh_stg_pinger_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_pinger_read",
        ['SELECT'],
        '"STG_PINGER".fetcher',
    )
    op.revoke_on_table(
        "test_dwh_stg_pinger_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_pinger_read",
        ['SELECT'],
        '"STG_PINGER".alert',
    )
    op.revoke_on_table(
        "test_dwh_stg_pinger_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_pinger_read",
        ['SELECT'],
        '"STG_PINGER".receiver',
    )
    op.revoke_on_table(
        "test_dwh_stg_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_all",
        ['ALL'],
        '"STG_AUTH".user_message_delay',
    )
    op.revoke_on_table(
        "test_dwh_stg_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_all",
        ['ALL'],
        '"STG_AUTH".user_session_scope',
    )
    op.revoke_on_table(
        "test_dwh_stg_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_all",
        ['ALL'],
        '"STG_AUTH".group_scope',
    )
    op.revoke_on_table(
        "test_dwh_stg_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_all",
        ['ALL'],
        '"STG_AUTH".scope',
    )
    op.revoke_on_table(
        "test_dwh_stg_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_all",
        ['ALL'],
        '"STG_AUTH".user_session',
    )
    op.revoke_on_table(
        "test_dwh_stg_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_all",
        ['ALL'],
        '"STG_AUTH".auth_method',
    )
    op.revoke_on_table(
        "test_dwh_stg_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_all",
        ['ALL'],
        '"STG_AUTH".user_group',
    )
    op.revoke_on_table(
        "test_dwh_stg_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_all",
        ['ALL'],
        '"STG_AUTH".group',
    )
    op.revoke_on_table(
        "test_dwh_stg_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_all",
        ['ALL'],
        '"STG_AUTH".user',
    )
    op.revoke_on_table(
        "test_dwh_stg_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_AUTH".user_message_delay',
    )
    op.revoke_on_table(
        "test_dwh_stg_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_AUTH".user_session_scope',
    )
    op.revoke_on_table(
        "test_dwh_stg_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_AUTH".group_scope',
    )
    op.revoke_on_table(
        "test_dwh_stg_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_AUTH".scope',
    )
    op.revoke_on_table(
        "test_dwh_stg_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_AUTH".user_session',
    )
    op.revoke_on_table(
        "test_dwh_stg_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_AUTH".auth_method',
    )
    op.revoke_on_table(
        "test_dwh_stg_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_AUTH".user_group',
    )
    op.revoke_on_table(
        "test_dwh_stg_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_AUTH".group',
    )
    op.revoke_on_table(
        "test_dwh_stg_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_AUTH".user',
    )
    op.revoke_on_table(
        "test_dwh_stg_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_read",
        ['SELECT'],
        '"STG_AUTH".user_message_delay',
    )
    op.revoke_on_table(
        "test_dwh_stg_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_read",
        ['SELECT'],
        '"STG_AUTH".user_session_scope',
    )
    op.revoke_on_table(
        "test_dwh_stg_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_read",
        ['SELECT'],
        '"STG_AUTH".group_scope',
    )
    op.revoke_on_table(
        "test_dwh_stg_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_read",
        ['SELECT'],
        '"STG_AUTH".scope',
    )
    op.revoke_on_table(
        "test_dwh_stg_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_read",
        ['SELECT'],
        '"STG_AUTH".user_session',
    )
    op.revoke_on_table(
        "test_dwh_stg_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_read",
        ['SELECT'],
        '"STG_AUTH".auth_method',
    )
    op.revoke_on_table(
        "test_dwh_stg_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_read",
        ['SELECT'],
        '"STG_AUTH".user_group',
    )
    op.revoke_on_table(
        "test_dwh_stg_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_read",
        ['SELECT'],
        '"STG_AUTH".group',
    )
    op.revoke_on_table(
        "test_dwh_stg_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_read",
        ['SELECT'],
        '"STG_AUTH".user',
    )
    op.revoke_on_table(
        "test_dwh_stg_social_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_all",
        ['ALL'],
        '"STG_SOCIAL".vk_groups',
    )
    op.revoke_on_table(
        "test_dwh_stg_social_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_all",
        ['ALL'],
        '"STG_SOCIAL".webhook_storage',
    )
    op.revoke_on_table(
        "test_dwh_stg_social_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_SOCIAL".vk_groups',
    )
    op.revoke_on_table(
        "test_dwh_stg_social_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_SOCIAL".webhook_storage',
    )
    op.revoke_on_table(
        "test_dwh_stg_social_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_read",
        ['SELECT'],
        '"STG_SOCIAL".vk_groups',
    )
    op.revoke_on_table(
        "test_dwh_stg_social_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_read",
        ['SELECT'],
        '"STG_SOCIAL".webhook_storage',
    )
    op.revoke_on_table(
        "test_dwh_stg_services_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_services_all",
        ['ALL'],
        '"STG_SERVICES".scope',
    )
    op.revoke_on_table(
        "test_dwh_stg_services_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_services_all",
        ['ALL'],
        '"STG_SERVICES".button',
    )
    op.revoke_on_table(
        "test_dwh_stg_services_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_services_all",
        ['ALL'],
        '"STG_SERVICES".category',
    )
    op.revoke_on_table(
        "test_dwh_stg_services_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_services_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_SERVICES".scope',
    )
    op.revoke_on_table(
        "test_dwh_stg_services_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_services_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_SERVICES".button',
    )
    op.revoke_on_table(
        "test_dwh_stg_services_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_services_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_SERVICES".category',
    )
    op.revoke_on_table(
        "test_dwh_stg_services_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_services_read",
        ['SELECT'],
        '"STG_SERVICES".scope',
    )
    op.revoke_on_table(
        "test_dwh_stg_services_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_services_read",
        ['SELECT'],
        '"STG_SERVICES".button',
    )
    op.revoke_on_table(
        "test_dwh_stg_services_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_services_read",
        ['SELECT'],
        '"STG_SERVICES".category',
    )
    op.revoke_on_table(
        "test_dwh_stg_marketing_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_marketing_all",
        ['ALL'],
        '"STG_MARKETING".actions_info',
    )
    op.revoke_on_table(
        "test_dwh_stg_marketing_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_marketing_all",
        ['ALL'],
        '"STG_MARKETING".user',
    )
    op.revoke_on_table(
        "test_dwh_stg_marketing_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_marketing_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_MARKETING".actions_info',
    )
    op.revoke_on_table(
        "test_dwh_stg_marketing_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_marketing_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_MARKETING".user',
    )
    op.revoke_on_table(
        "test_dwh_stg_marketing_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_marketing_read",
        ['SELECT'],
        '"STG_MARKETING".actions_info',
    )
    op.revoke_on_table(
        "test_dwh_stg_marketing_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_marketing_read",
        ['SELECT'],
        '"STG_MARKETING".user',
    )
    op.revoke_on_table(
        "test_dwh_stg_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_all",
        ['ALL'],
        '"STG_TIMETABLE".comment_event',
    )
    op.revoke_on_table(
        "test_dwh_stg_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_all",
        ['ALL'],
        '"STG_TIMETABLE".comment_lecturer',
    )
    op.revoke_on_table(
        "test_dwh_stg_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_all",
        ['ALL'],
        '"STG_TIMETABLE".photo',
    )
    op.revoke_on_table(
        "test_dwh_stg_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_all",
        ['ALL'],
        '"STG_TIMETABLE".events_groups',
    )
    op.revoke_on_table(
        "test_dwh_stg_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_all",
        ['ALL'],
        '"STG_TIMETABLE".events_rooms',
    )
    op.revoke_on_table(
        "test_dwh_stg_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_all",
        ['ALL'],
        '"STG_TIMETABLE".events_lecturers',
    )
    op.revoke_on_table(
        "test_dwh_stg_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_all",
        ['ALL'],
        '"STG_TIMETABLE".event',
    )
    op.revoke_on_table(
        "test_dwh_stg_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_all",
        ['ALL'],
        '"STG_TIMETABLE".group',
    )
    op.revoke_on_table(
        "test_dwh_stg_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_all",
        ['ALL'],
        '"STG_TIMETABLE".lecturer',
    )
    op.revoke_on_table(
        "test_dwh_stg_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_all",
        ['ALL'],
        '"STG_TIMETABLE".room',
    )
    op.revoke_on_table(
        "test_dwh_stg_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_all",
        ['ALL'],
        '"STG_TIMETABLE".credentials',
    )
    op.revoke_on_table(
        "test_dwh_stg_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_TIMETABLE".comment_event',
    )
    op.revoke_on_table(
        "test_dwh_stg_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_TIMETABLE".comment_lecturer',
    )
    op.revoke_on_table(
        "test_dwh_stg_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_TIMETABLE".photo',
    )
    op.revoke_on_table(
        "test_dwh_stg_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_TIMETABLE".events_groups',
    )
    op.revoke_on_table(
        "test_dwh_stg_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_TIMETABLE".events_rooms',
    )
    op.revoke_on_table(
        "test_dwh_stg_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_TIMETABLE".events_lecturers',
    )
    op.revoke_on_table(
        "test_dwh_stg_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_TIMETABLE".event',
    )
    op.revoke_on_table(
        "test_dwh_stg_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_TIMETABLE".group',
    )
    op.revoke_on_table(
        "test_dwh_stg_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_TIMETABLE".lecturer',
    )
    op.revoke_on_table(
        "test_dwh_stg_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_TIMETABLE".room',
    )
    op.revoke_on_table(
        "test_dwh_stg_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_TIMETABLE".credentials',
    )
    op.revoke_on_table(
        "test_dwh_stg_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_read",
        ['SELECT'],
        '"STG_TIMETABLE".comment_event',
    )
    op.revoke_on_table(
        "test_dwh_stg_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_read",
        ['SELECT'],
        '"STG_TIMETABLE".comment_lecturer',
    )
    op.revoke_on_table(
        "test_dwh_stg_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_read",
        ['SELECT'],
        '"STG_TIMETABLE".photo',
    )
    op.revoke_on_table(
        "test_dwh_stg_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_read",
        ['SELECT'],
        '"STG_TIMETABLE".events_groups',
    )
    op.revoke_on_table(
        "test_dwh_stg_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_read",
        ['SELECT'],
        '"STG_TIMETABLE".events_rooms',
    )
    op.revoke_on_table(
        "test_dwh_stg_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_read",
        ['SELECT'],
        '"STG_TIMETABLE".events_lecturers',
    )
    op.revoke_on_table(
        "test_dwh_stg_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_read",
        ['SELECT'],
        '"STG_TIMETABLE".event',
    )
    op.revoke_on_table(
        "test_dwh_stg_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_read",
        ['SELECT'],
        '"STG_TIMETABLE".group',
    )
    op.revoke_on_table(
        "test_dwh_stg_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_read",
        ['SELECT'],
        '"STG_TIMETABLE".lecturer',
    )
    op.revoke_on_table(
        "test_dwh_stg_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_read",
        ['SELECT'],
        '"STG_TIMETABLE".room',
    )
    op.revoke_on_table(
        "test_dwh_stg_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_read",
        ['SELECT'],
        '"STG_TIMETABLE".credentials',
    )
    op.revoke_on_schema(
        "test_dwh_stg_print_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_print_all", "STG_PRINT"
    )
    op.revoke_on_schema(
        "test_dwh_stg_print_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_print_write",
        "STG_PRINT",
    )
    op.revoke_on_schema(
        "test_dwh_stg_print_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_print_read",
        "STG_PRINT",
    )
    op.revoke_on_schema(
        "test_dwh_stg_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_userdata_all",
        "STG_USERDATA",
    )
    op.revoke_on_schema(
        "test_dwh_stg_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_userdata_write",
        "STG_USERDATA",
    )
    op.revoke_on_schema(
        "test_dwh_stg_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_userdata_read",
        "STG_USERDATA",
    )
    op.revoke_on_schema(
        "test_dwh_stg_pinger_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_pinger_all",
        "STG_PINGER",
    )
    op.revoke_on_schema(
        "test_dwh_stg_pinger_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_pinger_write",
        "STG_PINGER",
    )
    op.revoke_on_schema(
        "test_dwh_stg_pinger_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_pinger_read",
        "STG_PINGER",
    )
    op.revoke_on_schema(
        "test_dwh_stg_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_all", "STG_AUTH"
    )
    op.revoke_on_schema(
        "test_dwh_stg_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_write", "STG_AUTH"
    )
    op.revoke_on_schema(
        "test_dwh_stg_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_read", "STG_AUTH"
    )
    op.revoke_on_schema(
        "test_dwh_stg_social_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_all",
        "STG_SOCIAL",
    )
    op.revoke_on_schema(
        "test_dwh_stg_social_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_write",
        "STG_SOCIAL",
    )
    op.revoke_on_schema(
        "test_dwh_stg_social_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_read",
        "STG_SOCIAL",
    )
    op.revoke_on_schema(
        "test_dwh_stg_services_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_services_all",
        "STG_SERVICES",
    )
    op.revoke_on_schema(
        "test_dwh_stg_services_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_services_write",
        "STG_SERVICES",
    )
    op.revoke_on_schema(
        "test_dwh_stg_services_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_services_read",
        "STG_SERVICES",
    )
    op.revoke_on_schema(
        "test_dwh_stg_marketing_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_marketing_all",
        "STG_MARKETING",
    )
    op.revoke_on_schema(
        "test_dwh_stg_marketing_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_marketing_write",
        "STG_MARKETING",
    )
    op.revoke_on_schema(
        "test_dwh_stg_marketing_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_marketing_read",
        "STG_MARKETING",
    )
    op.revoke_on_schema(
        "test_dwh_stg_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_all",
        "STG_TIMETABLE",
    )
    op.revoke_on_schema(
        "test_dwh_stg_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_write",
        "STG_TIMETABLE",
    )
    op.revoke_on_schema(
        "test_dwh_stg_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_read",
        "STG_TIMETABLE",
    )
    op.drop_table('source', schema='STG_USERDATA')
    op.drop_table('param', schema='STG_USERDATA')
    op.drop_table('info', schema='STG_USERDATA')
    op.drop_table('category', schema='STG_USERDATA')
    op.drop_table('room', schema='STG_TIMETABLE')
    op.drop_table('photo', schema='STG_TIMETABLE')
    op.drop_table('lecturer', schema='STG_TIMETABLE')
    op.drop_table('group', schema='STG_TIMETABLE')
    op.drop_table('events_rooms', schema='STG_TIMETABLE')
    op.drop_table('events_lecturers', schema='STG_TIMETABLE')
    op.drop_table('events_groups', schema='STG_TIMETABLE')
    op.drop_table('event', schema='STG_TIMETABLE')
    op.drop_table('credentials', schema='STG_TIMETABLE')
    op.drop_table('comment_lecturer', schema='STG_TIMETABLE')
    op.drop_table('comment_event', schema='STG_TIMETABLE')
    op.drop_table('webhook_storage', schema='STG_SOCIAL')
    op.drop_table('vk_groups', schema='STG_SOCIAL')
    op.drop_table('scope', schema='STG_SERVICES')
    op.drop_table('category', schema='STG_SERVICES')
    op.drop_table('button', schema='STG_SERVICES')
    op.drop_table('vk_user', schema='STG_PRINT')
    op.drop_table('union_member', schema='STG_PRINT')
    op.drop_table('tg_user', schema='STG_PRINT')
    op.drop_table('print_fact', schema='STG_PRINT')
    op.drop_table('file', schema='STG_PRINT')
    op.drop_table('receiver', schema='STG_PINGER')
    op.drop_table('metric', schema='STG_PINGER')
    op.drop_table('fetcher', schema='STG_PINGER')
    op.drop_table('alert', schema='STG_PINGER')
    op.drop_table('user', schema='STG_MARKETING')
    op.drop_table('actions_info', schema='STG_MARKETING')
    op.drop_table('user_session_scope', schema='STG_AUTH')
    op.drop_table('user_session', schema='STG_AUTH')
    op.drop_table('user_message_delay', schema='STG_AUTH')
    op.drop_table('user_group', schema='STG_AUTH')
    op.drop_table('user', schema='STG_AUTH')
    op.drop_table('scope', schema='STG_AUTH')
    op.drop_table('group_scope', schema='STG_AUTH')
    op.drop_table('group', schema='STG_AUTH')
    op.drop_table('auth_method', schema='STG_AUTH')
    op.delete_group("test_dwh_stg_print_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_print_all")
    op.delete_group(
        "test_dwh_stg_print_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_print_write"
    )
    op.delete_group(
        "test_dwh_stg_print_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_print_read"
    )
    op.delete_group(
        "test_dwh_stg_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_userdata_all"
    )
    op.delete_group(
        "test_dwh_stg_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_userdata_write"
    )
    op.delete_group(
        "test_dwh_stg_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_userdata_read"
    )
    op.delete_group(
        "test_dwh_stg_pinger_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_pinger_all"
    )
    op.delete_group(
        "test_dwh_stg_pinger_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_pinger_write"
    )
    op.delete_group(
        "test_dwh_stg_pinger_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_pinger_read"
    )
    op.delete_group("test_dwh_stg_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_all")
    op.delete_group(
        "test_dwh_stg_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_write"
    )
    op.delete_group("test_dwh_stg_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_auth_read")
    op.delete_group(
        "test_dwh_stg_social_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_all"
    )
    op.delete_group(
        "test_dwh_stg_social_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_write"
    )
    op.delete_group(
        "test_dwh_stg_social_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_read"
    )
    op.delete_group(
        "test_dwh_stg_services_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_services_all"
    )
    op.delete_group(
        "test_dwh_stg_services_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_services_write"
    )
    op.delete_group(
        "test_dwh_stg_services_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_services_read"
    )
    op.delete_group(
        "test_dwh_stg_marketing_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_marketing_all"
    )
    op.delete_group(
        "test_dwh_stg_marketing_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_marketing_write"
    )
    op.delete_group(
        "test_dwh_stg_marketing_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_marketing_read"
    )
    op.delete_group(
        "test_dwh_stg_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_all"
    )
    op.delete_group(
        "test_dwh_stg_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_write"
    )
    op.delete_group(
        "test_dwh_stg_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_read"
    )
    op.drop_table_schema("STG_PRINT")
    op.drop_table_schema("STG_USERDATA")
    op.drop_table_schema("STG_PINGER")
    op.drop_table_schema("STG_AUTH")
    op.drop_table_schema("STG_SOCIAL")
    op.drop_table_schema("STG_SERVICES")
    op.drop_table_schema("STG_MARKETING")
    op.drop_table_schema("STG_TIMETABLE")
