"""added auth_email into DWH_USER.info

Revision ID: d47cdc452c99
Revises: cbf45dd211c7
Create Date: 2024-11-30 19:06:03.629971

"""

import sqlalchemy as sa
from alembic import op


revision = 'd47cdc452c99'
down_revision = 'cbf45dd211c7'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'info',
        sa.Column('auth_email', sa.String(), nullable=False, comment='email used for authentication'),
        schema='DWH_AUTH_USER',
    )
    op.alter_column(
        'info',
        'email',
        existing_type=sa.VARCHAR(),
        comment='email from stg userdata',
        existing_comment="user's email from stg userdata",
        existing_nullable=True,
        schema='DWH_AUTH_USER',
    )
    op.alter_column(
        'info',
        'phone_number',
        existing_type=sa.VARCHAR(),
        comment='phone_number from stg userdata',
        existing_comment="user's phone_number from stg userdata",
        existing_nullable=True,
        schema='DWH_AUTH_USER',
    )
    op.alter_column(
        'info',
        'vk_name',
        existing_type=sa.VARCHAR(),
        comment='vk_name from stg userdata',
        existing_comment="user's vk_name from stg userdata",
        existing_nullable=True,
        schema='DWH_AUTH_USER',
    )
    op.alter_column(
        'info',
        'city',
        existing_type=sa.VARCHAR(),
        comment='city from stg userdata',
        existing_comment="user's city from stg userdata",
        existing_nullable=True,
        schema='DWH_AUTH_USER',
    )
    op.alter_column(
        'info',
        'hometown',
        existing_type=sa.VARCHAR(),
        comment='hometown from stg userdata',
        existing_comment="user's hometown from stg userdata",
        existing_nullable=True,
        schema='DWH_AUTH_USER',
    )
    op.alter_column(
        'info',
        'location',
        existing_type=sa.VARCHAR(),
        comment='current city from stg userdata',
        existing_comment="user's current city from stg userdata",
        existing_nullable=True,
        schema='DWH_AUTH_USER',
    )
    op.alter_column(
        'info',
        'github_name',
        existing_type=sa.VARCHAR(),
        comment='github_name from stg userdata',
        existing_comment="user's github_name from stg userdata",
        existing_nullable=True,
        schema='DWH_AUTH_USER',
    )
    op.alter_column(
        'info',
        'telegram_name',
        existing_type=sa.VARCHAR(),
        comment='telegram_name stg userdata',
        existing_comment="user's telegram_name stg userdata",
        existing_nullable=True,
        schema='DWH_AUTH_USER',
    )
    op.alter_column(
        'info',
        'home_phone_number',
        existing_type=sa.VARCHAR(),
        comment='home_phone_number from stg userdata',
        existing_comment="user's home_phone_number from stg userdata",
        existing_nullable=True,
        schema='DWH_AUTH_USER',
    )
    op.alter_column(
        'info',
        'university',
        existing_type=sa.VARCHAR(),
        comment='university from stg userdata',
        existing_comment="user's university from stg userdata",
        existing_nullable=True,
        schema='DWH_AUTH_USER',
    )
    op.alter_column(
        'info',
        'group',
        existing_type=sa.VARCHAR(),
        comment='group from stg userdata',
        existing_comment="user's group from stg userdata",
        existing_nullable=True,
        schema='DWH_AUTH_USER',
    )
    op.alter_column(
        'info',
        'faculty',
        existing_type=sa.VARCHAR(),
        comment='faculty from stg userdata',
        existing_comment="user's faculty from stg userdata",
        existing_nullable=True,
        schema='DWH_AUTH_USER',
    )
    op.alter_column(
        'info',
        'position',
        existing_type=sa.VARCHAR(),
        comment='position in university from stg userdata',
        existing_comment="user's position in university from stg userdata",
        existing_nullable=True,
        schema='DWH_AUTH_USER',
    )
    op.alter_column(
        'info',
        'student_id_number',
        existing_type=sa.VARCHAR(),
        comment='student_id_number from stg userdata',
        existing_comment="user's student_id_number from stg userdata",
        existing_nullable=True,
        schema='DWH_AUTH_USER',
    )
    op.alter_column(
        'info',
        'department',
        existing_type=sa.VARCHAR(),
        comment='department in university from stg userdata',
        existing_comment="user's department in university from stg userdata",
        existing_nullable=True,
        schema='DWH_AUTH_USER',
    )
    op.alter_column(
        'info',
        'full_name',
        existing_type=sa.VARCHAR(),
        comment='full_name from stg userdata',
        existing_comment="user's full_name from stg userdata",
        existing_nullable=True,
        schema='DWH_AUTH_USER',
    )
    op.alter_column(
        'info',
        'birth_date',
        existing_type=sa.VARCHAR(),
        comment='birth_date from stg userdata',
        existing_comment="user's birth_date from stg userdata",
        existing_nullable=True,
        schema='DWH_AUTH_USER',
    )
    op.alter_column(
        'info',
        'photo',
        existing_type=sa.VARCHAR(),
        comment='photo (URL) from stg userdata',
        existing_comment="user's photo(https://) from stg userdata",
        existing_nullable=True,
        schema='DWH_AUTH_USER',
    )
    op.alter_column(
        'info',
        'job',
        existing_type=sa.VARCHAR(),
        comment='job from stg userdata',
        existing_comment="user's job from stg userdata",
        existing_nullable=True,
        schema='DWH_AUTH_USER',
    )
    op.alter_column(
        'info',
        'work_location',
        existing_type=sa.VARCHAR(),
        comment='work_location from stg userdata',
        existing_comment="user's work_location from stg userdata",
        existing_nullable=True,
        schema='DWH_AUTH_USER',
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        'info',
        'work_location',
        existing_type=sa.VARCHAR(),
        comment="user's work_location from stg userdata",
        existing_comment='work_location from stg userdata',
        existing_nullable=True,
        schema='DWH_AUTH_USER',
    )
    op.alter_column(
        'info',
        'job',
        existing_type=sa.VARCHAR(),
        comment="user's job from stg userdata",
        existing_comment='job from stg userdata',
        existing_nullable=True,
        schema='DWH_AUTH_USER',
    )
    op.alter_column(
        'info',
        'photo',
        existing_type=sa.VARCHAR(),
        comment="user's photo(https://) from stg userdata",
        existing_comment='photo (URL) from stg userdata',
        existing_nullable=True,
        schema='DWH_AUTH_USER',
    )
    op.alter_column(
        'info',
        'birth_date',
        existing_type=sa.VARCHAR(),
        comment="user's birth_date from stg userdata",
        existing_comment='birth_date from stg userdata',
        existing_nullable=True,
        schema='DWH_AUTH_USER',
    )
    op.alter_column(
        'info',
        'full_name',
        existing_type=sa.VARCHAR(),
        comment="user's full_name from stg userdata",
        existing_comment='full_name from stg userdata',
        existing_nullable=True,
        schema='DWH_AUTH_USER',
    )
    op.alter_column(
        'info',
        'department',
        existing_type=sa.VARCHAR(),
        comment="user's department in university from stg userdata",
        existing_comment='department in university from stg userdata',
        existing_nullable=True,
        schema='DWH_AUTH_USER',
    )
    op.alter_column(
        'info',
        'student_id_number',
        existing_type=sa.VARCHAR(),
        comment="user's student_id_number from stg userdata",
        existing_comment='student_id_number from stg userdata',
        existing_nullable=True,
        schema='DWH_AUTH_USER',
    )
    op.alter_column(
        'info',
        'position',
        existing_type=sa.VARCHAR(),
        comment="user's position in university from stg userdata",
        existing_comment='position in university from stg userdata',
        existing_nullable=True,
        schema='DWH_AUTH_USER',
    )
    op.alter_column(
        'info',
        'faculty',
        existing_type=sa.VARCHAR(),
        comment="user's faculty from stg userdata",
        existing_comment='faculty from stg userdata',
        existing_nullable=True,
        schema='DWH_AUTH_USER',
    )
    op.alter_column(
        'info',
        'group',
        existing_type=sa.VARCHAR(),
        comment="user's group from stg userdata",
        existing_comment='group from stg userdata',
        existing_nullable=True,
        schema='DWH_AUTH_USER',
    )
    op.alter_column(
        'info',
        'university',
        existing_type=sa.VARCHAR(),
        comment="user's university from stg userdata",
        existing_comment='university from stg userdata',
        existing_nullable=True,
        schema='DWH_AUTH_USER',
    )
    op.alter_column(
        'info',
        'home_phone_number',
        existing_type=sa.VARCHAR(),
        comment="user's home_phone_number from stg userdata",
        existing_comment='home_phone_number from stg userdata',
        existing_nullable=True,
        schema='DWH_AUTH_USER',
    )
    op.alter_column(
        'info',
        'telegram_name',
        existing_type=sa.VARCHAR(),
        comment="user's telegram_name stg userdata",
        existing_comment='telegram_name stg userdata',
        existing_nullable=True,
        schema='DWH_AUTH_USER',
    )
    op.alter_column(
        'info',
        'github_name',
        existing_type=sa.VARCHAR(),
        comment="user's github_name from stg userdata",
        existing_comment='github_name from stg userdata',
        existing_nullable=True,
        schema='DWH_AUTH_USER',
    )
    op.alter_column(
        'info',
        'location',
        existing_type=sa.VARCHAR(),
        comment="user's current city from stg userdata",
        existing_comment='current city from stg userdata',
        existing_nullable=True,
        schema='DWH_AUTH_USER',
    )
    op.alter_column(
        'info',
        'hometown',
        existing_type=sa.VARCHAR(),
        comment="user's hometown from stg userdata",
        existing_comment='hometown from stg userdata',
        existing_nullable=True,
        schema='DWH_AUTH_USER',
    )
    op.alter_column(
        'info',
        'city',
        existing_type=sa.VARCHAR(),
        comment="user's city from stg userdata",
        existing_comment='city from stg userdata',
        existing_nullable=True,
        schema='DWH_AUTH_USER',
    )
    op.alter_column(
        'info',
        'vk_name',
        existing_type=sa.VARCHAR(),
        comment="user's vk_name from stg userdata",
        existing_comment='vk_name from stg userdata',
        existing_nullable=True,
        schema='DWH_AUTH_USER',
    )
    op.alter_column(
        'info',
        'phone_number',
        existing_type=sa.VARCHAR(),
        comment="user's phone_number from stg userdata",
        existing_comment='phone_number from stg userdata',
        existing_nullable=True,
        schema='DWH_AUTH_USER',
    )
    op.alter_column(
        'info',
        'email',
        existing_type=sa.VARCHAR(),
        comment="user's email from stg userdata",
        existing_comment='email from stg userdata',
        existing_nullable=True,
        schema='DWH_AUTH_USER',
    )
    op.drop_column('info', 'auth_email', schema='DWH_AUTH_USER')
