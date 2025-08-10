"""ods_userdata

Revision ID: dd8e7cd6c56e
Revises: 5345485db41c
Create Date: 2025-08-07 17:13:37.525238

"""

import os

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = 'dd8e7cd6c56e'
down_revision = '5345485db41c'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table_schema("ODS_USERDATA")
    op.create_table(
        'academic_group',
        sa.Column('group', sa.String(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('source', sa.String(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=True),
        sa.Column('modified', sa.DateTime(), nullable=True),
        sa.Column('is_deleted', sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint('group', 'user_id'),
        schema='ODS_USERDATA',
        info={'sensitive': False},
    )
    op.create_table(
        'address',
        sa.Column('address', sa.String(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('source', sa.String(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=True),
        sa.Column('modified', sa.DateTime(), nullable=True),
        sa.Column('is_deleted', sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint('address', 'user_id'),
        schema='ODS_USERDATA',
        info={'sensitive': False},
    )
    op.create_table(
        'birth_city',
        sa.Column('city', sa.String(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('source', sa.String(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=True),
        sa.Column('modified', sa.DateTime(), nullable=True),
        sa.Column('is_deleted', sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint('city', 'user_id'),
        schema='ODS_USERDATA',
        info={'sensitive': False},
    )
    op.create_table(
        'birthday',
        sa.Column('birthday', sa.DateTime(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('source', sa.String(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=True),
        sa.Column('modified', sa.DateTime(), nullable=True),
        sa.Column('is_deleted', sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint('birthday', 'user_id'),
        schema='ODS_USERDATA',
        info={'sensitive': False},
    )
    op.create_table(
        'city',
        sa.Column('city', sa.String(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('source', sa.String(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=True),
        sa.Column('modified', sa.DateTime(), nullable=True),
        sa.Column('is_deleted', sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint('city', 'user_id'),
        schema='ODS_USERDATA',
        info={'sensitive': False},
    )
    op.create_table(
        'department',
        sa.Column('department', sa.String(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('source', sa.String(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=True),
        sa.Column('modified', sa.DateTime(), nullable=True),
        sa.Column('is_deleted', sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint('department', 'user_id'),
        schema='ODS_USERDATA',
        info={'sensitive': False},
    )
    op.create_table(
        'education_form',
        sa.Column('form', sa.String(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('source', sa.String(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=True),
        sa.Column('modified', sa.DateTime(), nullable=True),
        sa.Column('is_deleted', sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint('form', 'user_id'),
        schema='ODS_USERDATA',
        info={'sensitive': False},
    )
    op.create_table(
        'education_level',
        sa.Column('level', sa.String(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('source', sa.String(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=True),
        sa.Column('modified', sa.DateTime(), nullable=True),
        sa.Column('is_deleted', sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint('level', 'user_id'),
        schema='ODS_USERDATA',
        info={'sensitive': False},
    )
    op.create_table(
        'email',
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('source', sa.String(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=True),
        sa.Column('modified', sa.DateTime(), nullable=True),
        sa.Column('is_deleted', sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint('email', 'user_id'),
        schema='ODS_USERDATA',
        info={'sensitive': False},
    )
    op.create_table(
        'faculty',
        sa.Column('faculty', sa.String(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('source', sa.String(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=True),
        sa.Column('modified', sa.DateTime(), nullable=True),
        sa.Column('is_deleted', sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint('faculty', 'user_id'),
        schema='ODS_USERDATA',
        info={'sensitive': False},
    )
    op.create_table(
        'full_name',
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('source', sa.String(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=True),
        sa.Column('modified', sa.DateTime(), nullable=True),
        sa.Column('is_deleted', sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint('name', 'user_id'),
        schema='ODS_USERDATA',
        info={'sensitive': False},
    )
    op.create_table(
        'git_hub_username',
        sa.Column('username', sa.String(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('source', sa.String(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=True),
        sa.Column('modified', sa.DateTime(), nullable=True),
        sa.Column('is_deleted', sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint('username', 'user_id'),
        schema='ODS_USERDATA',
        info={'sensitive': False},
    )
    op.create_table(
        'home_phone_number',
        sa.Column('phone_number', sa.String(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('source', sa.String(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=True),
        sa.Column('modified', sa.DateTime(), nullable=True),
        sa.Column('is_deleted', sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint('phone_number', 'user_id'),
        schema='ODS_USERDATA',
        info={'sensitive': False},
    )
    op.create_table(
        'phone_number',
        sa.Column('phone_number', sa.String(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('source', sa.String(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=True),
        sa.Column('modified', sa.DateTime(), nullable=True),
        sa.Column('is_deleted', sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint('phone_number', 'user_id'),
        schema='ODS_USERDATA',
        info={'sensitive': False},
    )
    op.create_table(
        'photo',
        sa.Column('url', sa.String(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('source', sa.String(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=True),
        sa.Column('modified', sa.DateTime(), nullable=True),
        sa.Column('is_deleted', sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint('url', 'user_id'),
        schema='ODS_USERDATA',
        info={'sensitive': False},
    )
    op.create_table(
        'position',
        sa.Column('position', sa.String(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('source', sa.String(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=True),
        sa.Column('modified', sa.DateTime(), nullable=True),
        sa.Column('is_deleted', sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint('position', 'user_id'),
        schema='ODS_USERDATA',
        info={'sensitive': False},
    )
    op.create_table(
        'sex',
        sa.Column('gender', sa.String(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('source', sa.String(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=True),
        sa.Column('modified', sa.DateTime(), nullable=True),
        sa.Column('is_deleted', sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint('gender', 'user_id'),
        schema='ODS_USERDATA',
        info={'sensitive': False},
    )
    op.create_table(
        'student_id',
        sa.Column('student_id', sa.String(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('source', sa.String(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=True),
        sa.Column('modified', sa.DateTime(), nullable=True),
        sa.Column('is_deleted', sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint('student_id', 'user_id'),
        schema='ODS_USERDATA',
        info={'sensitive': False},
    )
    op.create_table(
        'telegram_username',
        sa.Column('username', sa.String(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('source', sa.String(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=True),
        sa.Column('modified', sa.DateTime(), nullable=True),
        sa.Column('is_deleted', sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint('username', 'user_id'),
        schema='ODS_USERDATA',
        info={'sensitive': False},
    )
    op.create_table(
        'university',
        sa.Column('university', sa.String(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('source', sa.String(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=True),
        sa.Column('modified', sa.DateTime(), nullable=True),
        sa.Column('is_deleted', sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint('university', 'user_id'),
        schema='ODS_USERDATA',
        info={'sensitive': False},
    )
    op.create_table(
        'vk_username',
        sa.Column('username', sa.String(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('source', sa.String(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=True),
        sa.Column('modified', sa.DateTime(), nullable=True),
        sa.Column('is_deleted', sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint('username', 'user_id'),
        schema='ODS_USERDATA',
        info={'sensitive': False},
    )
    op.create_table(
        'workplace',
        sa.Column('workplace', sa.String(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('source', sa.String(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=True),
        sa.Column('modified', sa.DateTime(), nullable=True),
        sa.Column('is_deleted', sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint('workplace', 'user_id'),
        schema='ODS_USERDATA',
        info={'sensitive': False},
    )
    op.create_table(
        'workplace_address',
        sa.Column('address', sa.String(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('source', sa.String(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=True),
        sa.Column('modified', sa.DateTime(), nullable=True),
        sa.Column('is_deleted', sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint('address', 'user_id'),
        schema='ODS_USERDATA',
        info={'sensitive': False},
    )
    op.create_group(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read"
    )
    op.create_group(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write"
    )
    op.create_group(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all"
    )
    op.grant_on_schema(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read",
        "ODS_USERDATA",
    )
    op.grant_on_schema(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write",
        "ODS_USERDATA",
    )
    op.grant_on_schema(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all",
        "ODS_USERDATA",
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read",
        ['SELECT'],
        '"ODS_USERDATA".full_name',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USERDATA".full_name',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all",
        ['ALL'],
        '"ODS_USERDATA".full_name',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read",
        ['SELECT'],
        '"ODS_USERDATA".faculty',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USERDATA".faculty',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all",
        ['ALL'],
        '"ODS_USERDATA".faculty',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read",
        ['SELECT'],
        '"ODS_USERDATA".workplace_address',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USERDATA".workplace_address',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all",
        ['ALL'],
        '"ODS_USERDATA".workplace_address',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read",
        ['SELECT'],
        '"ODS_USERDATA".email',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USERDATA".email',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all",
        ['ALL'],
        '"ODS_USERDATA".email',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read",
        ['SELECT'],
        '"ODS_USERDATA".address',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USERDATA".address',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all",
        ['ALL'],
        '"ODS_USERDATA".address',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read",
        ['SELECT'],
        '"ODS_USERDATA".workplace',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USERDATA".workplace',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all",
        ['ALL'],
        '"ODS_USERDATA".workplace',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read",
        ['SELECT'],
        '"ODS_USERDATA".education_form',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USERDATA".education_form',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all",
        ['ALL'],
        '"ODS_USERDATA".education_form',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read",
        ['SELECT'],
        '"ODS_USERDATA".birth_city',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USERDATA".birth_city',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all",
        ['ALL'],
        '"ODS_USERDATA".birth_city',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read",
        ['SELECT'],
        '"ODS_USERDATA".university',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USERDATA".university',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all",
        ['ALL'],
        '"ODS_USERDATA".university',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read",
        ['SELECT'],
        '"ODS_USERDATA".department',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USERDATA".department',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all",
        ['ALL'],
        '"ODS_USERDATA".department',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read",
        ['SELECT'],
        '"ODS_USERDATA".city',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USERDATA".city',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all",
        ['ALL'],
        '"ODS_USERDATA".city',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read",
        ['SELECT'],
        '"ODS_USERDATA".education_level',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USERDATA".education_level',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all",
        ['ALL'],
        '"ODS_USERDATA".education_level',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read",
        ['SELECT'],
        '"ODS_USERDATA".sex',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USERDATA".sex',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all",
        ['ALL'],
        '"ODS_USERDATA".sex',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read",
        ['SELECT'],
        '"ODS_USERDATA".academic_group',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USERDATA".academic_group',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all",
        ['ALL'],
        '"ODS_USERDATA".academic_group',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read",
        ['SELECT'],
        '"ODS_USERDATA".git_hub_username',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USERDATA".git_hub_username',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all",
        ['ALL'],
        '"ODS_USERDATA".git_hub_username',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read",
        ['SELECT'],
        '"ODS_USERDATA".home_phone_number',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USERDATA".home_phone_number',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all",
        ['ALL'],
        '"ODS_USERDATA".home_phone_number',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read",
        ['SELECT'],
        '"ODS_USERDATA".student_id',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USERDATA".student_id',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all",
        ['ALL'],
        '"ODS_USERDATA".student_id',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read",
        ['SELECT'],
        '"ODS_USERDATA".photo',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USERDATA".photo',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all",
        ['ALL'],
        '"ODS_USERDATA".photo',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read",
        ['SELECT'],
        '"ODS_USERDATA".vk_username',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USERDATA".vk_username',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all",
        ['ALL'],
        '"ODS_USERDATA".vk_username',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read",
        ['SELECT'],
        '"ODS_USERDATA".position',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USERDATA".position',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all",
        ['ALL'],
        '"ODS_USERDATA".position',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read",
        ['SELECT'],
        '"ODS_USERDATA".telegram_username',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USERDATA".telegram_username',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all",
        ['ALL'],
        '"ODS_USERDATA".telegram_username',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read",
        ['SELECT'],
        '"ODS_USERDATA".phone_number',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USERDATA".phone_number',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all",
        ['ALL'],
        '"ODS_USERDATA".phone_number',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read",
        ['SELECT'],
        '"ODS_USERDATA".birthday',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USERDATA".birthday',
    )
    op.grant_on_table(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all",
        ['ALL'],
        '"ODS_USERDATA".birthday',
    )
    op.drop_column('union_member', 'card', schema='STG_UNION_MEMBER')


def downgrade():
    op.add_column(
        'union_member', sa.Column('card', sa.VARCHAR(), autoincrement=False, nullable=True), schema='STG_UNION_MEMBER'
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all",
        ['ALL'],
        '"ODS_USERDATA".birthday',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USERDATA".birthday',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read",
        ['SELECT'],
        '"ODS_USERDATA".birthday',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all",
        ['ALL'],
        '"ODS_USERDATA".phone_number',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USERDATA".phone_number',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read",
        ['SELECT'],
        '"ODS_USERDATA".phone_number',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all",
        ['ALL'],
        '"ODS_USERDATA".telegram_username',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USERDATA".telegram_username',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read",
        ['SELECT'],
        '"ODS_USERDATA".telegram_username',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all",
        ['ALL'],
        '"ODS_USERDATA".position',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USERDATA".position',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read",
        ['SELECT'],
        '"ODS_USERDATA".position',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all",
        ['ALL'],
        '"ODS_USERDATA".vk_username',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USERDATA".vk_username',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read",
        ['SELECT'],
        '"ODS_USERDATA".vk_username',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all",
        ['ALL'],
        '"ODS_USERDATA".photo',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USERDATA".photo',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read",
        ['SELECT'],
        '"ODS_USERDATA".photo',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all",
        ['ALL'],
        '"ODS_USERDATA".student_id',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USERDATA".student_id',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read",
        ['SELECT'],
        '"ODS_USERDATA".student_id',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all",
        ['ALL'],
        '"ODS_USERDATA".home_phone_number',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USERDATA".home_phone_number',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read",
        ['SELECT'],
        '"ODS_USERDATA".home_phone_number',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all",
        ['ALL'],
        '"ODS_USERDATA".git_hub_username',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USERDATA".git_hub_username',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read",
        ['SELECT'],
        '"ODS_USERDATA".git_hub_username',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all",
        ['ALL'],
        '"ODS_USERDATA".academic_group',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USERDATA".academic_group',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read",
        ['SELECT'],
        '"ODS_USERDATA".academic_group',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all",
        ['ALL'],
        '"ODS_USERDATA".sex',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USERDATA".sex',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read",
        ['SELECT'],
        '"ODS_USERDATA".sex',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all",
        ['ALL'],
        '"ODS_USERDATA".education_level',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USERDATA".education_level',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read",
        ['SELECT'],
        '"ODS_USERDATA".education_level',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all",
        ['ALL'],
        '"ODS_USERDATA".city',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USERDATA".city',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read",
        ['SELECT'],
        '"ODS_USERDATA".city',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all",
        ['ALL'],
        '"ODS_USERDATA".department',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USERDATA".department',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read",
        ['SELECT'],
        '"ODS_USERDATA".department',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all",
        ['ALL'],
        '"ODS_USERDATA".university',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USERDATA".university',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read",
        ['SELECT'],
        '"ODS_USERDATA".university',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all",
        ['ALL'],
        '"ODS_USERDATA".birth_city',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USERDATA".birth_city',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read",
        ['SELECT'],
        '"ODS_USERDATA".birth_city',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all",
        ['ALL'],
        '"ODS_USERDATA".education_form',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USERDATA".education_form',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read",
        ['SELECT'],
        '"ODS_USERDATA".education_form',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all",
        ['ALL'],
        '"ODS_USERDATA".workplace',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USERDATA".workplace',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read",
        ['SELECT'],
        '"ODS_USERDATA".workplace',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all",
        ['ALL'],
        '"ODS_USERDATA".address',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USERDATA".address',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read",
        ['SELECT'],
        '"ODS_USERDATA".address',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all",
        ['ALL'],
        '"ODS_USERDATA".email',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USERDATA".email',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read",
        ['SELECT'],
        '"ODS_USERDATA".email',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all",
        ['ALL'],
        '"ODS_USERDATA".workplace_address',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USERDATA".workplace_address',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read",
        ['SELECT'],
        '"ODS_USERDATA".workplace_address',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all",
        ['ALL'],
        '"ODS_USERDATA".faculty',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USERDATA".faculty',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read",
        ['SELECT'],
        '"ODS_USERDATA".faculty',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all",
        ['ALL'],
        '"ODS_USERDATA".full_name',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USERDATA".full_name',
    )
    op.revoke_on_table(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read",
        ['SELECT'],
        '"ODS_USERDATA".full_name',
    )
    op.revoke_on_schema(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all",
        "ODS_USERDATA",
    )
    op.revoke_on_schema(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write",
        "ODS_USERDATA",
    )
    op.revoke_on_schema(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read",
        "ODS_USERDATA",
    )
    op.drop_table('workplace_address', schema='ODS_USERDATA')
    op.drop_table('workplace', schema='ODS_USERDATA')
    op.drop_table('vk_username', schema='ODS_USERDATA')
    op.drop_table('university', schema='ODS_USERDATA')
    op.drop_table('telegram_username', schema='ODS_USERDATA')
    op.drop_table('student_id', schema='ODS_USERDATA')
    op.drop_table('sex', schema='ODS_USERDATA')
    op.drop_table('position', schema='ODS_USERDATA')
    op.drop_table('photo', schema='ODS_USERDATA')
    op.drop_table('phone_number', schema='ODS_USERDATA')
    op.drop_table('home_phone_number', schema='ODS_USERDATA')
    op.drop_table('git_hub_username', schema='ODS_USERDATA')
    op.drop_table('full_name', schema='ODS_USERDATA')
    op.drop_table('faculty', schema='ODS_USERDATA')
    op.drop_table('email', schema='ODS_USERDATA')
    op.drop_table('education_level', schema='ODS_USERDATA')
    op.drop_table('education_form', schema='ODS_USERDATA')
    op.drop_table('department', schema='ODS_USERDATA')
    op.drop_table('city', schema='ODS_USERDATA')
    op.drop_table('birthday', schema='ODS_USERDATA')
    op.drop_table('birth_city', schema='ODS_USERDATA')
    op.drop_table('address', schema='ODS_USERDATA')
    op.drop_table('academic_group', schema='ODS_USERDATA')
    op.delete_group(
        "test_dwh_ods_userdata_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_all"
    )
    op.delete_group(
        "test_dwh_ods_userdata_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_write"
    )
    op.delete_group(
        "test_dwh_ods_userdata_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_userdata_read"
    )
    op.drop_table_schema("ODS_USERDATA")
