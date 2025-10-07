"""multicommit: fix state

Revision ID: ab55e423b1e4
Revises: 3ac342622c64
Create Date: 2025-10-07 14:46:07.684999

"""

import os

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'ab55e423b1e4'
down_revision = '3ac342622c64'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column(
        'dm_lecturer_comment_act',
        'mark_weighted',
        existing_type=sa.DOUBLE_PRECISION(precision=53),
        type_=sa.Integer(),
        existing_comment='Взвешенная оценка преподавателя',
        existing_nullable=False,
        existing_server_default=sa.text("'0'::double precision"),
        schema='DM_RATING',
    )
    op.alter_column(
        'dm_lecturer_comment_act',
        'mark_kindness_weighted',
        existing_type=sa.DOUBLE_PRECISION(precision=53),
        type_=sa.Integer(),
        existing_comment='Взвешенная доброта преподавателя',
        existing_nullable=False,
        existing_server_default=sa.text("'0'::double precision"),
        schema='DM_RATING',
    )
    op.alter_column(
        'dm_lecturer_comment_act',
        'mark_clarity_weighted',
        existing_type=sa.DOUBLE_PRECISION(precision=53),
        type_=sa.Integer(),
        existing_comment='Взвешенная понятность преподавателя',
        existing_nullable=False,
        existing_server_default=sa.text("'0'::double precision"),
        schema='DM_RATING',
    )
    op.alter_column(
        'dm_lecturer_comment_act',
        'mark_freebie_weighted',
        existing_type=sa.DOUBLE_PRECISION(precision=53),
        type_=sa.Integer(),
        existing_comment='Взвешенная халявность преподавателя',
        existing_nullable=False,
        existing_server_default=sa.text("'0'::double precision"),
        schema='DM_RATING',
    )
    op.drop_table_comment('dm_strike', existing_comment='\n    Витрина страйки\n    ', schema='DM_RENTAL')
    op.drop_index(op.f('lecturer_ts_idx'), table_name='lecturer', schema='DWH_RATING')

    # МИГРАЦИЯ: Надо поменять на op.execute("... USING issue_id::Integer");
    op.alter_column(
        'git_hub',
        'issue_id',
        existing_type=sa.VARCHAR(),
        type_=sa.Integer(),
        comment='Идентификатор issue',
        existing_nullable=True,
        schema='ODS_SOCIAL',
        postgresql_using='git_hub.issue_id::integer',
    )
    op.alter_column(
        'git_hub',
        'user_id',
        existing_type=sa.VARCHAR(),
        type_=sa.Integer(),
        comment='Идентификатор пользователя открывшего issue',
        existing_nullable=True,
        schema='ODS_SOCIAL',
        postgresql_using='git_hub.issue_id::integer',
    )
    op.alter_column(
        'git_hub',
        'repository_id',
        existing_type=sa.VARCHAR(),
        type_=sa.Integer(),
        comment='Идентификатор репозитория',
        existing_nullable=True,
        schema='ODS_SOCIAL',
        postgresql_using='git_hub.issue_id::integer',
    )
    op.alter_column(
        'git_hub',
        'assignee_id',
        existing_type=sa.VARCHAR(),
        type_=sa.Integer(),
        comment='Идентификатор назначенного исполнителем issue',
        existing_nullable=True,
        schema='ODS_SOCIAL',
        postgresql_using='git_hub.issue_id::integer',
    )
    op.alter_column(
        'git_hub',
        'assignee_login',
        existing_type=sa.VARCHAR(),
        type_=sa.Integer(),
        comment='Логин назначенного исполнителем issue',
        existing_nullable=True,
        schema='ODS_SOCIAL',
        postgresql_using='git_hub.issue_id::integer',
    )
    op.alter_column(
        'git_hub',
        'organization_id',
        existing_type=sa.VARCHAR(),
        type_=sa.Integer(),
        nullable=False,
        comment='Идентификатор организации',
        schema='ODS_SOCIAL',
        postgresql_using='git_hub.issue_id::integer',
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
    op.alter_column(
        'union_member',
        'middle_name',
        existing_type=sa.VARCHAR(),
        comment='Отчество пользователя',
        existing_nullable=True,
        schema='STG_UNION_MEMBER',
    )
    op.drop_column('union_member', 'card', schema='STG_UNION_MEMBER')
    op.drop_table('test')


def downgrade():
    op.create_table(
        'test',
        sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column('val', sa.INTEGER(), autoincrement=False, nullable=True),
        sa.PrimaryKeyConstraint('id', name=op.f('test_pkey')),
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
    # При касте integer -> varchar, ручные изменения не нужны
    op.alter_column(
        'git_hub',
        'organization_id',
        existing_type=sa.Integer(),
        type_=sa.VARCHAR(),
        nullable=True,
        comment=None,
        existing_comment='Идентификатор организации',
        schema='ODS_SOCIAL',
    )
    op.alter_column(
        'git_hub',
        'assignee_login',
        existing_type=sa.Integer(),
        type_=sa.VARCHAR(),
        comment=None,
        existing_comment='Логин назначенного исполнителем issue',
        existing_nullable=True,
        schema='ODS_SOCIAL',
    )
    op.alter_column(
        'git_hub',
        'assignee_id',
        existing_type=sa.Integer(),
        type_=sa.VARCHAR(),
        comment=None,
        existing_comment='Идентификатор назначенного исполнителем issue',
        existing_nullable=True,
        schema='ODS_SOCIAL',
    )
    op.alter_column(
        'git_hub',
        'repository_id',
        existing_type=sa.Integer(),
        type_=sa.VARCHAR(),
        comment=None,
        existing_comment='Идентификатор репозитория',
        existing_nullable=True,
        schema='ODS_SOCIAL',
    )
    op.alter_column(
        'git_hub',
        'user_id',
        existing_type=sa.Integer(),
        type_=sa.VARCHAR(),
        comment=None,
        existing_comment='Идентификатор пользователя открывшего issue',
        existing_nullable=True,
        schema='ODS_SOCIAL',
    )
    op.alter_column(
        'git_hub',
        'issue_id',
        existing_type=sa.Integer(),
        type_=sa.VARCHAR(),
        comment=None,
        existing_comment='Идентификатор issue',
        existing_nullable=True,
        schema='ODS_SOCIAL',
    )
    op.create_index(
        op.f('lecturer_ts_idx'), 'lecturer', ['valid_from_dt', 'valid_to_dt'], unique=False, schema='DWH_RATING'
    )
    op.create_table_comment('dm_strike', '\n    Витрина страйки\n    ', existing_comment=None, schema='DM_RENTAL')
    op.alter_column(
        'dm_lecturer_comment_act',
        'mark_freebie_weighted',
        existing_type=sa.Integer(),
        type_=sa.DOUBLE_PRECISION(precision=53),
        existing_comment='Взвешенная халявность преподавателя',
        existing_nullable=False,
        existing_server_default=sa.text("'0'::double precision"),
        schema='DM_RATING',
    )
    op.alter_column(
        'dm_lecturer_comment_act',
        'mark_clarity_weighted',
        existing_type=sa.Integer(),
        type_=sa.DOUBLE_PRECISION(precision=53),
        existing_comment='Взвешенная понятность преподавателя',
        existing_nullable=False,
        existing_server_default=sa.text("'0'::double precision"),
        schema='DM_RATING',
    )
    op.alter_column(
        'dm_lecturer_comment_act',
        'mark_kindness_weighted',
        existing_type=sa.Integer(),
        type_=sa.DOUBLE_PRECISION(precision=53),
        existing_comment='Взвешенная доброта преподавателя',
        existing_nullable=False,
        existing_server_default=sa.text("'0'::double precision"),
        schema='DM_RATING',
    )
    op.alter_column(
        'dm_lecturer_comment_act',
        'mark_weighted',
        existing_type=sa.Integer(),
        type_=sa.DOUBLE_PRECISION(precision=53),
        existing_comment='Взвешенная оценка преподавателя',
        existing_nullable=False,
        existing_server_default=sa.text("'0'::double precision"),
        schema='DM_RATING',
    )
