"""add_link_full_schema

Revision ID: eebd0dbc6839
Revises: bc4897a9cadd
Create Date: 2024-08-30 17:54:35.609023

"""

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = 'eebd0dbc6839'
down_revision = 'bc4897a9cadd'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('link_new_with_dates', sa.Column('odd', sa.Boolean(), nullable=False), schema='STG_RASPHYSMSU')
    op.add_column('link_new_with_dates', sa.Column('even', sa.Boolean(), nullable=False), schema='STG_RASPHYSMSU')
    op.add_column('link_new_with_dates', sa.Column('weekday', sa.Integer(), nullable=True), schema='STG_RASPHYSMSU')
    op.add_column('link_new_with_dates', sa.Column('num', sa.Integer(), nullable=True), schema='STG_RASPHYSMSU')
    op.add_column(
        'link_new_with_dates', sa.Column('place', sa.ARRAY(sa.Integer()), nullable=False), schema='STG_RASPHYSMSU'
    )
    op.add_column(
        'link_new_with_dates', sa.Column('group', sa.ARRAY(sa.Integer()), nullable=False), schema='STG_RASPHYSMSU'
    )
    op.add_column(
        'link_new_with_dates', sa.Column('teacher', sa.ARRAY(sa.Integer()), nullable=False), schema='STG_RASPHYSMSU'
    )
    op.add_column(
        'link_new_with_dates', sa.Column('events_id', sa.ARRAY(sa.Integer()), nullable=True), schema='STG_RASPHYSMSU'
    )
    op.alter_column(
        'link_new_with_dates', 'subject', existing_type=sa.VARCHAR(), nullable=False, schema='STG_RASPHYSMSU'
    )


def downgrade():
    op.alter_column(
        'link_new_with_dates', 'subject', existing_type=sa.VARCHAR(), nullable=True, schema='STG_RASPHYSMSU'
    )
    op.drop_column('link_new_with_dates', 'events_id', schema='STG_RASPHYSMSU')
    op.drop_column('link_new_with_dates', 'teacher', schema='STG_RASPHYSMSU')
    op.drop_column('link_new_with_dates', 'group', schema='STG_RASPHYSMSU')
    op.drop_column('link_new_with_dates', 'place', schema='STG_RASPHYSMSU')
    op.drop_column('link_new_with_dates', 'num', schema='STG_RASPHYSMSU')
    op.drop_column('link_new_with_dates', 'weekday', schema='STG_RASPHYSMSU')
    op.drop_column('link_new_with_dates', 'even', schema='STG_RASPHYSMSU')
    op.drop_column('link_new_with_dates', 'odd', schema='STG_RASPHYSMSU')
