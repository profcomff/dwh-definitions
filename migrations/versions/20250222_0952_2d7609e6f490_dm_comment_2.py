"""dm_comment_2

Revision ID: 2d7609e6f490
Revises: 41490fd26134
Create Date: 2025-02-22 09:52:54.267898

"""

import os

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '2d7609e6f490'
down_revision = '41490fd26134'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table_schema("DM_RATING")
    op.create_table(
        'dm_lecturer_comment_act',
        sa.Column('comment_api_uuid', sa.Uuid(), nullable=False, comment='Идентифиактор в rating-api'),
        sa.Column('lecturer_api_id', sa.Integer(), nullable=False, comment='Идентифиактор в rating-api'),
        sa.Column('lecturer_full_name', sa.String(), nullable=True, comment='ФИО преподавателя'),
        sa.Column('lecturer_first_name', sa.String(), nullable=True, comment='Имя преподавателя'),
        sa.Column('lecturer_last_name', sa.String(), nullable=True, comment='Фамилия преподавателя'),
        sa.Column('lecturer_middle_name', sa.String(), nullable=True, comment='ОТчество преподавателя'),
        sa.Column('timetable_id', sa.Integer(), nullable=True, comment='Идертификатор в timetable-api'),
        sa.Column('has_timetable_id', sa.Boolean(), nullable=False, comment='Флаг: есть ли преподаватель в расписании'),
        sa.Column('lecturer_subject', sa.String(), nullable=True, comment='Предмет, относящийся к преподавателю'),
        sa.Column('comment_subject', sa.String(), nullable=True, comment='Оцениваемый предмет'),
        sa.Column(
            'comment_shortened_text', sa.String(), nullable=True, comment='Первые 80 символов текста комментария'
        ),
        sa.Column('comment_full_text', sa.String(), nullable=True, comment='Полный текст комментария'),
        sa.Column('comment_create_ts', sa.DateTime(), nullable=True, comment='Timestamp создания комментария, мск'),
        sa.Column('comment_update_ts', sa.DateTime(), nullable=True, comment='Timestamp обновления комментария, мск'),
        sa.Column('comment_mark_kindness', sa.Integer(), nullable=False, comment='Оценка доброты'),
        sa.Column('comment_mark_freebie', sa.Integer(), nullable=False, comment='Оценка халявности'),
        sa.Column('comment_mark_clarity', sa.Integer(), nullable=False, comment='Оценка понятности'),
        sa.Column('comment_review_status', sa.String(), nullable=False, comment='Статус комментария'),
        sa.Column('user_id', sa.Integer(), nullable=True, comment='Идентификатор пользователя из auth-api'),
        sa.Column('user_full_name', sa.String(), nullable=True, comment='Имя пользователя'),
        sa.Column('user_email', sa.String(), nullable=True, comment='Список электронных почт пользователя'),
        schema='DM_RATING',
        comment='\n    Snapshot table that shows sizes for all tables in DWH\n    ',
        info={'sensitive': False},
    )
    op.create_group(
        "test_dwh_dm_rating_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_rating_read"
    )
    op.create_group(
        "test_dwh_dm_rating_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_rating_write"
    )
    op.create_group("test_dwh_dm_rating_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_rating_all")
    op.grant_on_schema(
        "test_dwh_dm_rating_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_rating_read",
        "DM_RATING",
    )
    op.grant_on_schema(
        "test_dwh_dm_rating_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_rating_write",
        "DM_RATING",
    )
    op.grant_on_schema(
        "test_dwh_dm_rating_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_rating_all", "DM_RATING"
    )
    op.grant_on_table(
        "test_dwh_dm_rating_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_rating_read",
        ['SELECT'],
        '"DM_RATING".dm_lecturer_comment_act',
    )
    op.grant_on_table(
        "test_dwh_dm_rating_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_rating_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DM_RATING".dm_lecturer_comment_act',
    )
    op.grant_on_table(
        "test_dwh_dm_rating_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_rating_all",
        ['ALL'],
        '"DM_RATING".dm_lecturer_comment_act',
    )
    op.create_index(
        op.f('ix_DM_RATING_dm_lecturer_comment_act_comment_create_ts'),
        'dm_lecturer_comment_act',
        ['comment_create_ts'],
        unique=False,
        schema='DM_RATING',
    )
    op.create_index(
        op.f('ix_DM_RATING_dm_lecturer_comment_act_user_id'),
        'dm_lecturer_comment_act',
        ['user_id'],
        unique=False,
        schema='DM_RATING',
    )


def downgrade():
    op.drop_index(
        op.f('ix_DM_RATING_dm_lecturer_comment_act_user_id'), table_name='dm_lecturer_comment_act', schema='DM_RATING'
    )
    op.drop_index(
        op.f('ix_DM_RATING_dm_lecturer_comment_act_comment_create_ts'),
        table_name='dm_lecturer_comment_act',
        schema='DM_RATING',
    )
    op.revoke_on_table(
        "test_dwh_dm_rating_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_rating_all",
        ['ALL'],
        '"DM_RATING".dm_lecturer_comment_act',
    )
    op.revoke_on_table(
        "test_dwh_dm_rating_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_rating_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DM_RATING".dm_lecturer_comment_act',
    )
    op.revoke_on_table(
        "test_dwh_dm_rating_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_rating_read",
        ['SELECT'],
        '"DM_RATING".dm_lecturer_comment_act',
    )
    op.revoke_on_schema(
        "test_dwh_dm_rating_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_rating_all", "DM_RATING"
    )
    op.revoke_on_schema(
        "test_dwh_dm_rating_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_rating_write",
        "DM_RATING",
    )
    op.revoke_on_schema(
        "test_dwh_dm_rating_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_rating_read",
        "DM_RATING",
    )
    op.drop_table('dm_lecturer_comment_act', schema='DM_RATING')
    op.delete_group("test_dwh_dm_rating_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_rating_all")
    op.delete_group(
        "test_dwh_dm_rating_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_rating_write"
    )
    op.delete_group(
        "test_dwh_dm_rating_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_rating_read"
    )
    op.drop_table_schema("DM_RATING")
