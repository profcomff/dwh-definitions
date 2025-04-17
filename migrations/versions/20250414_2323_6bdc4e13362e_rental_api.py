"""rental-api

Revision ID: 6bdc4e13362e
Revises: f8908a4837a5
Create Date: 2025-04-14 23:23:30.132546

"""

from alembic import op
import sqlalchemy as sa
import os


# revision identifiers, used by Alembic.
revision = '6bdc4e13362e'
down_revision = 'f8908a4837a5'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table_schema("ODS_RENTAL")
    op.create_table_schema("STG_RENTAL")
    op.create_table_schema("DM_RENTAL")
    op.create_table_schema("DWH_RENTAL")
    op.create_table(
        'dm_rentals_events',
        sa.Column('uuid', sa.Uuid(), nullable=False, comment='Техническое поле dwh'),
        sa.Column('user_id', sa.Integer(), nullable=False, comment='Идентификатор пользователя'),
        sa.Column('item_id', sa.Integer(), nullable=False, comment='Идентификатор предмета'),
        sa.Column(
            'admin_open_session_id', sa.Integer(), nullable=False, comment='Идентификатор админа начавшего сессию'
        ),
        sa.Column(
            'admin_close_session_id', sa.Integer(), nullable=True, comment='Идентификатор админа закончевшего сессию'
        ),
        sa.Column('reservation_ts', sa.DateTime(), nullable=False, comment='Время начала брони'),
        sa.Column('start_ts', sa.DateTime(), nullable=False, comment='Timestamp начала аренды предмета, мск'),
        sa.Column('end_ts', sa.DateTime(), nullable=False, comment='Timestamp рассчетное время возврата предмета, мск'),
        sa.Column(
            'actual_return_ts', sa.DateTime(), nullable=False, comment='Timestamp реальное время возврата предмета, мск'
        ),
        sa.Column('status', sa.String(), nullable=False, comment='Статус текущей сессии'),
        sa.Column('duration', sa.Interval(), nullable=False, comment='Продолжительность аренды, в часах'),
        sa.Column('delay', sa.Interval(), nullable=False, comment='Время задержки возврата'),
        sa.Column('overdue_flag', sa.Boolean(), nullable=False, comment='Флаг просрочки'),
        sa.Column('conversion_flag', sa.Boolean(), nullable=False, comment='Флаг конверсии из брони в аренду'),
        sa.Column('type_id', sa.Integer(), nullable=False, comment='Идентификатор типа вещи'),
        sa.Column('type', sa.String(), nullable=False, comment='Тип вещи'),
        sa.Column('name', sa.String(), nullable=False, comment='Название вещи'),
        sa.Column('image_url', sa.String(), nullable=True, comment='Ссылка на фото вещи'),
        sa.Column('description', sa.String(), nullable=True, comment='Описание вещи'),
        sa.Column('available_items', sa.Integer(), nullable=False, comment='Количество доступных вещей'),
        sa.Column('total_items', sa.Integer(), nullable=False, comment='Количество вещей данного типа'),
        sa.Column('rental_count', sa.Integer(), nullable=False, comment='Общее количество аренд данного типа'),
        sa.Column('avg_downtime_hours', sa.Interval(), nullable=False, comment='Среднее время простоя'),
        sa.Column('avg_rent_hours', sa.Interval(), nullable=False, comment='Среднее время аренды'),
        sa.Column('session_id', sa.Integer(), nullable=False, comment='Идентификатор сессии'),
        sa.Column('admin_strike_id', sa.Integer(), nullable=True, comment='Идентификаор админа'),
        sa.Column('strike_reason', sa.String(), nullable=True, comment='Причина страйка'),
        sa.Column('strike_date', sa.DateTime(), nullable=True, comment='Timestamp начисления страйка, мск'),
        sa.Column('strike_count', sa.Integer(), nullable=True, comment='Количество страйков у пользователя'),
        sa.PrimaryKeyConstraint('uuid'),
        schema='DM_RENTAL',
        comment='\n    Данные арендных сессий\n    ',
        info={'sensitive': False},
    )
    op.create_table(
        'event',
        sa.Column('uuid', sa.Uuid(), nullable=False, comment='Техническое поле dwh'),
        sa.Column('api_id', sa.Integer(), nullable=False, comment='Идентификатор в rental-api'),
        sa.Column('user_id', sa.Integer(), nullable=False, comment='Идентификатор пользователя'),
        sa.Column('admin_id', sa.Integer(), nullable=False, comment='Идентификатор админа'),
        sa.Column('session_id', sa.Integer(), nullable=False, comment='Идентификатор сессии'),
        sa.Column('action_type', sa.String(), nullable=False, comment='Тип действия'),
        sa.Column('details', sa.String(), nullable=False, comment='Описание лога'),
        sa.Column('create_ts', sa.DateTime(), nullable=False, comment='Timestamp лога, мск'),
        sa.Column('valid_from_dt', sa.Date(), nullable=True, comment='Дата начала действия записи'),
        sa.Column('valid_to_dt', sa.Date(), nullable=True, comment='Дата конца действия записи'),
        sa.PrimaryKeyConstraint('uuid'),
        schema='DWH_RENTAL',
        comment='\n    Логи rental-api\n    ',
        info={'sensitive': False},
    )
    op.create_table(
        'item',
        sa.Column('uuid', sa.Uuid(), nullable=False, comment='Техническое поле в dwh'),
        sa.Column('api_id', sa.Integer(), nullable=False, comment='Идентификатор в rental-api'),
        sa.Column('type_id', sa.Integer(), nullable=False, comment='Идентификатор типа вещи'),
        sa.Column('is_available', sa.Boolean(), nullable=False, comment='Маркер доступности вещи'),
        sa.Column('type', sa.String(), nullable=False, comment='Тип вещи'),
        sa.Column('valid_from_dt', sa.Date(), nullable=True, comment='Дата начала действия записи'),
        sa.Column('valid_to_dt', sa.Date(), nullable=True, comment='Дата конца действия записи'),
        sa.PrimaryKeyConstraint('uuid'),
        schema='DWH_RENTAL',
        comment='\n    Вещи в rental.api\n    ',
        info={'sensitive': False},
    )
    op.create_table(
        'item_type',
        sa.Column('uuid', sa.Uuid(), nullable=False, comment='Техническое поле в dwh'),
        sa.Column('api_id', sa.Integer(), nullable=False, comment='Идентификатор в rental-api'),
        sa.Column('name', sa.String(), nullable=False, comment='Название вещи'),
        sa.Column('image_url', sa.String(), nullable=True, comment='Ссылка на фото вещи'),
        sa.Column('description', sa.String(), nullable=True, comment='Описание вещи'),
        sa.Column('valid_from_dt', sa.Date(), nullable=True, comment='Дата начала действия записи'),
        sa.Column('valid_to_dt', sa.Date(), nullable=True, comment='Дата конца действия записи'),
        sa.PrimaryKeyConstraint('uuid'),
        schema='DWH_RENTAL',
        comment='\n    Описание, фото типа вещи в rental-api\n    ',
        info={'sensitive': False},
    )
    op.create_table(
        'rental_session',
        sa.Column('uuid', sa.Uuid(), nullable=False, comment='Техническое поле dwh'),
        sa.Column('api_id', sa.Integer(), nullable=False, comment='Идентификатор в rental-api'),
        sa.Column('user_id', sa.Integer(), nullable=False, comment='Идентификатор пользователя'),
        sa.Column('item_id', sa.Integer(), nullable=False, comment='Идентификатор предмета'),
        sa.Column('admin_open_id', sa.Integer(), nullable=False, comment='Идентификатор админа начавшего сессию'),
        sa.Column('admin_close_id', sa.Integer(), nullable=True, comment='Идентификатор админа закончевшего сессию'),
        sa.Column('reservation_ts', sa.DateTime(), nullable=False, comment='Время начала брони'),
        sa.Column('start_ts', sa.DateTime(), nullable=False, comment='Timestamp начала аренды предмета, мск'),
        sa.Column('end_ts', sa.DateTime(), nullable=False, comment='Timestamp рассчетное время возврата предмета, мск'),
        sa.Column(
            'actual_return_ts', sa.DateTime(), nullable=False, comment='Timestamp реальное время возврата предмета, мск'
        ),
        sa.Column('status', sa.String(), nullable=False, comment='Статус текущей сессии'),
        sa.Column('valid_from_dt', sa.Date(), nullable=True, comment='Дата начала действия записи'),
        sa.Column('valid_to_dt', sa.Date(), nullable=True, comment='Дата конца действия записи'),
        sa.PrimaryKeyConstraint('uuid'),
        schema='DWH_RENTAL',
        comment='\n    Сессия и статус для вещей rental-api\n    ',
        info={'sensitive': False},
    )
    op.create_table(
        'strike',
        sa.Column('uuid', sa.Uuid(), nullable=False, comment='Техническое поле dwh'),
        sa.Column('api_id', sa.Integer(), nullable=False, comment='Идентификатор в rental-api'),
        sa.Column('user_id', sa.Integer(), nullable=False, comment='Идентификатор пользователя'),
        sa.Column('session_id', sa.Integer(), nullable=False, comment='Идентификатор сессии'),
        sa.Column('admin_id', sa.Integer(), nullable=False, comment='Идентификаор админа'),
        sa.Column('reason', sa.String(), nullable=False, comment='Причина страйка'),
        sa.Column('create_ts', sa.DateTime(), nullable=False, comment='Timestamp страйка, мск'),
        sa.Column('valid_from_dt', sa.Date(), nullable=True, comment='Дата начала действия записи'),
        sa.Column('valid_to_dt', sa.Date(), nullable=True, comment='Дата конца действия записи'),
        sa.PrimaryKeyConstraint('uuid'),
        schema='DWH_RENTAL',
        comment='\n    Страйки пользователям в rental-api\n    ',
        info={'sensitive': False},
    )
    op.create_table(
        'event',
        sa.Column('uuid', sa.Uuid(), nullable=False, comment='Техническое поле dwh'),
        sa.Column('api_id', sa.Integer(), nullable=False, comment='Идентификатор в rental-api'),
        sa.Column('user_id', sa.Integer(), nullable=False, comment='Идентификатор пользователя'),
        sa.Column('admin_id', sa.Integer(), nullable=False, comment='Идентификатор админа'),
        sa.Column('session_id', sa.Integer(), nullable=False, comment='Идентификатор сессии'),
        sa.Column('action_type', sa.String(), nullable=False, comment='Тип действия'),
        sa.Column('details', sa.String(), nullable=False, comment='Описание лога'),
        sa.Column('create_ts', sa.DateTime(), nullable=False, comment='Timestamp лога, мск'),
        sa.PrimaryKeyConstraint('uuid'),
        schema='ODS_RENTAL',
        comment='\n    Логи rental-api\n    ',
        info={'sensitive': False},
    )
    op.create_table(
        'item',
        sa.Column('uuid', sa.Uuid(), nullable=False, comment='Техническое поле в dwh'),
        sa.Column('api_id', sa.Integer(), nullable=False, comment='Идентификатор в rental-api'),
        sa.Column('type_id', sa.Integer(), nullable=False, comment='Идентификатор типа вещи'),
        sa.Column('is_available', sa.Boolean(), nullable=False, comment='Маркер доступности вещи'),
        sa.Column('type', sa.String(), nullable=False, comment='Тип вещи'),
        sa.PrimaryKeyConstraint('uuid'),
        schema='ODS_RENTAL',
        comment='\n    Вещи в rental.api\n    ',
        info={'sensitive': False},
    )
    op.create_table(
        'item_type',
        sa.Column('uuid', sa.Uuid(), nullable=False, comment='Техническое поле в dwh'),
        sa.Column('api_id', sa.Integer(), nullable=False, comment='Идентификатор в rental-api'),
        sa.Column('name', sa.String(), nullable=False, comment='Название вещи'),
        sa.Column('image_url', sa.String(), nullable=True, comment='Ссылка на фото вещи'),
        sa.Column('description', sa.String(), nullable=True, comment='Описание вещи'),
        sa.PrimaryKeyConstraint('uuid'),
        schema='ODS_RENTAL',
        comment='\n    Описание, фото типа вещи в rental-api\n    ',
        info={'sensitive': False},
    )
    op.create_table(
        'rental_session',
        sa.Column('uuid', sa.Uuid(), nullable=False, comment='Техническое поле dwh'),
        sa.Column('api_id', sa.Integer(), nullable=False, comment='Идентификатор в rental-api'),
        sa.Column('user_id', sa.Integer(), nullable=False, comment='Идентификатор пользователя'),
        sa.Column('item_id', sa.Integer(), nullable=False, comment='Идентификатор предмета'),
        sa.Column('admin_open_id', sa.Integer(), nullable=False, comment='Идентификатор админа начавшего сессию'),
        sa.Column('admin_close_id', sa.Integer(), nullable=True, comment='Идентификатор админа закончевшего сессию'),
        sa.Column('reservation_ts', sa.DateTime(), nullable=False, comment='Время начала брони'),
        sa.Column('start_ts', sa.DateTime(), nullable=False, comment='Timestamp начала аренды предмета, мск'),
        sa.Column('end_ts', sa.DateTime(), nullable=False, comment='Timestamp рассчетное время возврата предмета, мск'),
        sa.Column(
            'actual_return_ts', sa.DateTime(), nullable=False, comment='Timestamp реальное время возврата предмета, мск'
        ),
        sa.Column('status', sa.String(), nullable=False, comment='Статус текущей сессии'),
        sa.PrimaryKeyConstraint('uuid'),
        schema='ODS_RENTAL',
        comment='\n    Сессия и статус для вещей rental-api\n    ',
        info={'sensitive': False},
    )
    op.create_table(
        'strike',
        sa.Column('uuid', sa.Uuid(), nullable=False, comment='Техническое поле dwh'),
        sa.Column('api_id', sa.Integer(), nullable=False, comment='Идентификатор в rental-api'),
        sa.Column('user_id', sa.Integer(), nullable=False, comment='Идентификатор пользователя'),
        sa.Column('session_id', sa.Integer(), nullable=False, comment='Идентификатор сессии'),
        sa.Column('admin_id', sa.Integer(), nullable=False, comment='Идентификаор админа'),
        sa.Column('reason', sa.String(), nullable=False, comment='Причина страйка'),
        sa.Column('create_ts', sa.DateTime(), nullable=False, comment='Timestamp страйка, мск'),
        sa.PrimaryKeyConstraint('uuid'),
        schema='ODS_RENTAL',
        comment='\n    Страйки пользователям в rental-api\n    ',
        info={'sensitive': False},
    )
    op.create_table(
        'event',
        sa.Column('api_id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('admin_id', sa.Integer(), nullable=False),
        sa.Column('session_id', sa.Integer(), nullable=False),
        sa.Column('action_type', sa.String(), nullable=False),
        sa.Column('details', sa.String(), nullable=False),
        sa.Column('create_ts', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('api_id'),
        schema='STG_RENTAL',
        info={'sensitive': False},
    )
    op.create_table(
        'item',
        sa.Column('api_id', sa.Integer(), nullable=False),
        sa.Column('type_id', sa.Integer(), nullable=False),
        sa.Column('is_available', sa.Boolean(), nullable=False),
        sa.Column('type', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('api_id'),
        schema='STG_RENTAL',
        info={'sensitive': False},
    )
    op.create_table(
        'item_type',
        sa.Column('api_id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('image_url', sa.String(), nullable=True),
        sa.Column('description', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('api_id'),
        schema='STG_RENTAL',
        info={'sensitive': False},
    )
    op.create_table(
        'rental_session',
        sa.Column('api_id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('item_id', sa.Integer(), nullable=False),
        sa.Column('admin_open_id', sa.Integer(), nullable=False),
        sa.Column('admin_close_id', sa.Integer(), nullable=True),
        sa.Column('reservation_ts', sa.DateTime(), nullable=False),
        sa.Column('start_ts', sa.DateTime(), nullable=False),
        sa.Column('end_ts', sa.DateTime(), nullable=False),
        sa.Column('actual_return_ts', sa.DateTime(), nullable=False),
        sa.Column('status', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('api_id'),
        schema='STG_RENTAL',
        info={'sensitive': False},
    )
    op.create_table(
        'strike',
        sa.Column('api_id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('session_id', sa.Integer(), nullable=False),
        sa.Column('admin_id', sa.Integer(), nullable=False),
        sa.Column('reason', sa.String(), nullable=False),
        sa.Column('create_ts', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('api_id'),
        schema='STG_RENTAL',
        info={'sensitive': False},
    )
    op.create_group(
        "test_dwh_ods_rental_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_rental_read"
    )
    op.create_group(
        "test_dwh_ods_rental_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_rental_write"
    )
    op.create_group(
        "test_dwh_ods_rental_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_rental_all"
    )
    op.create_group(
        "test_dwh_stg_rental_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rental_read"
    )
    op.create_group(
        "test_dwh_stg_rental_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rental_write"
    )
    op.create_group(
        "test_dwh_stg_rental_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rental_all"
    )
    op.create_group(
        "test_dwh_dm_rental_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_rental_read"
    )
    op.create_group(
        "test_dwh_dm_rental_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_rental_write"
    )
    op.create_group("test_dwh_dm_rental_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_rental_all")
    op.create_group(
        "test_dwh_dwh_rental_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rental_read"
    )
    op.create_group(
        "test_dwh_dwh_rental_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rental_write"
    )
    op.create_group(
        "test_dwh_dwh_rental_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rental_all"
    )
    op.grant_on_schema(
        "test_dwh_ods_rental_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_rental_read",
        "ODS_RENTAL",
    )
    op.grant_on_schema(
        "test_dwh_ods_rental_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_rental_write",
        "ODS_RENTAL",
    )
    op.grant_on_schema(
        "test_dwh_ods_rental_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_rental_all",
        "ODS_RENTAL",
    )
    op.grant_on_schema(
        "test_dwh_stg_rental_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rental_read",
        "STG_RENTAL",
    )
    op.grant_on_schema(
        "test_dwh_stg_rental_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rental_write",
        "STG_RENTAL",
    )
    op.grant_on_schema(
        "test_dwh_stg_rental_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rental_all",
        "STG_RENTAL",
    )
    op.grant_on_schema(
        "test_dwh_dm_rental_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_rental_read",
        "DM_RENTAL",
    )
    op.grant_on_schema(
        "test_dwh_dm_rental_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_rental_write",
        "DM_RENTAL",
    )
    op.grant_on_schema(
        "test_dwh_dm_rental_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_rental_all", "DM_RENTAL"
    )
    op.grant_on_schema(
        "test_dwh_dwh_rental_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rental_read",
        "DWH_RENTAL",
    )
    op.grant_on_schema(
        "test_dwh_dwh_rental_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rental_write",
        "DWH_RENTAL",
    )
    op.grant_on_schema(
        "test_dwh_dwh_rental_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rental_all",
        "DWH_RENTAL",
    )
    op.grant_on_table(
        "test_dwh_ods_rental_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_rental_read",
        ['SELECT'],
        '"ODS_RENTAL".item_type',
    )
    op.grant_on_table(
        "test_dwh_ods_rental_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_rental_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_RENTAL".item_type',
    )
    op.grant_on_table(
        "test_dwh_ods_rental_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_rental_all",
        ['ALL'],
        '"ODS_RENTAL".item_type',
    )
    op.grant_on_table(
        "test_dwh_ods_rental_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_rental_read",
        ['SELECT'],
        '"ODS_RENTAL".rental_session',
    )
    op.grant_on_table(
        "test_dwh_ods_rental_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_rental_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_RENTAL".rental_session',
    )
    op.grant_on_table(
        "test_dwh_ods_rental_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_rental_all",
        ['ALL'],
        '"ODS_RENTAL".rental_session',
    )
    op.grant_on_table(
        "test_dwh_ods_rental_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_rental_read",
        ['SELECT'],
        '"ODS_RENTAL".item',
    )
    op.grant_on_table(
        "test_dwh_ods_rental_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_rental_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_RENTAL".item',
    )
    op.grant_on_table(
        "test_dwh_ods_rental_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_rental_all",
        ['ALL'],
        '"ODS_RENTAL".item',
    )
    op.grant_on_table(
        "test_dwh_ods_rental_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_rental_read",
        ['SELECT'],
        '"ODS_RENTAL".strike',
    )
    op.grant_on_table(
        "test_dwh_ods_rental_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_rental_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_RENTAL".strike',
    )
    op.grant_on_table(
        "test_dwh_ods_rental_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_rental_all",
        ['ALL'],
        '"ODS_RENTAL".strike',
    )
    op.grant_on_table(
        "test_dwh_ods_rental_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_rental_read",
        ['SELECT'],
        '"ODS_RENTAL".event',
    )
    op.grant_on_table(
        "test_dwh_ods_rental_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_rental_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_RENTAL".event',
    )
    op.grant_on_table(
        "test_dwh_ods_rental_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_rental_all",
        ['ALL'],
        '"ODS_RENTAL".event',
    )
    op.grant_on_table(
        "test_dwh_stg_rental_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rental_read",
        ['SELECT'],
        '"STG_RENTAL".event',
    )
    op.grant_on_table(
        "test_dwh_stg_rental_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rental_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_RENTAL".event',
    )
    op.grant_on_table(
        "test_dwh_stg_rental_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rental_all",
        ['ALL'],
        '"STG_RENTAL".event',
    )
    op.grant_on_table(
        "test_dwh_stg_rental_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rental_read",
        ['SELECT'],
        '"STG_RENTAL".item_type',
    )
    op.grant_on_table(
        "test_dwh_stg_rental_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rental_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_RENTAL".item_type',
    )
    op.grant_on_table(
        "test_dwh_stg_rental_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rental_all",
        ['ALL'],
        '"STG_RENTAL".item_type',
    )
    op.grant_on_table(
        "test_dwh_stg_rental_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rental_read",
        ['SELECT'],
        '"STG_RENTAL".strike',
    )
    op.grant_on_table(
        "test_dwh_stg_rental_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rental_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_RENTAL".strike',
    )
    op.grant_on_table(
        "test_dwh_stg_rental_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rental_all",
        ['ALL'],
        '"STG_RENTAL".strike',
    )
    op.grant_on_table(
        "test_dwh_stg_rental_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rental_read",
        ['SELECT'],
        '"STG_RENTAL".item',
    )
    op.grant_on_table(
        "test_dwh_stg_rental_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rental_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_RENTAL".item',
    )
    op.grant_on_table(
        "test_dwh_stg_rental_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rental_all",
        ['ALL'],
        '"STG_RENTAL".item',
    )
    op.grant_on_table(
        "test_dwh_stg_rental_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rental_read",
        ['SELECT'],
        '"STG_RENTAL".rental_session',
    )
    op.grant_on_table(
        "test_dwh_stg_rental_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rental_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_RENTAL".rental_session',
    )
    op.grant_on_table(
        "test_dwh_stg_rental_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rental_all",
        ['ALL'],
        '"STG_RENTAL".rental_session',
    )
    op.grant_on_table(
        "test_dwh_dm_rental_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_rental_read",
        ['SELECT'],
        '"DM_RENTAL".dm_rentals_events',
    )
    op.grant_on_table(
        "test_dwh_dm_rental_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_rental_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DM_RENTAL".dm_rentals_events',
    )
    op.grant_on_table(
        "test_dwh_dm_rental_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_rental_all",
        ['ALL'],
        '"DM_RENTAL".dm_rentals_events',
    )
    op.grant_on_table(
        "test_dwh_dwh_rental_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rental_read",
        ['SELECT'],
        '"DWH_RENTAL".event',
    )
    op.grant_on_table(
        "test_dwh_dwh_rental_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rental_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DWH_RENTAL".event',
    )
    op.grant_on_table(
        "test_dwh_dwh_rental_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rental_all",
        ['ALL'],
        '"DWH_RENTAL".event',
    )
    op.grant_on_table(
        "test_dwh_dwh_rental_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rental_read",
        ['SELECT'],
        '"DWH_RENTAL".item_type',
    )
    op.grant_on_table(
        "test_dwh_dwh_rental_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rental_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DWH_RENTAL".item_type',
    )
    op.grant_on_table(
        "test_dwh_dwh_rental_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rental_all",
        ['ALL'],
        '"DWH_RENTAL".item_type',
    )
    op.grant_on_table(
        "test_dwh_dwh_rental_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rental_read",
        ['SELECT'],
        '"DWH_RENTAL".item',
    )
    op.grant_on_table(
        "test_dwh_dwh_rental_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rental_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DWH_RENTAL".item',
    )
    op.grant_on_table(
        "test_dwh_dwh_rental_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rental_all",
        ['ALL'],
        '"DWH_RENTAL".item',
    )
    op.grant_on_table(
        "test_dwh_dwh_rental_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rental_read",
        ['SELECT'],
        '"DWH_RENTAL".rental_session',
    )
    op.grant_on_table(
        "test_dwh_dwh_rental_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rental_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DWH_RENTAL".rental_session',
    )
    op.grant_on_table(
        "test_dwh_dwh_rental_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rental_all",
        ['ALL'],
        '"DWH_RENTAL".rental_session',
    )
    op.grant_on_table(
        "test_dwh_dwh_rental_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rental_read",
        ['SELECT'],
        '"DWH_RENTAL".strike',
    )
    op.grant_on_table(
        "test_dwh_dwh_rental_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rental_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DWH_RENTAL".strike',
    )
    op.grant_on_table(
        "test_dwh_dwh_rental_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rental_all",
        ['ALL'],
        '"DWH_RENTAL".strike',
    )


def downgrade():
    op.revoke_on_table(
        "test_dwh_dwh_rental_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rental_all",
        ['ALL'],
        '"DWH_RENTAL".strike',
    )
    op.revoke_on_table(
        "test_dwh_dwh_rental_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rental_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DWH_RENTAL".strike',
    )
    op.revoke_on_table(
        "test_dwh_dwh_rental_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rental_read",
        ['SELECT'],
        '"DWH_RENTAL".strike',
    )
    op.revoke_on_table(
        "test_dwh_dwh_rental_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rental_all",
        ['ALL'],
        '"DWH_RENTAL".rental_session',
    )
    op.revoke_on_table(
        "test_dwh_dwh_rental_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rental_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DWH_RENTAL".rental_session',
    )
    op.revoke_on_table(
        "test_dwh_dwh_rental_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rental_read",
        ['SELECT'],
        '"DWH_RENTAL".rental_session',
    )
    op.revoke_on_table(
        "test_dwh_dwh_rental_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rental_all",
        ['ALL'],
        '"DWH_RENTAL".item',
    )
    op.revoke_on_table(
        "test_dwh_dwh_rental_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rental_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DWH_RENTAL".item',
    )
    op.revoke_on_table(
        "test_dwh_dwh_rental_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rental_read",
        ['SELECT'],
        '"DWH_RENTAL".item',
    )
    op.revoke_on_table(
        "test_dwh_dwh_rental_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rental_all",
        ['ALL'],
        '"DWH_RENTAL".item_type',
    )
    op.revoke_on_table(
        "test_dwh_dwh_rental_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rental_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DWH_RENTAL".item_type',
    )
    op.revoke_on_table(
        "test_dwh_dwh_rental_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rental_read",
        ['SELECT'],
        '"DWH_RENTAL".item_type',
    )
    op.revoke_on_table(
        "test_dwh_dwh_rental_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rental_all",
        ['ALL'],
        '"DWH_RENTAL".event',
    )
    op.revoke_on_table(
        "test_dwh_dwh_rental_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rental_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DWH_RENTAL".event',
    )
    op.revoke_on_table(
        "test_dwh_dwh_rental_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rental_read",
        ['SELECT'],
        '"DWH_RENTAL".event',
    )
    op.revoke_on_table(
        "test_dwh_dm_rental_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_rental_all",
        ['ALL'],
        '"DM_RENTAL".dm_rentals_events',
    )
    op.revoke_on_table(
        "test_dwh_dm_rental_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_rental_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DM_RENTAL".dm_rentals_events',
    )
    op.revoke_on_table(
        "test_dwh_dm_rental_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_rental_read",
        ['SELECT'],
        '"DM_RENTAL".dm_rentals_events',
    )
    op.revoke_on_table(
        "test_dwh_stg_rental_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rental_all",
        ['ALL'],
        '"STG_RENTAL".rental_session',
    )
    op.revoke_on_table(
        "test_dwh_stg_rental_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rental_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_RENTAL".rental_session',
    )
    op.revoke_on_table(
        "test_dwh_stg_rental_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rental_read",
        ['SELECT'],
        '"STG_RENTAL".rental_session',
    )
    op.revoke_on_table(
        "test_dwh_stg_rental_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rental_all",
        ['ALL'],
        '"STG_RENTAL".item',
    )
    op.revoke_on_table(
        "test_dwh_stg_rental_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rental_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_RENTAL".item',
    )
    op.revoke_on_table(
        "test_dwh_stg_rental_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rental_read",
        ['SELECT'],
        '"STG_RENTAL".item',
    )
    op.revoke_on_table(
        "test_dwh_stg_rental_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rental_all",
        ['ALL'],
        '"STG_RENTAL".strike',
    )
    op.revoke_on_table(
        "test_dwh_stg_rental_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rental_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_RENTAL".strike',
    )
    op.revoke_on_table(
        "test_dwh_stg_rental_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rental_read",
        ['SELECT'],
        '"STG_RENTAL".strike',
    )
    op.revoke_on_table(
        "test_dwh_stg_rental_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rental_all",
        ['ALL'],
        '"STG_RENTAL".item_type',
    )
    op.revoke_on_table(
        "test_dwh_stg_rental_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rental_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_RENTAL".item_type',
    )
    op.revoke_on_table(
        "test_dwh_stg_rental_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rental_read",
        ['SELECT'],
        '"STG_RENTAL".item_type',
    )
    op.revoke_on_table(
        "test_dwh_stg_rental_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rental_all",
        ['ALL'],
        '"STG_RENTAL".event',
    )
    op.revoke_on_table(
        "test_dwh_stg_rental_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rental_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_RENTAL".event',
    )
    op.revoke_on_table(
        "test_dwh_stg_rental_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rental_read",
        ['SELECT'],
        '"STG_RENTAL".event',
    )
    op.revoke_on_table(
        "test_dwh_ods_rental_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_rental_all",
        ['ALL'],
        '"ODS_RENTAL".event',
    )
    op.revoke_on_table(
        "test_dwh_ods_rental_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_rental_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_RENTAL".event',
    )
    op.revoke_on_table(
        "test_dwh_ods_rental_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_rental_read",
        ['SELECT'],
        '"ODS_RENTAL".event',
    )
    op.revoke_on_table(
        "test_dwh_ods_rental_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_rental_all",
        ['ALL'],
        '"ODS_RENTAL".strike',
    )
    op.revoke_on_table(
        "test_dwh_ods_rental_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_rental_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_RENTAL".strike',
    )
    op.revoke_on_table(
        "test_dwh_ods_rental_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_rental_read",
        ['SELECT'],
        '"ODS_RENTAL".strike',
    )
    op.revoke_on_table(
        "test_dwh_ods_rental_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_rental_all",
        ['ALL'],
        '"ODS_RENTAL".item',
    )
    op.revoke_on_table(
        "test_dwh_ods_rental_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_rental_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_RENTAL".item',
    )
    op.revoke_on_table(
        "test_dwh_ods_rental_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_rental_read",
        ['SELECT'],
        '"ODS_RENTAL".item',
    )
    op.revoke_on_table(
        "test_dwh_ods_rental_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_rental_all",
        ['ALL'],
        '"ODS_RENTAL".rental_session',
    )
    op.revoke_on_table(
        "test_dwh_ods_rental_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_rental_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_RENTAL".rental_session',
    )
    op.revoke_on_table(
        "test_dwh_ods_rental_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_rental_read",
        ['SELECT'],
        '"ODS_RENTAL".rental_session',
    )
    op.revoke_on_table(
        "test_dwh_ods_rental_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_rental_all",
        ['ALL'],
        '"ODS_RENTAL".item_type',
    )
    op.revoke_on_table(
        "test_dwh_ods_rental_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_rental_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_RENTAL".item_type',
    )
    op.revoke_on_table(
        "test_dwh_ods_rental_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_rental_read",
        ['SELECT'],
        '"ODS_RENTAL".item_type',
    )
    op.revoke_on_schema(
        "test_dwh_dwh_rental_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rental_all",
        "DWH_RENTAL",
    )
    op.revoke_on_schema(
        "test_dwh_dwh_rental_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rental_write",
        "DWH_RENTAL",
    )
    op.revoke_on_schema(
        "test_dwh_dwh_rental_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rental_read",
        "DWH_RENTAL",
    )
    op.revoke_on_schema(
        "test_dwh_dm_rental_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_rental_all", "DM_RENTAL"
    )
    op.revoke_on_schema(
        "test_dwh_dm_rental_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_rental_write",
        "DM_RENTAL",
    )
    op.revoke_on_schema(
        "test_dwh_dm_rental_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_rental_read",
        "DM_RENTAL",
    )
    op.revoke_on_schema(
        "test_dwh_stg_rental_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rental_all",
        "STG_RENTAL",
    )
    op.revoke_on_schema(
        "test_dwh_stg_rental_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rental_write",
        "STG_RENTAL",
    )
    op.revoke_on_schema(
        "test_dwh_stg_rental_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rental_read",
        "STG_RENTAL",
    )
    op.revoke_on_schema(
        "test_dwh_ods_rental_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_rental_all",
        "ODS_RENTAL",
    )
    op.revoke_on_schema(
        "test_dwh_ods_rental_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_rental_write",
        "ODS_RENTAL",
    )
    op.revoke_on_schema(
        "test_dwh_ods_rental_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_rental_read",
        "ODS_RENTAL",
    )
    op.drop_table('strike', schema='STG_RENTAL')
    op.drop_table('rental_session', schema='STG_RENTAL')
    op.drop_table('item_type', schema='STG_RENTAL')
    op.drop_table('item', schema='STG_RENTAL')
    op.drop_table('event', schema='STG_RENTAL')
    op.drop_table('strike', schema='ODS_RENTAL')
    op.drop_table('rental_session', schema='ODS_RENTAL')
    op.drop_table('item_type', schema='ODS_RENTAL')
    op.drop_table('item', schema='ODS_RENTAL')
    op.drop_table('event', schema='ODS_RENTAL')
    op.drop_table('strike', schema='DWH_RENTAL')
    op.drop_table('rental_session', schema='DWH_RENTAL')
    op.drop_table('item_type', schema='DWH_RENTAL')
    op.drop_table('item', schema='DWH_RENTAL')
    op.drop_table('event', schema='DWH_RENTAL')
    op.drop_table('dm_rentals_events', schema='DM_RENTAL')
    op.delete_group(
        "test_dwh_dwh_rental_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rental_all"
    )
    op.delete_group(
        "test_dwh_dwh_rental_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rental_write"
    )
    op.delete_group(
        "test_dwh_dwh_rental_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_rental_read"
    )
    op.delete_group("test_dwh_dm_rental_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_rental_all")
    op.delete_group(
        "test_dwh_dm_rental_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_rental_write"
    )
    op.delete_group(
        "test_dwh_dm_rental_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_rental_read"
    )
    op.delete_group(
        "test_dwh_stg_rental_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rental_all"
    )
    op.delete_group(
        "test_dwh_stg_rental_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rental_write"
    )
    op.delete_group(
        "test_dwh_stg_rental_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rental_read"
    )
    op.delete_group(
        "test_dwh_ods_rental_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_rental_all"
    )
    op.delete_group(
        "test_dwh_ods_rental_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_rental_write"
    )
    op.delete_group(
        "test_dwh_ods_rental_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_rental_read"
    )
    op.drop_table_schema("DWH_RENTAL")
    op.drop_table_schema("DM_RENTAL")
    op.drop_table_schema("STG_RENTAL")
    op.drop_table_schema("ODS_RENTAL")
