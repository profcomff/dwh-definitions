"""comments-stg-union-member

Revision ID: 2a352723139d
Revises: 059a2a1571f1
Create Date: 2025-09-09 15:08:35.218584

"""

import sqlalchemy as sa
from alembic import op


revision = '2a352723139d'
down_revision = '059a2a1571f1'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column(
        'union_member',
        'id',
        existing_type=sa.INTEGER(),
        comment='Уникальный идентификатор пользователя',
        existing_nullable=False,
        autoincrement=True,
        schema='STG_UNION_MEMBER',
    )
    op.alter_column(
        'union_member',
        'type_of_learning',
        existing_type=sa.VARCHAR(),
        comment='Тип обучения (дневное/вечернее, бюджет/контракт)',
        existing_nullable=True,
        schema='STG_UNION_MEMBER',
    )
    op.alter_column(
        'union_member',
        'rzd_status',
        existing_type=sa.VARCHAR(),
        comment='Статус в системе РЖД',
        existing_nullable=True,
        schema='STG_UNION_MEMBER',
    )
    op.alter_column(
        'union_member',
        'academic_level',
        existing_type=sa.VARCHAR(),
        comment='Уровень образования (бакалавриат/магистратура/аспирантура)',
        existing_nullable=True,
        schema='STG_UNION_MEMBER',
    )
    op.alter_column(
        'union_member',
        'status',
        existing_type=sa.VARCHAR(),
        comment='Текущий статус пользователя',
        existing_nullable=True,
        schema='STG_UNION_MEMBER',
    )
    op.alter_column(
        'union_member',
        'faculty',
        existing_type=sa.VARCHAR(),
        comment='Название факультета',
        existing_nullable=True,
        schema='STG_UNION_MEMBER',
    )
    op.alter_column(
        'union_member',
        'first_name',
        existing_type=sa.VARCHAR(),
        comment='Имя пользователя',
        existing_nullable=True,
        schema='STG_UNION_MEMBER',
    )
    op.alter_column(
        'union_member',
        'last_name',
        existing_type=sa.VARCHAR(),
        comment='Фамилия пользователя',
        existing_nullable=True,
        schema='STG_UNION_MEMBER',
    )
    op.alter_column(
        'union_member',
        'email',
        existing_type=sa.VARCHAR(),
        comment='Email пользователя',
        existing_nullable=True,
        schema='STG_UNION_MEMBER',
    )
    op.alter_column(
        'union_member',
        'date_of_birth',
        existing_type=sa.VARCHAR(),
        comment='Дата рождения',
        existing_nullable=True,
        schema='STG_UNION_MEMBER',
    )
    op.alter_column(
        'union_member',
        'phone_number',
        existing_type=sa.VARCHAR(),
        comment='Номер телефона',
        existing_nullable=True,
        schema='STG_UNION_MEMBER',
    )
    op.alter_column(
        'union_member',
        'image',
        existing_type=sa.VARCHAR(),
        comment='Фото пользователя (ссылка или base64)',
        existing_nullable=True,
        schema='STG_UNION_MEMBER',
    )
    op.alter_column(
        'union_member',
        'rzd_datetime',
        existing_type=sa.VARCHAR(),
        comment='Дата в системе РЖД',
        existing_nullable=True,
        schema='STG_UNION_MEMBER',
    )
    op.alter_column(
        'union_member',
        'rzd_number',
        existing_type=sa.VARCHAR(),
        comment='Номер в системе РЖД',
        existing_nullable=True,
        schema='STG_UNION_MEMBER',
    )
    op.alter_column(
        'union_member',
        'grade_level',
        existing_type=sa.INTEGER(),
        comment='Курс (год обучения)',
        existing_nullable=True,
        schema='STG_UNION_MEMBER',
    )
    op.alter_column(
        'union_member',
        'has_student_id',
        existing_type=sa.BOOLEAN(),
        comment='Наличие студенческого билета',
        existing_nullable=True,
        schema='STG_UNION_MEMBER',
    )
    op.alter_column(
        'union_member',
        'entry_date',
        existing_type=sa.VARCHAR(),
        comment='Дата поступления',
        existing_nullable=True,
        schema='STG_UNION_MEMBER',
    )
    op.alter_column(
        'union_member',
        'status_gain_date',
        existing_type=sa.VARCHAR(),
        comment='Дата получения текущего статуса',
        existing_nullable=True,
        schema='STG_UNION_MEMBER',
    )
    op.alter_column(
        'union_member',
        'card_id',
        existing_type=sa.INTEGER(),
        comment='ID карты профкома',
        existing_nullable=True,
        schema='STG_UNION_MEMBER',
    )
    op.alter_column(
        'union_member',
        'card_status',
        existing_type=sa.VARCHAR(),
        comment='Статус карты профкома',
        existing_nullable=True,
        schema='STG_UNION_MEMBER',
    )
    op.alter_column(
        'union_member',
        'card_date',
        existing_type=sa.VARCHAR(),
        comment='Дата выдачи карты профкома',
        existing_nullable=True,
        schema='STG_UNION_MEMBER',
    )
    op.alter_column(
        'union_member',
        'card_number',
        existing_type=sa.VARCHAR(),
        comment='Номер карты профкома',
        existing_nullable=True,
        schema='STG_UNION_MEMBER',
    )
    op.alter_column(
        'union_member',
        'card_user',
        existing_type=sa.VARCHAR(),
        comment='Пользователь, связанный с картой',
        existing_nullable=True,
        schema='STG_UNION_MEMBER',
    )
    op.alter_column(
        'union_member',
        'student_id',
        existing_type=sa.VARCHAR(),
        comment='Номер студенческого билета',
        existing_nullable=True,
        schema='STG_UNION_MEMBER',
    )


