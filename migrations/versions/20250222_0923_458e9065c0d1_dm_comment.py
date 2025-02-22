"""dm_comment

Revision ID: 458e9065c0d1
Revises: 41490fd26134
Create Date: 2025-02-22 09:23:35.334508

"""

from alembic import op
import sqlalchemy as sa
import os


# revision identifiers, used by Alembic.
revision = '458e9065c0d1'
down_revision = '41490fd26134'
branch_labels = None
depends_on = None


def upgrade():
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
    )
    op.execute(
        """
        CREATE INDEX "ix__dm_lecturer_comment_act__comment_shortened_text" 
        ON "dm_lecturer_comment_act" 
        USING gin(to_tsvector('russian', "comment_shortened_text"));
        """
    )
    op.execute(
        """
        CREATE INDEX "ix__dm_lecturer_comment_act__lecturer_full_name" 
        ON "dm_lecturer_comment_act" 
        USING gin(to_tsvector('russian', "lecturer_full_name"));
        """
    )
    op.execute(
        """
        CREATE INDEX "ix__dm_lecturer_comment_act__user_full_name" 
        ON "dm_lecturer_comment_act" 
        USING gin(to_tsvector('russian', "user_full_name"));
        """
    )
    op.create_index(
        op.f('ix_dm_lecturer_comment_act_comment_create_ts'),
        'dm_lecturer_comment_act',
        ['comment_create_ts'],
        unique=False,
    )
    op.create_index(op.f('ix_dm_lecturer_comment_act_user_id'), 'dm_lecturer_comment_act', ['user_id'], unique=False)


def downgrade():
    op.drop_index(op.f('ix_dm_lecturer_comment_act_user_id'), table_name='dm_lecturer_comment_act')
    op.drop_index(op.f('ix_dm_lecturer_comment_act_comment_create_ts'), table_name='dm_lecturer_comment_act')
    op.drop_index(
        'ix__dm_lecturer_comment_act__user_full_name', table_name='dm_lecturer_comment_act', postgresql_using='gin'
    )
    op.drop_index(
        'ix__dm_lecturer_comment_act__lecturer_full_name', table_name='dm_lecturer_comment_act', postgresql_using='gin'
    )
    op.drop_index(
        'ix__dm_lecturer_comment_act__comment_shortened_text',
        table_name='dm_lecturer_comment_act',
        postgresql_using='gin',
    )
    op.drop_table('dm_lecturer_comment_act')
