"""rating-refactor

Revision ID: 059a2a1571f1
Revises: dd8e7cd6c56e
Create Date: 2025-08-17 00:32:15.412638

"""

import os

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = '059a2a1571f1'
down_revision = 'dd8e7cd6c56e'
branch_labels = None
depends_on = None


def upgrade():
    op.create_index('lecturer_ts_idx', 'lecturer', ['valid_from_dt', 'valid_to_dt'], schema="DWH_RATING")
    op.add_column(
        'dm_lecturer_comment_act',
        sa.Column(
            'mark_weighted', sa.Float(), nullable=False, comment='Взвешенная оценка преподавателя', server_default='0.0'
        ),
        schema='DM_RATING',
    )
    op.add_column(
        'dm_lecturer_comment_act',
        sa.Column(
            'mark_kindness_weighted',
            sa.Float(),
            nullable=False,
            comment='Взвешенная доброта преподавателя',
            server_default='0.0',
        ),
        schema='DM_RATING',
    )
    op.add_column(
        'dm_lecturer_comment_act',
        sa.Column(
            'mark_clarity_weighted',
            sa.Float(),
            nullable=False,
            comment='Взвешенная понятность преподавателя',
            server_default='0.0',
        ),
        schema='DM_RATING',
    )
    op.add_column(
        'dm_lecturer_comment_act',
        sa.Column(
            'mark_freebie_weighted',
            sa.Float(),
            nullable=False,
            comment='Взвешенная халявность преподавателя',
            server_default='0.0',
        ),
        schema='DM_RATING',
    )
    op.add_column(
        'dm_lecturer_comment_act',
        sa.Column('rank', sa.Integer(), nullable=False, comment='Место в рейтинге', server_default='0'),
        schema='DM_RATING',
    )
    op.alter_column(
        'dm_lecturer_comment_act',
        'lecturer_middle_name',
        existing_type=sa.VARCHAR(),
        comment='Отчество преподавателя',
        existing_comment='ОТчество преподавателя',
        existing_nullable=True,
        schema='DM_RATING',
    )
    op.add_column(
        'lecturer',
        sa.Column('rank', sa.Integer(), nullable=False, comment='Место в рейтинге', server_default='0'),
        schema='DWH_RATING',
    )
    op.add_column(
        'lecturer',
        sa.Column(
            'mark_weighted', sa.Float(), nullable=False, comment='Взвешенная оценка преподавателя', server_default='0.0'
        ),
        schema='DWH_RATING',
    )
    op.add_column(
        'lecturer',
        sa.Column(
            'mark_kindness_weighted',
            sa.Float(),
            nullable=False,
            comment='Взвешенная доброта преподавателя',
            server_default='0.0',
        ),
        schema='DWH_RATING',
    )
    op.add_column(
        'lecturer',
        sa.Column(
            'mark_clarity_weighted',
            sa.Float(),
            nullable=False,
            comment='Взверешенная понятность преподавателя',
            server_default='0.0',
        ),
        schema='DWH_RATING',
    )
    op.add_column(
        'lecturer',
        sa.Column(
            'mark_freebie_weighted',
            sa.Float(),
            nullable=False,
            comment='Взвешенная халявность преподавателя',
            server_default='0.0',
        ),
        schema='DWH_RATING',
    )
    op.add_column(
        'lecturer',
        sa.Column(
            'mark_weighted',
            sa.Float(),
            nullable=False,
            comment='Взвешенная оценка преподавателя',
            server_default='0.0',
        ),
        schema='ODS_RATING',
    )
    op.add_column(
        'lecturer',
        sa.Column(
            'mark_kindness_weighted',
            sa.Float(),
            server_default='0',
            nullable=False,
            comment='Взвешенная доброта преподавателя',
        ),
        schema='ODS_RATING',
    )
    op.add_column(
        'lecturer',
        sa.Column(
            'mark_clarity_weighted',
            sa.Float(),
            server_default='0',
            nullable=False,
            comment='Взверешенная понятность преподавателя',
        ),
        schema='ODS_RATING',
    )
    op.add_column(
        'lecturer',
        sa.Column(
            'mark_freebie_weighted',
            sa.Float(),
            server_default='0',
            nullable=False,
            comment='Взвешенная халявность преподавателя',
        ),
        schema='ODS_RATING',
    )
    op.add_column(
        'lecturer',
        sa.Column('rank', sa.Integer(), server_default='0', nullable=False, comment='Место в рейтинге'),
        schema='ODS_RATING',
    )
    op.alter_column(
        'lecturer',
        'middle_name',
        existing_type=sa.VARCHAR(),
        comment='Отчество преподавателя',
        existing_comment='отчество преподавателя',
        existing_nullable=False,
        schema='ODS_RATING',
    )
    op.alter_column(
        'academic_group',
        'group',
        existing_type=sa.VARCHAR(),
        comment='Название академической группы',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'academic_group',
        'user_id',
        existing_type=sa.INTEGER(),
        comment='Идентификатор пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'academic_group',
        'source',
        existing_type=sa.VARCHAR(),
        comment='Источник данных',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'academic_group',
        'created',
        existing_type=postgresql.TIMESTAMP(),
        comment='Дата создания записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'academic_group',
        'modified',
        existing_type=postgresql.TIMESTAMP(),
        comment='Дата последнего изменения записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'academic_group',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment='Флаг удаления записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'address',
        'address',
        existing_type=sa.VARCHAR(),
        comment='Адрес проживания пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'address',
        'user_id',
        existing_type=sa.INTEGER(),
        comment='Идентификатор пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'address',
        'source',
        existing_type=sa.VARCHAR(),
        comment='Источник данных',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'address',
        'created',
        existing_type=postgresql.TIMESTAMP(),
        comment='Дата создания записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'address',
        'modified',
        existing_type=postgresql.TIMESTAMP(),
        comment='Дата последнего изменения записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'address',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment='Флаг удаления записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'birth_city',
        'city',
        existing_type=sa.VARCHAR(),
        comment='Название города рождения',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'birth_city',
        'user_id',
        existing_type=sa.INTEGER(),
        comment='Идентификатор пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'birth_city',
        'source',
        existing_type=sa.VARCHAR(),
        comment='Источник данных',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'birth_city',
        'created',
        existing_type=postgresql.TIMESTAMP(),
        comment='Дата создания записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'birth_city',
        'modified',
        existing_type=postgresql.TIMESTAMP(),
        comment='Дата последнего изменения записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'birth_city',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment='Флаг удаления записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'birthday',
        'birthday',
        existing_type=postgresql.TIMESTAMP(),
        comment='Дата рождения пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'birthday',
        'user_id',
        existing_type=sa.INTEGER(),
        comment='Идентификатор пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'birthday',
        'source',
        existing_type=sa.VARCHAR(),
        comment='Источник данных',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'birthday',
        'created',
        existing_type=postgresql.TIMESTAMP(),
        comment='Дата создания записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'birthday',
        'modified',
        existing_type=postgresql.TIMESTAMP(),
        comment='Дата последнего изменения записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'birthday',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment='Флаг удаления записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'city',
        'city',
        existing_type=sa.VARCHAR(),
        comment='Название города проживания',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'city',
        'user_id',
        existing_type=sa.INTEGER(),
        comment='Идентификатор пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'city',
        'source',
        existing_type=sa.VARCHAR(),
        comment='Источник данных',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'city',
        'created',
        existing_type=postgresql.TIMESTAMP(),
        comment='Дата создания записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'city',
        'modified',
        existing_type=postgresql.TIMESTAMP(),
        comment='Дата последнего изменения записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'city',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment='Флаг удаления записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'department',
        'department',
        existing_type=sa.VARCHAR(),
        comment='Название кафедры/отдела',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'department',
        'user_id',
        existing_type=sa.INTEGER(),
        comment='Идентификатор пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'department',
        'source',
        existing_type=sa.VARCHAR(),
        comment='Источник данных',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'department',
        'created',
        existing_type=postgresql.TIMESTAMP(),
        comment='Дата создания записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'department',
        'modified',
        existing_type=postgresql.TIMESTAMP(),
        comment='Дата последнего изменения записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'department',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment='Флаг удаления записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'education_form',
        'form',
        existing_type=sa.VARCHAR(),
        comment='Форма обучения',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'education_form',
        'user_id',
        existing_type=sa.INTEGER(),
        comment='Идентификатор пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'education_form',
        'source',
        existing_type=sa.VARCHAR(),
        comment='Источник данных',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'education_form',
        'created',
        existing_type=postgresql.TIMESTAMP(),
        comment='Дата создания записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'education_form',
        'modified',
        existing_type=postgresql.TIMESTAMP(),
        comment='Дата последнего изменения записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'education_form',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment='Флаг удаления записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'education_level',
        'level',
        existing_type=sa.VARCHAR(),
        comment='Уровень образования',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'education_level',
        'user_id',
        existing_type=sa.INTEGER(),
        comment='Идентификатор пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'education_level',
        'source',
        existing_type=sa.VARCHAR(),
        comment='Источник данных',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'education_level',
        'created',
        existing_type=postgresql.TIMESTAMP(),
        comment='Дата создания записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'education_level',
        'modified',
        existing_type=postgresql.TIMESTAMP(),
        comment='Дата последнего изменения записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'education_level',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment='Флаг удаления записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'email',
        'email',
        existing_type=sa.VARCHAR(),
        comment='Электронная почта пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'email',
        'user_id',
        existing_type=sa.INTEGER(),
        comment='Идентификатор пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'email',
        'source',
        existing_type=sa.VARCHAR(),
        comment='Источник данных',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'email',
        'created',
        existing_type=postgresql.TIMESTAMP(),
        comment='Дата создания записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'email',
        'modified',
        existing_type=postgresql.TIMESTAMP(),
        comment='Дата последнего изменения записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'email',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment='Флаг удаления записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'faculty',
        'faculty',
        existing_type=sa.VARCHAR(),
        comment='Название факультета',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'faculty',
        'user_id',
        existing_type=sa.INTEGER(),
        comment='Идентификатор пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'faculty',
        'source',
        existing_type=sa.VARCHAR(),
        comment='Источник данных',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'faculty',
        'created',
        existing_type=postgresql.TIMESTAMP(),
        comment='Дата создания записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'faculty',
        'modified',
        existing_type=postgresql.TIMESTAMP(),
        comment='Дата последнего изменения записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'faculty',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment='Флаг удаления записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'full_name',
        'name',
        existing_type=sa.VARCHAR(),
        comment='Полное имя пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'full_name',
        'user_id',
        existing_type=sa.INTEGER(),
        comment='Идентификатор пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'full_name',
        'source',
        existing_type=sa.VARCHAR(),
        comment='Источник данных',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'full_name',
        'created',
        existing_type=postgresql.TIMESTAMP(),
        comment='Дата создания записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'full_name',
        'modified',
        existing_type=postgresql.TIMESTAMP(),
        comment='Дата последнего изменения записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'full_name',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment='Флаг удаления записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'home_phone_number',
        'phone_number',
        existing_type=sa.VARCHAR(),
        comment='Домашний номер телефона',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'home_phone_number',
        'user_id',
        existing_type=sa.INTEGER(),
        comment='Идентификатор пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'home_phone_number',
        'source',
        existing_type=sa.VARCHAR(),
        comment='Источник данных',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'home_phone_number',
        'created',
        existing_type=postgresql.TIMESTAMP(),
        comment='Дата создания записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'home_phone_number',
        'modified',
        existing_type=postgresql.TIMESTAMP(),
        comment='Дата последнего изменения записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'home_phone_number',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment='Флаг удаления записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'phone_number',
        'phone_number',
        existing_type=sa.VARCHAR(),
        comment='Номер телефона пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'phone_number',
        'user_id',
        existing_type=sa.INTEGER(),
        comment='Идентификатор пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'phone_number',
        'source',
        existing_type=sa.VARCHAR(),
        comment='Источник данных',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'phone_number',
        'created',
        existing_type=postgresql.TIMESTAMP(),
        comment='Дата создания записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'phone_number',
        'modified',
        existing_type=postgresql.TIMESTAMP(),
        comment='Дата последнего изменения записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'phone_number',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment='Флаг удаления записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'photo',
        'url',
        existing_type=sa.VARCHAR(),
        comment='URL фотографии пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'photo',
        'user_id',
        existing_type=sa.INTEGER(),
        comment='Идентификатор пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'photo',
        'source',
        existing_type=sa.VARCHAR(),
        comment='Источник данных',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'photo',
        'created',
        existing_type=postgresql.TIMESTAMP(),
        comment='Дата создания записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'photo',
        'modified',
        existing_type=postgresql.TIMESTAMP(),
        comment='Дата последнего изменения записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'photo',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment='Флаг удаления записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'position',
        'position',
        existing_type=sa.VARCHAR(),
        comment='Должность пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'position',
        'user_id',
        existing_type=sa.INTEGER(),
        comment='Идентификатор пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'position',
        'source',
        existing_type=sa.VARCHAR(),
        comment='Источник данных',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'position',
        'created',
        existing_type=postgresql.TIMESTAMP(),
        comment='Дата создания записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'position',
        'modified',
        existing_type=postgresql.TIMESTAMP(),
        comment='Дата последнего изменения записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'position',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment='Флаг удаления записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'sex',
        'gender',
        existing_type=sa.VARCHAR(),
        comment='Пол пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'sex',
        'user_id',
        existing_type=sa.INTEGER(),
        comment='Идентификатор пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'sex',
        'source',
        existing_type=sa.VARCHAR(),
        comment='Источник данных',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'sex',
        'created',
        existing_type=postgresql.TIMESTAMP(),
        comment='Дата создания записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'sex',
        'modified',
        existing_type=postgresql.TIMESTAMP(),
        comment='Дата последнего изменения записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'sex',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment='Флаг удаления записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'student_id',
        'student_id',
        existing_type=sa.VARCHAR(),
        comment='Студенческий билет',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'student_id',
        'user_id',
        existing_type=sa.INTEGER(),
        comment='Идентификатор пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'student_id',
        'source',
        existing_type=sa.VARCHAR(),
        comment='Источник данных',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'student_id',
        'created',
        existing_type=postgresql.TIMESTAMP(),
        comment='Дата создания записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'student_id',
        'modified',
        existing_type=postgresql.TIMESTAMP(),
        comment='Дата последнего изменения записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'student_id',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment='Флаг удаления записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'telegram_username',
        'username',
        existing_type=sa.VARCHAR(),
        comment='Имя пользователя Telegram',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'telegram_username',
        'user_id',
        existing_type=sa.INTEGER(),
        comment='Идентификатор пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'telegram_username',
        'source',
        existing_type=sa.VARCHAR(),
        comment='Источник данных',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'telegram_username',
        'created',
        existing_type=postgresql.TIMESTAMP(),
        comment='Дата создания записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'telegram_username',
        'modified',
        existing_type=postgresql.TIMESTAMP(),
        comment='Дата последнего изменения записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'telegram_username',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment='Флаг удаления записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'university',
        'university',
        existing_type=sa.VARCHAR(),
        comment='Название университета',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'university',
        'user_id',
        existing_type=sa.INTEGER(),
        comment='Идентификатор пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'university',
        'source',
        existing_type=sa.VARCHAR(),
        comment='Источник данных',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'university',
        'created',
        existing_type=postgresql.TIMESTAMP(),
        comment='Дата создания записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'university',
        'modified',
        existing_type=postgresql.TIMESTAMP(),
        comment='Дата последнего изменения записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'university',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment='Флаг удаления записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'vk_username',
        'username',
        existing_type=sa.VARCHAR(),
        comment='Имя пользователя ВКонтакте',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'vk_username',
        'user_id',
        existing_type=sa.INTEGER(),
        comment='Идентификатор пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'vk_username',
        'source',
        existing_type=sa.VARCHAR(),
        comment='Источник данных',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'vk_username',
        'created',
        existing_type=postgresql.TIMESTAMP(),
        comment='Дата создания записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'vk_username',
        'modified',
        existing_type=postgresql.TIMESTAMP(),
        comment='Дата последнего изменения записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'vk_username',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment='Флаг удаления записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'workplace',
        'workplace',
        existing_type=sa.VARCHAR(),
        comment='Место работы пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'workplace',
        'user_id',
        existing_type=sa.INTEGER(),
        comment='Идентификатор пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'workplace',
        'source',
        existing_type=sa.VARCHAR(),
        comment='Источник данных',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'workplace',
        'created',
        existing_type=postgresql.TIMESTAMP(),
        comment='Дата создания записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'workplace',
        'modified',
        existing_type=postgresql.TIMESTAMP(),
        comment='Дата последнего изменения записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'workplace',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment='Флаг удаления записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'workplace_address',
        'address',
        existing_type=sa.VARCHAR(),
        comment='Адрес места работы',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'workplace_address',
        'user_id',
        existing_type=sa.INTEGER(),
        comment='Идентификатор пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'workplace_address',
        'source',
        existing_type=sa.VARCHAR(),
        comment='Источник данных',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'workplace_address',
        'created',
        existing_type=postgresql.TIMESTAMP(),
        comment='Дата создания записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'workplace_address',
        'modified',
        existing_type=postgresql.TIMESTAMP(),
        comment='Дата последнего изменения записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'workplace_address',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment='Флаг удаления записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'category',
        'id',
        existing_type=sa.INTEGER(),
        comment='Идентификатор категории',
        existing_nullable=False,
        autoincrement=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'category',
        'name',
        existing_type=sa.VARCHAR(),
        comment='Название категории',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'category',
        'read_scope',
        existing_type=sa.VARCHAR(),
        comment='Область видимости для чтения',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'category',
        'update_scope',
        existing_type=sa.VARCHAR(),
        comment='Область видимости для обновления',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'category',
        'create_ts',
        existing_type=postgresql.TIMESTAMP(),
        comment='Время создания записи',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'category',
        'modify_ts',
        existing_type=postgresql.TIMESTAMP(),
        comment='Время последнего изменения записи',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'category',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment='Флаг удаления записи',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'encrypted_info',
        'id',
        existing_type=sa.INTEGER(),
        comment='Идентификатор зашифрованной записи',
        existing_nullable=False,
        autoincrement=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'encrypted_info',
        'param_id',
        existing_type=sa.INTEGER(),
        comment='Идентификатор параметра',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'encrypted_info',
        'source_id',
        existing_type=sa.INTEGER(),
        comment='Идентификатор источника данных',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'encrypted_info',
        'owner_id',
        existing_type=sa.INTEGER(),
        comment='Идентификатор владельца данных',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'encrypted_info',
        'value',
        existing_type=postgresql.BYTEA(),
        comment='Зашифрованное значение параметра',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'encrypted_info',
        'create_ts',
        existing_type=postgresql.TIMESTAMP(),
        comment='Время создания записи',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'encrypted_info',
        'modify_ts',
        existing_type=postgresql.TIMESTAMP(),
        comment='Время последнего изменения записи',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'encrypted_info',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment='Флаг удаления записи',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'info',
        'id',
        existing_type=sa.INTEGER(),
        comment='Идентификатор информационной записи',
        existing_nullable=False,
        autoincrement=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'info',
        'param_id',
        existing_type=sa.INTEGER(),
        comment='Идентификатор параметра',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'info',
        'source_id',
        existing_type=sa.INTEGER(),
        comment='Идентификатор источника данных',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'info',
        'owner_id',
        existing_type=sa.INTEGER(),
        comment='Идентификатор владельца данных',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'info',
        'value',
        existing_type=sa.VARCHAR(),
        comment='Значение параметра',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'info',
        'create_ts',
        existing_type=postgresql.TIMESTAMP(),
        comment='Время создания записи',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'info',
        'modify_ts',
        existing_type=postgresql.TIMESTAMP(),
        comment='Время последнего изменения записи',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'info',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment='Флаг удаления записи',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'info_keys',
        'id',
        existing_type=sa.INTEGER(),
        comment='Идентификатор ключа шифрования',
        existing_comment='key id (maps to)',
        existing_nullable=False,
        autoincrement=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'info_keys',
        'key',
        existing_type=sa.VARCHAR(),
        comment='Симметричный ключ шифрования',
        existing_comment='symmetric encryption key',
        existing_nullable=False,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'param',
        'id',
        existing_type=sa.INTEGER(),
        comment='Идентификатор параметра',
        existing_nullable=False,
        autoincrement=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'param',
        'visible_in_user_response',
        existing_type=sa.BOOLEAN(),
        comment='Видимость параметра в ответе пользователю',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'param',
        'name',
        existing_type=sa.VARCHAR(),
        comment='Название параметра',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'param',
        'category_id',
        existing_type=sa.INTEGER(),
        comment='Идентификатор категории',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'param',
        'is_required',
        existing_type=sa.BOOLEAN(),
        comment='Является ли параметр обязательным',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'param',
        'changeable',
        existing_type=sa.BOOLEAN(),
        comment='Может ли параметр быть изменен',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'param',
        'type',
        existing_type=sa.VARCHAR(),
        comment='Тип данных параметра',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'param',
        'create_ts',
        existing_type=postgresql.TIMESTAMP(),
        comment='Время создания записи',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'param',
        'modify_ts',
        existing_type=postgresql.TIMESTAMP(),
        comment='Время последнего изменения записи',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'param',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment='Флаг удаления записи',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'param',
        'is_public',
        existing_type=sa.BOOLEAN(),
        comment='Является ли параметр публичным',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'param',
        'validation',
        existing_type=sa.VARCHAR(),
        comment='Правила валидации параметра',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'source',
        'id',
        existing_type=sa.INTEGER(),
        comment='Идентификатор источника данных',
        existing_nullable=False,
        autoincrement=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'source',
        'name',
        existing_type=sa.VARCHAR(),
        comment='Название источника данных',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'source',
        'trust_level',
        existing_type=sa.INTEGER(),
        comment='Уровень доверия к источнику',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'source',
        'create_ts',
        existing_type=postgresql.TIMESTAMP(),
        comment='Время создания записи',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'source',
        'modify_ts',
        existing_type=postgresql.TIMESTAMP(),
        comment='Время последнего изменения записи',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'source',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment='Флаг удаления записи',
        existing_nullable=True,
        schema='STG_USERDATA',
    )