def downgrade():
    op.alter_column(
        'union_member',
        'student_id',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Номер студенческого билета',
        existing_nullable=True,
        schema='STG_UNION_MEMBER',
    )
    op.alter_column(
        'union_member',
        'card_user',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Пользователь, связанный с картой',
        existing_nullable=True,
        schema='STG_UNION_MEMBER',
    )
    op.alter_column(
        'union_member',
        'card_number',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Номер карты профкома',
        existing_nullable=True,
        schema='STG_UNION_MEMBER',
    )
    op.alter_column(
        'union_member',
        'card_date',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Дата выдачи карты профкома',
        existing_nullable=True,
        schema='STG_UNION_MEMBER',
    )
    op.alter_column(
        'union_member',
        'card_status',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Статус карты профкома',
        existing_nullable=True,
        schema='STG_UNION_MEMBER',
    )
    op.alter_column(
        'union_member',
        'card_id',
        existing_type=sa.INTEGER(),
        comment=None,
        existing_comment='ID карты профкома',
        existing_nullable=True,
        schema='STG_UNION_MEMBER',
    )
    op.alter_column(
        'union_member',
        'status_gain_date',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Дата получения текущего статуса',
        existing_nullable=True,
        schema='STG_UNION_MEMBER',
    )
    op.alter_column(
        'union_member',
        'entry_date',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Дата поступления',
        existing_nullable=True,
        schema='STG_UNION_MEMBER',
    )
    op.alter_column(
        'union_member',
        'has_student_id',
        existing_type=sa.BOOLEAN(),
        comment=None,
        existing_comment='Наличие студенческого билета',
        existing_nullable=True,
        schema='STG_UNION_MEMBER',
    )
    op.alter_column(
        'union_member',
        'grade_level',
        existing_type=sa.INTEGER(),
        comment=None,
        existing_comment='Курс (год обучения)',
        existing_nullable=True,
        schema='STG_UNION_MEMBER',
    )
    op.alter_column(
        'union_member',
        'rzd_number',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Номер в системе РЖД',
        existing_nullable=True,
        schema='STG_UNION_MEMBER',
    )
    op.alter_column(
        'union_member',
        'rzd_datetime',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Дата в системе РЖД',
        existing_nullable=True,
        schema='STG_UNION_MEMBER',
    )
    op.alter_column(
        'union_member',
        'image',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Фото пользователя (ссылка или base64)',
        existing_nullable=True,
        schema='STG_UNION_MEMBER',
    )
    op.alter_column(
        'union_member',
        'phone_number',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Номер телефона',
        existing_nullable=True,
        schema='STG_UNION_MEMBER',
    )
    op.alter_column(
        'union_member',
        'date_of_birth',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Дата рождения',
        existing_nullable=True,
        schema='STG_UNION_MEMBER',
    )
    op.alter_column(
        'union_member',
        'email',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Email пользователя',
        existing_nullable=True,
        schema='STG_UNION_MEMBER',
    )
    op.alter_column(
        'union_member',
        'last_name',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Фамилия пользователя',
        existing_nullable=True,
        schema='STG_UNION_MEMBER',
    )
    op.alter_column(
        'union_member',
        'first_name',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Имя пользователя',
        existing_nullable=True,
        schema='STG_UNION_MEMBER',
    )
    op.alter_column(
        'union_member',
        'faculty',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Название факультета',
        existing_nullable=True,
        schema='STG_UNION_MEMBER',
    )
    op.alter_column(
        'union_member',
        'status',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Текущий статус пользователя',
        existing_nullable=True,
        schema='STG_UNION_MEMBER',
    )
    op.alter_column(
        'union_member',
        'academic_level',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Уровень образования (бакалавриат/магистратура/аспирантура)',
        existing_nullable=True,
        schema='STG_UNION_MEMBER',
    )
    op.alter_column(
        'union_member',
        'rzd_status',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Статус в системе РЖД',
        existing_nullable=True,
        schema='STG_UNION_MEMBER',
    )
    op.alter_column(
        'union_member',
        'type_of_learning',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Тип обучения (дневное/вечернее, бюджет/контракт)',
        existing_nullable=True,
        schema='STG_UNION_MEMBER',
    )
    op.alter_column(
        'union_member',
        'id',
        existing_type=sa.INTEGER(),
        comment=None,
        existing_comment='Уникальный идентификатор пользователя',
        existing_nullable=False,
        autoincrement=True,
        schema='STG_UNION_MEMBER',
    )
