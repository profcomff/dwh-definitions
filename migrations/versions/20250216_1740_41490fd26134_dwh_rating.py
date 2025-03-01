"""dwh_rating

Revision ID: 41490fd26134
Revises: 8a7cb1960f13
Create Date: 2025-02-16 17:40:38.011446

"""

import os

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '41490fd26134'
down_revision = '8a7cb1960f13'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table_schema("DWH_RATING")
    op.create_table(
        'comment',
        sa.Column('uuid', sa.Uuid(), nullable=False, comment='Техническое поле в dwh'),
        sa.Column('api_uuid', sa.Uuid(), nullable=False, comment='Идентифиактор в rating-api'),
        sa.Column('create_ts', sa.DateTime(), nullable=False, comment='Timestamp создания комментария, мск'),
        sa.Column('update_ts', sa.DateTime(), nullable=False, comment='Timestamp обновления комментария, мск'),
        sa.Column('subject', sa.String(), nullable=True, comment='Предмет, к которому относится комментарий'),
        sa.Column('text', sa.String(), nullable=True, comment='Текст комментария'),
        sa.Column('mark_kindness', sa.Integer(), nullable=False, comment='Доброта преподавателя'),
        sa.Column('mark_freebie', sa.Integer(), nullable=False, comment='Халявность преподавателя'),
        sa.Column('mark_clarity', sa.Integer(), nullable=False, comment='Понятность преподавателя'),
        sa.Column('lecturer_id', sa.Integer(), nullable=False, comment='Идертификатор преподавателя'),
        sa.Column(
            'review_status',
            sa.String(),
            nullable=False,
            comment='Статус комментария, может быть approved, pending, dismissed',
        ),
        sa.Column('valid_from_dt', sa.Date(), nullable=True, comment='Дата начала действия записи'),
        sa.Column('valid_to_dt', sa.Date(), nullable=True, comment='Дата конца действия записи'),
        sa.PrimaryKeyConstraint('uuid'),
        schema='DWH_RATING',
        comment='\n    Комментарии в rating-api\n    ',
        info={'sensitive': False},
    )
    op.create_table(
        'lecturer',
        sa.Column('uuid', sa.Uuid(), nullable=False, comment='Техническое поле в dwh'),
        sa.Column('api_id', sa.Integer(), nullable=False, comment='Идентифиактор в rating-api'),
        sa.Column('first_name', sa.String(), nullable=False, comment='Имя преподавателя'),
        sa.Column('last_name', sa.String(), nullable=False, comment='Фамилия преподавателя'),
        sa.Column('middle_name', sa.String(), nullable=False, comment='отчество преподавателя'),
        sa.Column('subject', sa.String(), nullable=True, comment='Список предметов преподавателя'),
        sa.Column('avatar_link', sa.String(), nullable=True, comment='Ссылка на аватар преподавателя'),
        sa.Column('timetable_id', sa.Integer(), nullable=False, comment='Идертификатор в timetable-api'),
        sa.Column('valid_from_dt', sa.Date(), nullable=True, comment='Дата начала действия записи'),
        sa.Column('valid_to_dt', sa.Date(), nullable=True, comment='Дата конца действия записи'),
        sa.PrimaryKeyConstraint('uuid'),
        schema='DWH_RATING',
        comment='\n    Преподаватели в rating-api\n    ',
        info={'sensitive': False},
    )
    op.create_table(
        'lecturer_user_comment',
        sa.Column('uuid', sa.Uuid(), nullable=False, comment='Техническое поле в dwh'),
        sa.Column('api_id', sa.Integer(), nullable=False, comment='Идентифиактор в rating-api'),
        sa.Column('lecturer_id', sa.Integer(), nullable=False, comment='Идентифиактор преподавателя'),
        sa.Column('user_id', sa.Integer(), nullable=False, comment='Идентификатор пользователя в auth-api'),
        sa.Column('create_ts', sa.DateTime(), nullable=False, comment='Timestamp создания комментария, мск'),
        sa.Column('update_ts', sa.DateTime(), nullable=False, comment='Timestamp обновления комментария, мск'),
        sa.Column('valid_from_dt', sa.Date(), nullable=True, comment='Дата начала действия записи'),
        sa.Column('valid_to_dt', sa.Date(), nullable=True, comment='Дата конца действия записи'),
        sa.PrimaryKeyConstraint('uuid'),
        schema='DWH_RATING',
        comment='\n    Связь лекторов и комметариев в rating-api\n    ',
        info={'sensitive': False},
    )
    op.create_group(
        "test_dwh_dwh_rating_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rating_read"
    )
    op.create_group(
        "test_dwh_dwh_rating_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rating_write"
    )
    op.create_group(
        "test_dwh_dwh_rating_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rating_all"
    )
    op.grant_on_schema(
        "test_dwh_dwh_rating_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rating_read",
        "DWH_RATING",
    )
    op.grant_on_schema(
        "test_dwh_dwh_rating_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rating_write",
        "DWH_RATING",
    )
    op.grant_on_schema(
        "test_dwh_dwh_rating_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rating_all",
        "DWH_RATING",
    )
    op.grant_on_table(
        "test_dwh_dwh_rating_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rating_read",
        ['SELECT'],
        '"DWH_RATING".comment',
    )
    op.grant_on_table(
        "test_dwh_dwh_rating_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rating_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DWH_RATING".comment',
    )
    op.grant_on_table(
        "test_dwh_dwh_rating_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rating_all",
        ['ALL'],
        '"DWH_RATING".comment',
    )
    op.grant_on_table(
        "test_dwh_dwh_rating_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rating_read",
        ['SELECT'],
        '"DWH_RATING".lecturer_user_comment',
    )
    op.grant_on_table(
        "test_dwh_dwh_rating_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rating_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DWH_RATING".lecturer_user_comment',
    )
    op.grant_on_table(
        "test_dwh_dwh_rating_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rating_all",
        ['ALL'],
        '"DWH_RATING".lecturer_user_comment',
    )
    op.grant_on_table(
        "test_dwh_dwh_rating_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rating_read",
        ['SELECT'],
        '"DWH_RATING".lecturer',
    )
    op.grant_on_table(
        "test_dwh_dwh_rating_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rating_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DWH_RATING".lecturer',
    )
    op.grant_on_table(
        "test_dwh_dwh_rating_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rating_all",
        ['ALL'],
        '"DWH_RATING".lecturer',
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.revoke_on_table(
        "test_dwh_dwh_rating_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rating_all",
        ['ALL'],
        '"DWH_RATING".lecturer',
    )
    op.revoke_on_table(
        "test_dwh_dwh_rating_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rating_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DWH_RATING".lecturer',
    )
    op.revoke_on_table(
        "test_dwh_dwh_rating_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rating_read",
        ['SELECT'],
        '"DWH_RATING".lecturer',
    )
    op.revoke_on_table(
        "test_dwh_dwh_rating_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rating_all",
        ['ALL'],
        '"DWH_RATING".lecturer_user_comment',
    )
    op.revoke_on_table(
        "test_dwh_dwh_rating_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rating_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DWH_RATING".lecturer_user_comment',
    )
    op.revoke_on_table(
        "test_dwh_dwh_rating_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rating_read",
        ['SELECT'],
        '"DWH_RATING".lecturer_user_comment',
    )
    op.revoke_on_table(
        "test_dwh_dwh_rating_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rating_all",
        ['ALL'],
        '"DWH_RATING".comment',
    )
    op.revoke_on_table(
        "test_dwh_dwh_rating_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rating_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DWH_RATING".comment',
    )
    op.revoke_on_table(
        "test_dwh_dwh_rating_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rating_read",
        ['SELECT'],
        '"DWH_RATING".comment',
    )
    op.revoke_on_schema(
        "test_dwh_dwh_rating_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rating_all",
        "DWH_RATING",
    )
    op.revoke_on_schema(
        "test_dwh_dwh_rating_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rating_write",
        "DWH_RATING",
    )
    op.revoke_on_schema(
        "test_dwh_dwh_rating_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rating_read",
        "DWH_RATING",
    )
    op.drop_table('lecturer_user_comment', schema='DWH_RATING')
    op.drop_table('lecturer', schema='DWH_RATING')
    op.drop_table('comment', schema='DWH_RATING')
    op.delete_group(
        "test_dwh_dwh_rating_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rating_all"
    )
    op.delete_group(
        "test_dwh_dwh_rating_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rating_write"
    )
    op.delete_group(
        "test_dwh_dwh_rating_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rating_read"
    )
    op.drop_table_schema("DWH_RATING")