def downgrade():
    op.alter_column(
        'source',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment=None,
        existing_comment='Флаг удаления записи',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'source',
        'modify_ts',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Время последнего изменения записи',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'source',
        'create_ts',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Время создания записи',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'source',
        'trust_level',
        existing_type=sa.INTEGER(),
        comment=None,
        existing_comment='Уровень доверия к источнику',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'source',
        'name',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Название источника данных',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'source',
        'id',
        existing_type=sa.INTEGER(),
        comment=None,
        existing_comment='Идентификатор источника данных',
        existing_nullable=False,
        autoincrement=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'param',
        'validation',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Правила валидации параметра',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'param',
        'is_public',
        existing_type=sa.BOOLEAN(),
        comment=None,
        existing_comment='Является ли параметр публичным',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'param',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment=None,
        existing_comment='Флаг удаления записи',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'param',
        'modify_ts',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Время последнего изменения записи',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'param',
        'create_ts',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Время создания записи',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'param',
        'type',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Тип данных параметра',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'param',
        'changeable',
        existing_type=sa.BOOLEAN(),
        comment=None,
        existing_comment='Может ли параметр быть изменен',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'param',
        'is_required',
        existing_type=sa.BOOLEAN(),
        comment=None,
        existing_comment='Является ли параметр обязательным',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'param',
        'category_id',
        existing_type=sa.INTEGER(),
        comment=None,
        existing_comment='Идентификатор категории',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'param',
        'name',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Название параметра',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'param',
        'visible_in_user_response',
        existing_type=sa.BOOLEAN(),
        comment=None,
        existing_comment='Видимость параметра в ответе пользователю',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'param',
        'id',
        existing_type=sa.INTEGER(),
        comment=None,
        existing_comment='Идентификатор параметра',
        existing_nullable=False,
        autoincrement=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'info_keys',
        'key',
        existing_type=sa.VARCHAR(),
        comment='symmetric encryption key',
        existing_comment='Симметричный ключ шифрования',
        existing_nullable=False,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'info_keys',
        'id',
        existing_type=sa.INTEGER(),
        comment='key id (maps to)',
        existing_comment='Идентификатор ключа шифрования',
        existing_nullable=False,
        autoincrement=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'info',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment=None,
        existing_comment='Флаг удаления записи',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'info',
        'modify_ts',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Время последнего изменения записи',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'info',
        'create_ts',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Время создания записи',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'info',
        'value',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Значение параметра',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'info',
        'owner_id',
        existing_type=sa.INTEGER(),
        comment=None,
        existing_comment='Идентификатор владельца данных',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'info',
        'source_id',
        existing_type=sa.INTEGER(),
        comment=None,
        existing_comment='Идентификатор источника данных',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'info',
        'param_id',
        existing_type=sa.INTEGER(),
        comment=None,
        existing_comment='Идентификатор параметра',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'info',
        'id',
        existing_type=sa.INTEGER(),
        comment=None,
        existing_comment='Идентификатор информационной записи',
        existing_nullable=False,
        autoincrement=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'encrypted_info',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment=None,
        existing_comment='Флаг удаления записи',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'encrypted_info',
        'modify_ts',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Время последнего изменения записи',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'encrypted_info',
        'create_ts',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Время создания записи',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'encrypted_info',
        'value',
        existing_type=postgresql.BYTEA(),
        comment=None,
        existing_comment='Зашифрованное значение параметра',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'encrypted_info',
        'owner_id',
        existing_type=sa.INTEGER(),
        comment=None,
        existing_comment='Идентификатор владельца данных',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'encrypted_info',
        'source_id',
        existing_type=sa.INTEGER(),
        comment=None,
        existing_comment='Идентификатор источника данных',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'encrypted_info',
        'param_id',
        existing_type=sa.INTEGER(),
        comment=None,
        existing_comment='Идентификатор параметра',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'encrypted_info',
        'id',
        existing_type=sa.INTEGER(),
        comment=None,
        existing_comment='Идентификатор зашифрованной записи',
        existing_nullable=False,
        autoincrement=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'category',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment=None,
        existing_comment='Флаг удаления записи',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'category',
        'modify_ts',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Время последнего изменения записи',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'category',
        'create_ts',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Время создания записи',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'category',
        'update_scope',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Область видимости для обновления',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'category',
        'read_scope',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Область видимости для чтения',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'category',
        'name',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Название категории',
        existing_nullable=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'category',
        'id',
        existing_type=sa.INTEGER(),
        comment=None,
        existing_comment='Идентификатор категории',
        existing_nullable=False,
        autoincrement=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'workplace_address',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment=None,
        existing_comment='Флаг удаления записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'workplace_address',
        'modified',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Дата последнего изменения записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'workplace_address',
        'created',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Дата создания записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'workplace_address',
        'source',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Источник данных',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'workplace_address',
        'user_id',
        existing_type=sa.INTEGER(),
        comment=None,
        existing_comment='Идентификатор пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'workplace_address',
        'address',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Адрес места работы',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'workplace',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment=None,
        existing_comment='Флаг удаления записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'workplace',
        'modified',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Дата последнего изменения записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'workplace',
        'created',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Дата создания записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'workplace',
        'source',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Источник данных',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'workplace',
        'user_id',
        existing_type=sa.INTEGER(),
        comment=None,
        existing_comment='Идентификатор пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'workplace',
        'workplace',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Место работы пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'vk_username',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment=None,
        existing_comment='Флаг удаления записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'vk_username',
        'modified',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Дата последнего изменения записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'vk_username',
        'created',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Дата создания записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'vk_username',
        'source',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Источник данных',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'vk_username',
        'user_id',
        existing_type=sa.INTEGER(),
        comment=None,
        existing_comment='Идентификатор пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'vk_username',
        'username',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Имя пользователя ВКонтакте',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'university',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment=None,
        existing_comment='Флаг удаления записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'university',
        'modified',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Дата последнего изменения записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'university',
        'created',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Дата создания записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'university',
        'source',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Источник данных',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'university',
        'user_id',
        existing_type=sa.INTEGER(),
        comment=None,
        existing_comment='Идентификатор пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'university',
        'university',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Название университета',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'telegram_username',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment=None,
        existing_comment='Флаг удаления записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'telegram_username',
        'modified',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Дата последнего изменения записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'telegram_username',
        'created',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Дата создания записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'telegram_username',
        'source',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Источник данных',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'telegram_username',
        'user_id',
        existing_type=sa.INTEGER(),
        comment=None,
        existing_comment='Идентификатор пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'telegram_username',
        'username',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Имя пользователя Telegram',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'student_id',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment=None,
        existing_comment='Флаг удаления записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'student_id',
        'modified',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Дата последнего изменения записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'student_id',
        'created',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Дата создания записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'student_id',
        'source',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Источник данных',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'student_id',
        'user_id',
        existing_type=sa.INTEGER(),
        comment=None,
        existing_comment='Идентификатор пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'student_id',
        'student_id',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Студенческий билет',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'sex',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment=None,
        existing_comment='Флаг удаления записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'sex',
        'modified',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Дата последнего изменения записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'sex',
        'created',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Дата создания записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'sex',
        'source',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Источник данных',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'sex',
        'user_id',
        existing_type=sa.INTEGER(),
        comment=None,
        existing_comment='Идентификатор пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'sex',
        'gender',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Пол пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'position',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment=None,
        existing_comment='Флаг удаления записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'position',
        'modified',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Дата последнего изменения записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'position',
        'created',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Дата создания записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'position',
        'source',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Источник данных',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'position',
        'user_id',
        existing_type=sa.INTEGER(),
        comment=None,
        existing_comment='Идентификатор пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'position',
        'position',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Должность пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'photo',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment=None,
        existing_comment='Флаг удаления записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'photo',
        'modified',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Дата последнего изменения записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'photo',
        'created',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Дата создания записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'photo',
        'source',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Источник данных',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'photo',
        'user_id',
        existing_type=sa.INTEGER(),
        comment=None,
        existing_comment='Идентификатор пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'photo',
        'url',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='URL фотографии пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'phone_number',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment=None,
        existing_comment='Флаг удаления записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'phone_number',
        'modified',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Дата последнего изменения записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'phone_number',
        'created',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Дата создания записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'phone_number',
        'source',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Источник данных',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'phone_number',
        'user_id',
        existing_type=sa.INTEGER(),
        comment=None,
        existing_comment='Идентификатор пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'phone_number',
        'phone_number',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Номер телефона пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'home_phone_number',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment=None,
        existing_comment='Флаг удаления записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'home_phone_number',
        'modified',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Дата последнего изменения записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'home_phone_number',
        'created',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Дата создания записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'home_phone_number',
        'source',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Источник данных',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'home_phone_number',
        'user_id',
        existing_type=sa.INTEGER(),
        comment=None,
        existing_comment='Идентификатор пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'home_phone_number',
        'phone_number',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Домашний номер телефона',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'full_name',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment=None,
        existing_comment='Флаг удаления записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'full_name',
        'modified',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Дата последнего изменения записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'full_name',
        'created',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Дата создания записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'full_name',
        'source',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Источник данных',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'full_name',
        'user_id',
        existing_type=sa.INTEGER(),
        comment=None,
        existing_comment='Идентификатор пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'full_name',
        'name',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Полное имя пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'faculty',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment=None,
        existing_comment='Флаг удаления записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'faculty',
        'modified',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Дата последнего изменения записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'faculty',
        'created',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Дата создания записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'faculty',
        'source',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Источник данных',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'faculty',
        'user_id',
        existing_type=sa.INTEGER(),
        comment=None,
        existing_comment='Идентификатор пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'faculty',
        'faculty',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Название факультета',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'email',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment=None,
        existing_comment='Флаг удаления записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'email',
        'modified',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Дата последнего изменения записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'email',
        'created',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Дата создания записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'email',
        'source',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Источник данных',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'email',
        'user_id',
        existing_type=sa.INTEGER(),
        comment=None,
        existing_comment='Идентификатор пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'email',
        'email',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Электронная почта пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'education_level',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment=None,
        existing_comment='Флаг удаления записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'education_level',
        'modified',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Дата последнего изменения записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'education_level',
        'created',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Дата создания записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'education_level',
        'source',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Источник данных',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'education_level',
        'user_id',
        existing_type=sa.INTEGER(),
        comment=None,
        existing_comment='Идентификатор пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'education_level',
        'level',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Уровень образования',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'education_form',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment=None,
        existing_comment='Флаг удаления записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'education_form',
        'modified',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Дата последнего изменения записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'education_form',
        'created',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Дата создания записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'education_form',
        'source',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Источник данных',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'education_form',
        'user_id',
        existing_type=sa.INTEGER(),
        comment=None,
        existing_comment='Идентификатор пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'education_form',
        'form',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Форма обучения',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'department',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment=None,
        existing_comment='Флаг удаления записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'department',
        'modified',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Дата последнего изменения записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'department',
        'created',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Дата создания записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'department',
        'source',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Источник данных',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'department',
        'user_id',
        existing_type=sa.INTEGER(),
        comment=None,
        existing_comment='Идентификатор пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'department',
        'department',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Название кафедры/отдела',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'city',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment=None,
        existing_comment='Флаг удаления записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'city',
        'modified',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Дата последнего изменения записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'city',
        'created',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Дата создания записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'city',
        'source',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Источник данных',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'city',
        'user_id',
        existing_type=sa.INTEGER(),
        comment=None,
        existing_comment='Идентификатор пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'city',
        'city',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Название города проживания',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'birthday',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment=None,
        existing_comment='Флаг удаления записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'birthday',
        'modified',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Дата последнего изменения записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'birthday',
        'created',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Дата создания записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'birthday',
        'source',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Источник данных',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'birthday',
        'user_id',
        existing_type=sa.INTEGER(),
        comment=None,
        existing_comment='Идентификатор пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'birthday',
        'birthday',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Дата рождения пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'birth_city',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment=None,
        existing_comment='Флаг удаления записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'birth_city',
        'modified',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Дата последнего изменения записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'birth_city',
        'created',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Дата создания записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'birth_city',
        'source',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Источник данных',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'birth_city',
        'user_id',
        existing_type=sa.INTEGER(),
        comment=None,
        existing_comment='Идентификатор пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'birth_city',
        'city',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Название города рождения',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'address',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment=None,
        existing_comment='Флаг удаления записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'address',
        'modified',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Дата последнего изменения записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'address',
        'created',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Дата создания записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'address',
        'source',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Источник данных',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'address',
        'user_id',
        existing_type=sa.INTEGER(),
        comment=None,
        existing_comment='Идентификатор пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'address',
        'address',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Адрес проживания пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'academic_group',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment=None,
        existing_comment='Флаг удаления записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'academic_group',
        'modified',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Дата последнего изменения записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'academic_group',
        'created',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Дата создания записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'academic_group',
        'source',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Источник данных',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'academic_group',
        'user_id',
        existing_type=sa.INTEGER(),
        comment=None,
        existing_comment='Идентификатор пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'academic_group',
        'group',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Название академической группы',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'lecturer',
        'middle_name',
        existing_type=sa.VARCHAR(),
        comment='отчество преподавателя',
        existing_comment='Отчество преподавателя',
        existing_nullable=False,
        schema='ODS_RATING',
    )
    op.drop_column('lecturer', 'rank', schema='ODS_RATING')
    op.drop_column('lecturer', 'mark_freebie_weighted', schema='ODS_RATING')
    op.drop_column('lecturer', 'mark_clarity_weighted', schema='ODS_RATING')
    op.drop_column('lecturer', 'mark_kindness_weighted', schema='ODS_RATING')
    op.drop_column('lecturer', 'mark_weighted', schema='ODS_RATING')
    op.drop_column('lecturer', 'mark_freebie_weighted', schema='DWH_RATING')
    op.drop_column('lecturer', 'mark_clarity_weighted', schema='DWH_RATING')
    op.drop_column('lecturer', 'mark_kindness_weighted', schema='DWH_RATING')
    op.drop_column('lecturer', 'mark_weighted', schema='DWH_RATING')
    op.drop_column('lecturer', 'rank', schema='DWH_RATING')
    op.alter_column(
        'dm_lecturer_comment_act',
        'lecturer_middle_name',
        existing_type=sa.VARCHAR(),
        comment='ОТчество преподавателя',
        existing_comment='Отчество преподавателя',
        existing_nullable=True,
        schema='DM_RATING',
    )
    op.drop_column('dm_lecturer_comment_act', 'rank', schema='DM_RATING')
    op.drop_column('dm_lecturer_comment_act', 'mark_freebie_weighted', schema='DM_RATING')
    op.drop_column('dm_lecturer_comment_act', 'mark_clarity_weighted', schema='DM_RATING')
    op.drop_column('dm_lecturer_comment_act', 'mark_kindness_weighted', schema='DM_RATING')
    op.drop_column('dm_lecturer_comment_act', 'mark_weighted', schema='DM_RATING')
    op.drop_index('lecturer_ts_idx', 'lecturer', schema="DWH_RATING")
