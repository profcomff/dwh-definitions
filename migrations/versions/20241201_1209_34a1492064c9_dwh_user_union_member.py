"""dwh.user.union_member

Revision ID: 34a1492064c9
Revises: 4662fc16ccde
Create Date: 2024-12-01 12:09:12.184468

"""

import os

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '34a1492064c9'
down_revision = '4662fc16ccde'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'union_member',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column(
            'full_name',
            sa.String(),
            nullable=True,
            comment="full_name - matched user's full names from ODS.user.info and STG.union_member.union_member",
        ),
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
        sa.PrimaryKeyConstraint('id'),
        schema='DWH_USER_INFO',
    )
    op.create_index(
        op.f('ix_DWH_USER_INFO_union_member_id'), 'union_member', ['id'], unique=False, schema='DWH_USER_INFO'
    )
    op.grant_on_table(
        "test_dwh_dwh_user_info_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_user_info_read",
        ['SELECT'],
        '"DWH_USER_INFO".union_member',
    )
    op.grant_on_table(
        "test_dwh_dwh_user_info_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_user_info_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DWH_USER_INFO".union_member',
    )
    op.grant_on_table(
        "test_dwh_dwh_user_info_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_user_info_all",
        ['ALL'],
        '"DWH_USER_INFO".union_member',
    )
    op.alter_column(
        'info',
        'email',
        existing_type=sa.VARCHAR(),
        comment="user's email from ods user info",
        existing_nullable=True,
        schema='DWH_USER_INFO',
    )
    op.alter_column(
        'info',
        'phone_number',
        existing_type=sa.VARCHAR(),
        comment="user's phone_number from ods user info",
        existing_nullable=True,
        schema='DWH_USER_INFO',
    )
    op.alter_column(
        'info',
        'vk_name',
        existing_type=sa.VARCHAR(),
        comment="user's vk_name from ods user info",
        existing_nullable=True,
        schema='DWH_USER_INFO',
    )
    op.alter_column(
        'info',
        'city',
        existing_type=sa.VARCHAR(),
        comment="user's city from ods uder info",
        existing_nullable=True,
        schema='DWH_USER_INFO',
    )
    op.alter_column(
        'info',
        'hometown',
        existing_type=sa.VARCHAR(),
        comment="user's hometown from ods user info",
        existing_nullable=True,
        schema='DWH_USER_INFO',
    )
    op.alter_column(
        'info',
        'location',
        existing_type=sa.VARCHAR(),
        comment="user's current city from ods user info",
        existing_nullable=True,
        schema='DWH_USER_INFO',
    )
    op.alter_column(
        'info',
        'github_name',
        existing_type=sa.VARCHAR(),
        comment="user's github_name from ods user info",
        existing_nullable=True,
        schema='DWH_USER_INFO',
    )
    op.alter_column(
        'info',
        'telegram_name',
        existing_type=sa.VARCHAR(),
        comment="user's telegram_name from ods user info",
        existing_nullable=True,
        schema='DWH_USER_INFO',
    )
    op.alter_column(
        'info',
        'home_phone_number',
        existing_type=sa.VARCHAR(),
        comment="user's home_phone_number from ods user info",
        existing_nullable=True,
        schema='DWH_USER_INFO',
    )
    op.alter_column(
        'info',
        'education_level',
        existing_type=sa.VARCHAR(),
        comment='Bachelor/Master/Specialist from ods user info',
        existing_nullable=True,
        schema='DWH_USER_INFO',
    )
    op.alter_column(
        'info',
        'university',
        existing_type=sa.VARCHAR(),
        comment="user's university from ods user info",
        existing_nullable=True,
        schema='DWH_USER_INFO',
    )
    op.alter_column(
        'info',
        'group',
        existing_type=sa.VARCHAR(),
        comment="user's group from ods user info",
        existing_nullable=True,
        schema='DWH_USER_INFO',
    )
    op.alter_column(
        'info',
        'faculty',
        existing_type=sa.VARCHAR(),
        comment="user's faculty from ods user info",
        existing_nullable=True,
        schema='DWH_USER_INFO',
    )
    op.alter_column(
        'info',
        'position',
        existing_type=sa.VARCHAR(),
        comment="user's position in university from ods user info",
        existing_nullable=True,
        schema='DWH_USER_INFO',
    )
    op.alter_column(
        'info',
        'student_id_number',
        existing_type=sa.VARCHAR(),
        comment="user's student_id_number from ods user info",
        existing_nullable=True,
        schema='DWH_USER_INFO',
    )
    op.alter_column(
        'info',
        'department',
        existing_type=sa.VARCHAR(),
        comment="user's department in university from ods user info",
        existing_nullable=True,
        schema='DWH_USER_INFO',
    )
    op.alter_column(
        'info',
        'mode_of_study',
        existing_type=sa.VARCHAR(),
        comment='full-time/correspondence education from ods user info',
        existing_nullable=True,
        schema='DWH_USER_INFO',
    )
    op.alter_column(
        'info',
        'full_name',
        existing_type=sa.VARCHAR(),
        comment="user's full_name from ods user info",
        existing_nullable=True,
        schema='DWH_USER_INFO',
    )
    op.alter_column(
        'info',
        'birth_date',
        existing_type=sa.VARCHAR(),
        comment="user's birth_date from ods user info",
        existing_nullable=True,
        schema='DWH_USER_INFO',
    )
    op.alter_column(
        'info',
        'photo',
        existing_type=sa.VARCHAR(),
        comment="user's photo(https://) from ods user info",
        existing_nullable=True,
        schema='DWH_USER_INFO',
    )
    op.alter_column(
        'info',
        'sex',
        existing_type=sa.VARCHAR(),
        comment='male/female from ods user info',
        existing_nullable=True,
        schema='DWH_USER_INFO',
    )
    op.alter_column(
        'info',
        'job',
        existing_type=sa.VARCHAR(),
        comment="user's job from ods user info",
        existing_nullable=True,
        schema='DWH_USER_INFO',
    )
    op.alter_column(
        'info',
        'work_location',
        existing_type=sa.VARCHAR(),
        comment="user's work_location from ods uder info",
        existing_nullable=True,
        schema='DWH_USER_INFO',
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        'info',
        'work_location',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment="user's work_location from ods uder info",
        existing_nullable=True,
        schema='DWH_USER_INFO',
    )
    op.alter_column(
        'info',
        'job',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment="user's job from ods user info",
        existing_nullable=True,
        schema='DWH_USER_INFO',
    )
    op.alter_column(
        'info',
        'sex',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='male/female from ods user info',
        existing_nullable=True,
        schema='DWH_USER_INFO',
    )
    op.alter_column(
        'info',
        'photo',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment="user's photo(https://) from ods user info",
        existing_nullable=True,
        schema='DWH_USER_INFO',
    )
    op.alter_column(
        'info',
        'birth_date',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment="user's birth_date from ods user info",
        existing_nullable=True,
        schema='DWH_USER_INFO',
    )
    op.alter_column(
        'info',
        'full_name',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment="user's full_name from ods user info",
        existing_nullable=True,
        schema='DWH_USER_INFO',
    )
    op.alter_column(
        'info',
        'mode_of_study',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='full-time/correspondence education from ods user info',
        existing_nullable=True,
        schema='DWH_USER_INFO',
    )
    op.alter_column(
        'info',
        'department',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment="user's department in university from ods user info",
        existing_nullable=True,
        schema='DWH_USER_INFO',
    )
    op.alter_column(
        'info',
        'student_id_number',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment="user's student_id_number from ods user info",
        existing_nullable=True,
        schema='DWH_USER_INFO',
    )
    op.alter_column(
        'info',
        'position',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment="user's position in university from ods user info",
        existing_nullable=True,
        schema='DWH_USER_INFO',
    )
    op.alter_column(
        'info',
        'faculty',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment="user's faculty from ods user info",
        existing_nullable=True,
        schema='DWH_USER_INFO',
    )
    op.alter_column(
        'info',
        'group',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment="user's group from ods user info",
        existing_nullable=True,
        schema='DWH_USER_INFO',
    )
    op.alter_column(
        'info',
        'university',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment="user's university from ods user info",
        existing_nullable=True,
        schema='DWH_USER_INFO',
    )
    op.alter_column(
        'info',
        'education_level',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Bachelor/Master/Specialist from ods user info',
        existing_nullable=True,
        schema='DWH_USER_INFO',
    )
    op.alter_column(
        'info',
        'home_phone_number',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment="user's home_phone_number from ods user info",
        existing_nullable=True,
        schema='DWH_USER_INFO',
    )
    op.alter_column(
        'info',
        'telegram_name',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment="user's telegram_name from ods user info",
        existing_nullable=True,
        schema='DWH_USER_INFO',
    )
    op.alter_column(
        'info',
        'github_name',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment="user's github_name from ods user info",
        existing_nullable=True,
        schema='DWH_USER_INFO',
    )
    op.alter_column(
        'info',
        'location',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment="user's current city from ods user info",
        existing_nullable=True,
        schema='DWH_USER_INFO',
    )
    op.alter_column(
        'info',
        'hometown',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment="user's hometown from ods user info",
        existing_nullable=True,
        schema='DWH_USER_INFO',
    )
    op.alter_column(
        'info',
        'city',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment="user's city from ods uder info",
        existing_nullable=True,
        schema='DWH_USER_INFO',
    )
    op.alter_column(
        'info',
        'vk_name',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment="user's vk_name from ods user info",
        existing_nullable=True,
        schema='DWH_USER_INFO',
    )
    op.alter_column(
        'info',
        'phone_number',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment="user's phone_number from ods user info",
        existing_nullable=True,
        schema='DWH_USER_INFO',
    )
    op.alter_column(
        'info',
        'email',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment="user's email from ods user info",
        existing_nullable=True,
        schema='DWH_USER_INFO',
    )
    op.revoke_on_table(
        "test_dwh_dwh_user_info_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_user_info_all",
        ['ALL'],
        '"DWH_USER_INFO".union_member',
    )
    op.revoke_on_table(
        "test_dwh_dwh_user_info_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_user_info_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DWH_USER_INFO".union_member',
    )
    op.revoke_on_table(
        "test_dwh_dwh_user_info_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_user_info_read",
        ['SELECT'],
        '"DWH_USER_INFO".union_member',
    )
    op.drop_index(op.f('ix_DWH_USER_INFO_union_member_id'), table_name='union_member', schema='DWH_USER_INFO')
    op.drop_table('union_member', schema='DWH_USER_INFO')
    # ### end Alembic commands ###
