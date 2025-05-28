"""dm_rental_fix_table

Revision ID: d1a22199f353
Revises: b259a3b8c31d
Create Date: 2025-05-28 18:02:42.798163

"""

import os

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = 'd1a22199f353'
down_revision = 'b259a3b8c31d'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_column("dm_rentals_events", "duration", schema="DM_RENTAL")
    op.drop_column("dm_rentals_events", "delay", schema="DM_RENTAL")
    op.drop_column("dm_rentals_events", "overdue_flag", schema="DM_RENTAL")
    op.drop_column("dm_rentals_events", "conversion_flag", schema="DM_RENTAL")
    op.drop_column("dm_rentals_events", "available_items", schema="DM_RENTAL")
    op.drop_column("dm_rentals_events", "total_items", schema="DM_RENTAL")
    op.drop_column("dm_rentals_events", "rental_count", schema="DM_RENTAL")
    op.drop_column("dm_rentals_events", "avg_downtime_hours", schema="DM_RENTAL")
    op.drop_column("dm_rentals_events", "avg_rent_hours", schema="DM_RENTAL")
    op.drop_column("dm_rentals_events", "strike_count", schema="DM_RENTAL")
    op.drop_column("dm_rentals_events", "activity_max_time", schema="DM_RENTAL")
    op.drop_column("dm_rentals_events", "activity_max", schema="DM_RENTAL")
    op.drop_column("dm_rentals_events", "type", schema="DM_RENTAL")


def downgrade():
    op.add_column("dm_rentals_events", sa.Column("duration", sa.Interval()), schema="DM_RENTAL")
    op.add_column("dm_rentals_events", sa.Column("delay", sa.Interval()), schema="DM_RENTAL")
    op.add_column("dm_rentals_events", sa.Column("overdue_flag", sa.Boolean()), schema="DM_RENTAL")
    op.add_column("dm_rentals_events", sa.Column("conversion_flag", sa.Boolean()), schema="DM_RENTAL")
    op.add_column("dm_rentals_events", sa.Column("available_items", sa.Integer()), schema="DM_RENTAL")
    op.add_column("dm_rentals_events", sa.Column("total_items", sa.Integer()), schema="DM_RENTAL")
    op.add_column("dm_rentals_events", sa.Column("rental_count", sa.Integer()), schema="DM_RENTAL")
    op.add_column("dm_rentals_events", sa.Column("avg_downtime_hours", sa.Interval()), schema="DM_RENTAL")
    op.add_column("dm_rentals_events", sa.Column("avg_rent_hours", sa.Interval()), schema="DM_RENTAL")
    op.add_column("dm_rentals_events", sa.Column("strike_count", sa.Integer()), schema="DM_RENTAL")
    op.add_column("dm_rentals_events", sa.Column("activity_max_time", sa.Integer()), schema="DM_RENTAL")
    op.add_column("dm_rentals_events", sa.Column("activity_max", sa.Integer()), schema="DM_RENTAL")
    op.add_column("dm_rentals_events", sa.Column("type", sa.String()), schema="DM_RENTAL")
