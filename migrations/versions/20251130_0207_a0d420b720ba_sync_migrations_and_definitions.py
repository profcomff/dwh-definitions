"""sync migrations and definitions

Revision ID: a0d420b720ba
Revises: 3ac342622c64
Create Date: 2025-11-30 02:07:25.872931

"""

import os

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = 'a0d420b720ba'
down_revision = '3ac342622c64'
branch_labels = None
depends_on = None


def upgrade():
    op.create_group(
        "test_sensitive_dwh_stg_userdata_all"
        if os.getenv("ENVIRONMENT") != "production"
        else "prod_sensitive_dwh_stg_userdata_all"
    )
    op.create_group(
        "test_sensitive_dwh_stg_userdata_read"
        if os.getenv("ENVIRONMENT") != "production"
        else "prod_sensitive_dwh_stg_userdata_read"
    )
    op.create_group(
        "test_sensitive_dwh_stg_userdata_write"
        if os.getenv("ENVIRONMENT") != "production"
        else "prod_sensitive_dwh_stg_userdata_write"
    )
    op.grant_on_schema(
        (
            "test_sensitive_dwh_stg_userdata_all"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_sensitive_dwh_stg_userdata_all"
        ),
        "STG_USERDATA",
    )
    op.grant_on_schema(
        (
            "test_sensitive_dwh_stg_userdata_read"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_sensitive_dwh_stg_userdata_read"
        ),
        "STG_USERDATA",
    )
    op.grant_on_schema(
        (
            "test_sensitive_dwh_stg_userdata_write"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_sensitive_dwh_stg_userdata_write"
        ),
        "STG_USERDATA",
    )
    op.grant_on_table(
        "test_dwh_dm_rental_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_rental_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DM_RENTAL".dm_strike',
    )
    op.grant_on_table(
        "test_dwh_dm_rental_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_rental_read",
        ['SELECT'],
        '"DM_RENTAL".dm_strike',
    )
    op.grant_on_table(
        "test_dwh_dm_rental_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_rental_all",
        ['ALL'],
        '"DM_RENTAL".dm_strike',
    )
    op.grant_on_table(
        "test_dwh_dm_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_timetable_all",
        ['ALL'],
        '"DM_TIMETABLE".dm_timetable_act',
    )
    op.grant_on_table(
        "test_dwh_dm_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_timetable_read",
        ['SELECT'],
        '"DM_TIMETABLE".dm_timetable_act',
    )
    op.grant_on_table(
        "test_dwh_dm_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DM_TIMETABLE".dm_timetable_act',
    )
    op.grant_on_table(
        "test_dwh_dm_user_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_user_read",
        ['SELECT'],
        '"DM_USER".union_member_card',
    )
    op.grant_on_table(
        "test_dwh_dm_user_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_user_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DM_USER".union_member_card',
    )
    op.grant_on_table(
        "test_dwh_dm_user_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_user_all",
        ['ALL'],
        '"DM_USER".union_member_card',
    )
    op.grant_on_table(
        "test_dwh_dwh_user_info_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_user_info_all",
        ['ALL'],
        '"DWH_USER_INFO".encrypted_info',
    )
    op.grant_on_table(
        "test_dwh_dwh_user_info_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_user_info_read",
        ['SELECT'],
        '"DWH_USER_INFO".encrypted_info',
    )
    op.grant_on_table(
        "test_dwh_dwh_user_info_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_user_info_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DWH_USER_INFO".encrypted_info',
    )
    op.alter_column(
        'git_hub',
        'issue_id',
        existing_type=sa.VARCHAR(),
        comment='Идентификатор issue',
        existing_nullable=True,
        schema='ODS_SOCIAL',
    )
    op.alter_column(
        'git_hub',
        'user_id',
        existing_type=sa.VARCHAR(),
        comment='Идентификатор пользователя открывшего issue',
        existing_nullable=True,
        schema='ODS_SOCIAL',
    )
    op.alter_column(
        'git_hub',
        'repository_id',
        existing_type=sa.VARCHAR(),
        comment='Идентификатор репозитория',
        existing_nullable=True,
        schema='ODS_SOCIAL',
    )
    op.alter_column(
        'git_hub',
        'assignee_id',
        existing_type=sa.VARCHAR(),
        comment='Идентификатор назначенного исполнителем issue',
        existing_nullable=True,
        schema='ODS_SOCIAL',
    )
    op.alter_column(
        'git_hub',
        'assignee_login',
        existing_type=sa.VARCHAR(),
        comment='Логин назначенного исполнителем issue',
        existing_nullable=True,
        schema='ODS_SOCIAL',
    )
    op.alter_column(
        'git_hub',
        'organization_id',
        existing_type=sa.VARCHAR(),
        nullable=False,
        comment='Идентификатор организации',
        schema='ODS_SOCIAL',
    )
    op.grant_on_table(
        "test_dwh_ods_social_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_social_read",
        ['SELECT'],
        '"ODS_SOCIAL".git_hub',
    )
    op.grant_on_table(
        "test_dwh_ods_social_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_social_all",
        ['ALL'],
        '"ODS_SOCIAL".git_hub',
    )
    op.grant_on_table(
        "test_dwh_ods_social_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_social_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_SOCIAL".git_hub',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read",
        ['SELECT'],
        '"ODS_USERDATA".card',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all",
        ['ALL'],
        '"ODS_USERDATA".card',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USERDATA".card',
    )
    op.alter_column(
        'git_hub_username',
        'username',
        existing_type=sa.VARCHAR(),
        comment='Имя пользователя GitHub',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'git_hub_username',
        'user_id',
        existing_type=sa.INTEGER(),
        comment='Идентификатор пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'git_hub_username',
        'source',
        existing_type=sa.VARCHAR(),
        comment='Источник данных',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'git_hub_username',
        'created',
        existing_type=postgresql.TIMESTAMP(),
        comment='Дата создания записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'git_hub_username',
        'modified',
        existing_type=postgresql.TIMESTAMP(),
        comment='Дата последнего изменения записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'git_hub_username',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment='Флаг удаления записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read",
        ['SELECT'],
        '"ODS_USERDATA".rzd',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all",
        ['ALL'],
        '"ODS_USERDATA".rzd',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USERDATA".rzd',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read",
        ['SELECT'],
        '"ODS_USERDATA".status',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all",
        ['ALL'],
        '"ODS_USERDATA".status',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USERDATA".status',
    )
    op.alter_column(
        'union_member',
        'middle_name',
        existing_type=sa.VARCHAR(),
        comment='Отчество пользователя',
        existing_nullable=True,
        schema='STG_UNION_MEMBER',
    )
    op.grant_on_table(
        "test_dwh_stg_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_USERDATA".encrypted_info',
    )
    op.grant_on_table(
        "test_dwh_stg_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_userdata_read",
        ['SELECT'],
        '"STG_USERDATA".encrypted_info',
    )
    op.grant_on_table(
        "test_dwh_stg_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_userdata_all",
        ['ALL'],
        '"STG_USERDATA".encrypted_info',
    )
    op.grant_on_table(
        (
            "test_sensitive_dwh_stg_userdata_write"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_sensitive_dwh_stg_userdata_write"
        ),
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_USERDATA".info_keys',
    )
    op.grant_on_table(
        (
            "test_sensitive_dwh_stg_userdata_all"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_sensitive_dwh_stg_userdata_all"
        ),
        ['ALL'],
        '"STG_USERDATA".info_keys',
    )
    op.grant_on_table(
        (
            "test_sensitive_dwh_stg_userdata_read"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_sensitive_dwh_stg_userdata_read"
        ),
        ['SELECT'],
        '"STG_USERDATA".info_keys',
    )


