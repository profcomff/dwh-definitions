"""added DWH_USER_INFO.info encrypted version

Revision ID: 00dc9eb31a18
Revises: 7baa38ad06f1
Create Date: 2025-04-26 17:10:05.618378

"""

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '00dc9eb31a18'
down_revision = '7baa38ad06f1'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'encrypted_info',
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('email', sa.LargeBinary(), nullable=True, comment="user's email from ods user info"),
        sa.Column('phone_number', sa.LargeBinary(), nullable=True, comment="user's phone_number from ods user info"),
        sa.Column('vk_name', sa.LargeBinary(), nullable=True, comment="user's vk_name from ods user info"),
        sa.Column('city', sa.LargeBinary(), nullable=True, comment="user's city from ods uder info"),
        sa.Column('hometown', sa.LargeBinary(), nullable=True, comment="user's hometown from ods user info"),
        sa.Column('location', sa.LargeBinary(), nullable=True, comment="user's current city from ods user info"),
        sa.Column('github_name', sa.LargeBinary(), nullable=True, comment="user's github_name from ods user info"),
        sa.Column('telegram_name', sa.LargeBinary(), nullable=True, comment="user's telegram_name from ods user info"),
        sa.Column(
            'home_phone_number', sa.LargeBinary(), nullable=True, comment="user's home_phone_number from ods user info"
        ),
        sa.Column(
            'education_level', sa.LargeBinary(), nullable=True, comment='Bachelor/Master/Specialist from ods user info'
        ),
        sa.Column('university', sa.LargeBinary(), nullable=True, comment="user's university from ods user info"),
        sa.Column('group', sa.LargeBinary(), nullable=True, comment="user's group from ods user info"),
        sa.Column('faculty', sa.LargeBinary(), nullable=True, comment="user's faculty from ods user info"),
        sa.Column(
            'position', sa.LargeBinary(), nullable=True, comment="user's position in university from ods user info"
        ),
        sa.Column(
            'student_id_number', sa.LargeBinary(), nullable=True, comment="user's student_id_number from ods user info"
        ),
        sa.Column(
            'department', sa.LargeBinary(), nullable=True, comment="user's department in university from ods user info"
        ),
        sa.Column(
            'mode_of_study',
            sa.LargeBinary(),
            nullable=True,
            comment='full-time/correspondence education from ods user info',
        ),
        sa.Column('full_name', sa.LargeBinary(), nullable=True, comment="user's full_name from ods user info"),
        sa.Column('birth_date', sa.LargeBinary(), nullable=True, comment="user's birth_date from ods user info"),
        sa.Column('photo', sa.LargeBinary(), nullable=True, comment="user's photo(https://) from ods user info"),
        sa.Column('sex', sa.LargeBinary(), nullable=True, comment='male/female from ods user info'),
        sa.Column('job', sa.LargeBinary(), nullable=True, comment="user's job from ods user info"),
        sa.Column('work_location', sa.LargeBinary(), nullable=True, comment="user's work_location from ods uder info"),
        sa.PrimaryKeyConstraint('user_id'),
        schema='DWH_USER_INFO',
        info={'sensitive': False},
    )
    op.create_index(
        op.f('ix_DWH_USER_INFO_encrypted_info_user_id'),
        'encrypted_info',
        ['user_id'],
        unique=False,
        schema='DWH_USER_INFO',
    )
    op.alter_column(
        'info_keys',
        'id',
        existing_type=sa.INTEGER(),
        comment='key id (maps to)',
        existing_nullable=False,
        autoincrement=True,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'info_keys',
        'key',
        existing_type=sa.TEXT(),
        type_=sa.String(),
        comment='symmetric encryption key',
        existing_nullable=False,
        schema='STG_USERDATA',
    )


def downgrade():
    op.alter_column(
        'info_keys',
        'key',
        existing_type=sa.String(),
        type_=sa.TEXT(),
        comment=None,
        existing_comment='symmetric encryption key',
        existing_nullable=False,
        schema='STG_USERDATA',
    )
    op.alter_column(
        'info_keys',
        'id',
        existing_type=sa.INTEGER(),
        comment=None,
        existing_comment='key id (maps to)',
        existing_nullable=False,
        autoincrement=True,
        schema='STG_USERDATA',
    )
    op.drop_index(op.f('ix_DWH_USER_INFO_encrypted_info_user_id'), table_name='encrypted_info', schema='DWH_USER_INFO')
    op.drop_table('encrypted_info', schema='DWH_USER_INFO')
