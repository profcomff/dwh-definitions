"""unionmemberjoin

Revision ID: f31bd2cf406f
Revises: 34a1492064c9
Create Date: 2024-12-07 21:30:05.690606

"""

import os

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = 'f31bd2cf406f'
down_revision = '34a1492064c9'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table_schema("DM_USER")
    op.create_table(
        'union_member_join',
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(), nullable=True, comment="user's email from ods user info"),
        sa.Column('phone_number', sa.String(), nullable=True, comment="user's phone_number from ods user info"),
        sa.Column('vk_name', sa.String(), nullable=True, comment="user's vk_name from ods user info"),
        sa.Column('city', sa.String(), nullable=True, comment="user's city from ods uder info"),
        sa.Column('hometown', sa.String(), nullable=True, comment="user's hometown from ods user info"),
        sa.Column('location', sa.String(), nullable=True, comment="user's current city from ods user info"),
        sa.Column('github_name', sa.String(), nullable=True, comment="user's github_name from ods user info"),
        sa.Column('telegram_name', sa.String(), nullable=True, comment="user's telegram_name from ods user info"),
        sa.Column(
            'home_phone_number', sa.String(), nullable=True, comment="user's home_phone_number from ods user info"
        ),
        sa.Column(
            'education_level', sa.String(), nullable=True, comment='Bachelor/Master/Specialist from ods user info'
        ),
        sa.Column('university', sa.String(), nullable=True, comment="user's university from ods user info"),
        sa.Column('group', sa.String(), nullable=True, comment="user's group from ods user info"),
        sa.Column('faculty', sa.String(), nullable=True, comment="user's faculty from ods user info"),
        sa.Column('position', sa.String(), nullable=True, comment="user's position in university from ods user info"),
        sa.Column(
            'student_id_number', sa.String(), nullable=True, comment="user's student_id_number from ods user info"
        ),
        sa.Column(
            'department', sa.String(), nullable=True, comment="user's department in university from ods user info"
        ),
        sa.Column(
            'mode_of_study', sa.String(), nullable=True, comment='full-time/correspondence education from ods user info'
        ),
        sa.Column('full_name', sa.String(), nullable=True, comment="user's full_name from ods user info"),
        sa.Column('birth_date', sa.String(), nullable=True, comment="user's birth_date from ods user info"),
        sa.Column('photo', sa.String(), nullable=True, comment="user's photo(https://) from ods user info"),
        sa.Column('sex', sa.String(), nullable=True, comment='male/female from ods user info'),
        sa.Column('job', sa.String(), nullable=True, comment="user's job from ods user info"),
        sa.Column('work_location', sa.String(), nullable=True, comment="user's work_location from ods uder info"),
        sa.Column(
            'card_status',
            sa.String(),
            nullable=True,
            comment="card_status - user's card status (current or not) from ODS.user.info",
        ),
        sa.Column(
            'card_date',
            sa.String(),
            nullable=True,
            comment="card date - date of user's card activation from ODS.user.info",
        ),
        sa.Column(
            'card_number', sa.String(), nullable=True, comment="card number - number of user's card from ODS.user.info"
        ),
        sa.PrimaryKeyConstraint('user_id'),
        schema='DM_USER',
        comment='Таблица соответствия пользователей приложения и членов профсоюза',
    )
    op.create_group("test_dwh_dm_user_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_user_read")
    op.create_group("test_dwh_dm_user_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_user_write")
    op.create_group("test_dwh_dm_user_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_user_all")
    op.grant_on_schema(
        "test_dwh_dm_user_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_user_read", "DM_USER"
    )
    op.grant_on_schema(
        "test_dwh_dm_user_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_user_write", "DM_USER"
    )
    op.grant_on_schema(
        "test_dwh_dm_user_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_user_all", "DM_USER"
    )
    op.grant_on_table(
        "test_dwh_dm_user_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_user_read",
        ['SELECT'],
        '"DM_USER".union_member_join',
    )
    op.grant_on_table(
        "test_dwh_dm_user_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_user_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DM_USER".union_member_join',
    )
    op.grant_on_table(
        "test_dwh_dm_user_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_user_all",
        ['ALL'],
        '"DM_USER".union_member_join',
    )
    op.create_index(
        op.f('ix_DM_USER_union_member_join_user_id'), 'union_member_join', ['user_id'], unique=False, schema='DM_USER'
    )
    op.grant_on_table(
        "test_dwh_dm_user_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_user_read",
        ['SELECT'],
        '"DM_USER".union_member_join',
    )
    op.grant_on_table(
        "test_dwh_dm_user_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_user_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DM_USER".union_member_join',
    )
    op.grant_on_table(
        "test_dwh_dm_user_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_user_all",
        ['ALL'],
        '"DM_USER".union_member_join',
    )


def downgrade():
    op.revoke_on_table(
        "test_dwh_dm_user_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_user_all",
        ['ALL'],
        '"DM_USER".union_member_join',
    )
    op.revoke_on_table(
        "test_dwh_dm_user_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_user_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DM_USER".union_member_join',
    )
    op.revoke_on_table(
        "test_dwh_dm_user_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_user_read",
        ['SELECT'],
        '"DM_USER".union_member_join',
    )
    op.drop_index(op.f('ix_DM_USER_union_member_join_user_id'), table_name='union_member_join', schema='DM_USER')
    op.revoke_on_table(
        "test_dwh_dm_user_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_user_all",
        ['ALL'],
        '"DM_USER".union_member_join',
    )
    op.revoke_on_table(
        "test_dwh_dm_user_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_user_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DM_USER".union_member_join',
    )
    op.revoke_on_table(
        "test_dwh_dm_user_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_user_read",
        ['SELECT'],
        '"DM_USER".union_member_join',
    )
    op.revoke_on_schema(
        "test_dwh_dm_user_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_user_all", "DM_USER"
    )
    op.revoke_on_schema(
        "test_dwh_dm_user_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_user_write", "DM_USER"
    )
    op.revoke_on_schema(
        "test_dwh_dm_user_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_user_read", "DM_USER"
    )
    op.drop_table('union_member_join', schema='DM_USER')
    op.delete_group("test_dwh_dm_user_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_user_all")
    op.delete_group("test_dwh_dm_user_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_user_write")
    op.delete_group("test_dwh_dm_user_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_user_read")
    op.drop_table_schema("DM_USER")