def downgrade():
    op.revoke_on_table(
        (
            "test_sensitive_dwh_stg_userdata_read"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_sensitive_dwh_stg_userdata_read"
        ),
        ['SELECT'],
        '"STG_USERDATA".info_keys',
    )
    op.revoke_on_table(
        (
            "test_sensitive_dwh_stg_userdata_all"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_sensitive_dwh_stg_userdata_all"
        ),
        ['ALL'],
        '"STG_USERDATA".info_keys',
    )
    op.revoke_on_table(
        (
            "test_sensitive_dwh_stg_userdata_write"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_sensitive_dwh_stg_userdata_write"
        ),
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_USERDATA".info_keys',
    )
    op.revoke_on_table(
        "test_dwh_stg_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_userdata_all",
        ['ALL'],
        '"STG_USERDATA".encrypted_info',
    )
    op.revoke_on_table(
        "test_dwh_stg_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_userdata_read",
        ['SELECT'],
        '"STG_USERDATA".encrypted_info',
    )
    op.revoke_on_table(
        "test_dwh_stg_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_USERDATA".encrypted_info',
    )
    op.add_column(
        'union_member', sa.Column('card', sa.VARCHAR(), autoincrement=False, nullable=True), schema='STG_UNION_MEMBER'
    )
    op.alter_column(
        'union_member',
        'middle_name',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Отчество пользователя',
        existing_nullable=True,
        schema='STG_UNION_MEMBER',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USERDATA".status',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all",
        ['ALL'],
        '"ODS_USERDATA".status',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read",
        ['SELECT'],
        '"ODS_USERDATA".status',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USERDATA".rzd',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all",
        ['ALL'],
        '"ODS_USERDATA".rzd',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read",
        ['SELECT'],
        '"ODS_USERDATA".rzd',
    )
    op.alter_column(
        'git_hub_username',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment=None,
        existing_comment='Флаг удаления записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'git_hub_username',
        'modified',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Дата последнего изменения записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'git_hub_username',
        'created',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Дата создания записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'git_hub_username',
        'source',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Источник данных',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'git_hub_username',
        'user_id',
        existing_type=sa.INTEGER(),
        comment=None,
        existing_comment='Идентификатор пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'git_hub_username',
        'username',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Имя пользователя GitHub',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USERDATA".card',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all",
        ['ALL'],
        '"ODS_USERDATA".card',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read",
        ['SELECT'],
        '"ODS_USERDATA".card',
    )
    op.revoke_on_table(
        "test_dwh_ods_social_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_social_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_SOCIAL".git_hub',
    )
    op.revoke_on_table(
        "test_dwh_ods_social_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_social_all",
        ['ALL'],
        '"ODS_SOCIAL".git_hub',
    )
    op.revoke_on_table(
        "test_dwh_ods_social_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_social_read",
        ['SELECT'],
        '"ODS_SOCIAL".git_hub',
    )
    op.alter_column(
        'git_hub',
        'organization_id',
        existing_type=sa.VARCHAR(),
        nullable=True,
        comment=None,
        existing_comment='Идентификатор организации',
        schema='ODS_SOCIAL',
    )
    op.alter_column(
        'git_hub',
        'assignee_login',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Логин назначенного исполнителем issue',
        existing_nullable=True,
        schema='ODS_SOCIAL',
    )
    op.alter_column(
        'git_hub',
        'assignee_id',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Идентификатор назначенного исполнителем issue',
        existing_nullable=True,
        schema='ODS_SOCIAL',
    )
    op.alter_column(
        'git_hub',
        'repository_id',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Идентификатор репозитория',
        existing_nullable=True,
        schema='ODS_SOCIAL',
    )
    op.alter_column(
        'git_hub',
        'user_id',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Идентификатор пользователя открывшего issue',
        existing_nullable=True,
        schema='ODS_SOCIAL',
    )
    op.alter_column(
        'git_hub',
        'issue_id',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Идентификатор issue',
        existing_nullable=True,
        schema='ODS_SOCIAL',
    )
    op.revoke_on_table(
        "test_dwh_dwh_user_info_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_user_info_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DWH_USER_INFO".encrypted_info',
    )
    op.revoke_on_table(
        "test_dwh_dwh_user_info_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_user_info_read",
        ['SELECT'],
        '"DWH_USER_INFO".encrypted_info',
    )
    op.revoke_on_table(
        "test_dwh_dwh_user_info_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_user_info_all",
        ['ALL'],
        '"DWH_USER_INFO".encrypted_info',
    )
    op.revoke_on_table(
        "test_dwh_dm_user_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_user_all",
        ['ALL'],
        '"DM_USER".union_member_card',
    )
    op.revoke_on_table(
        "test_dwh_dm_user_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_user_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DM_USER".union_member_card',
    )
    op.revoke_on_table(
        "test_dwh_dm_user_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_user_read",
        ['SELECT'],
        '"DM_USER".union_member_card',
    )
    op.revoke_on_table(
        "test_dwh_dm_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DM_TIMETABLE".dm_timetable_act',
    )
    op.revoke_on_table(
        "test_dwh_dm_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_timetable_read",
        ['SELECT'],
        '"DM_TIMETABLE".dm_timetable_act',
    )
    op.revoke_on_table(
        "test_dwh_dm_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_timetable_all",
        ['ALL'],
        '"DM_TIMETABLE".dm_timetable_act',
    )
    op.revoke_on_table(
        "test_dwh_dm_rental_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_rental_all",
        ['ALL'],
        '"DM_RENTAL".dm_strike',
    )
    op.revoke_on_table(
        "test_dwh_dm_rental_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_rental_read",
        ['SELECT'],
        '"DM_RENTAL".dm_strike',
    )
    op.revoke_on_table(
        "test_dwh_dm_rental_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_rental_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DM_RENTAL".dm_strike',
    )
    op.revoke_on_schema(
        (
            "test_sensitive_dwh_stg_userdata_write"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_sensitive_dwh_stg_userdata_write"
        ),
        "STG_USERDATA",
    )
    op.revoke_on_schema(
        (
            "test_sensitive_dwh_stg_userdata_read"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_sensitive_dwh_stg_userdata_read"
        ),
        "STG_USERDATA",
    )
    op.revoke_on_schema(
        (
            "test_sensitive_dwh_stg_userdata_all"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_sensitive_dwh_stg_userdata_all"
        ),
        "STG_USERDATA",
    )
    op.delete_group(
        "test_sensitive_dwh_stg_userdata_write"
        if os.getenv("ENVIRONMENT") != "production"
        else "prod_sensitive_dwh_stg_userdata_write"
    )
    op.delete_group(
        "test_sensitive_dwh_stg_userdata_read"
        if os.getenv("ENVIRONMENT") != "production"
        else "prod_sensitive_dwh_stg_userdata_read"
    )
    op.delete_group(
        "test_sensitive_dwh_stg_userdata_all"
        if os.getenv("ENVIRONMENT") != "production"
        else "prod_sensitive_dwh_stg_userdata_all"
    )
