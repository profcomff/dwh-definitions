"""add rating-api tables

Revision ID: ee89b52980d8
Revises: 0e97fd76b68a
Create Date: 2024-10-20 14:05:40.087805

"""

import os

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = 'ee89b52980d8'
down_revision = '0e97fd76b68a'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table_schema("STG_DUBINUSHKA_MANUAL")
    op.create_table_schema("STG_RATING")
    op.create_table(
        'comment',
        sa.Column('flag', sa.Integer(), nullable=False),
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('lecturer_id', sa.Integer(), nullable=True),
        sa.Column('comment_text', sa.String(), nullable=True),
        sa.Column('author_name', sa.String(), nullable=True),
        sa.Column('rate', sa.String(), nullable=True),
        sa.Column('date', sa.String(), nullable=True),
        sa.Column('dobr', sa.String(), nullable=True),
        sa.Column('hal', sa.String(), nullable=True),
        sa.Column('pon', sa.String(), nullable=True),
        schema='STG_DUBINUSHKA_MANUAL',
        comment='Comments from dubinushka\n    Because this data is downloaded from .sql query, the order of columns is significant',
    )
    op.create_table(
        'lecturer',
        sa.Column('flagprep', sa.Integer(), nullable=True),
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('surname', sa.String(), nullable=True),
        sa.Column('subject', sa.String(), nullable=True),
        sa.Column('fullrate', sa.Integer(), nullable=True),
        sa.Column('mn_count', sa.String(), nullable=True),
        sa.Column('photo', sa.Integer(), nullable=True),
        sa.Column('dobr', sa.Float(), nullable=True),
        sa.Column('hal', sa.Float(), nullable=True),
        sa.Column('pon', sa.Float(), nullable=True),
        sa.Column('isdead', sa.Integer(), nullable=True),
        sa.Column('obituary', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_DUBINUSHKA_MANUAL',
        comment='Lecturers from dubinushka\n    Because this data is downloaded from .sql query, the order of columns is significant',
    )
    op.create_table(
        'comment',
        sa.Column('uuid', sa.Uuid(), nullable=False),
        sa.Column('create_ts', sa.DateTime(), nullable=False),
        sa.Column('update_ts', sa.DateTime(), nullable=False),
        sa.Column('subject', sa.String(), nullable=False),
        sa.Column('text', sa.String(), nullable=True),
        sa.Column('mark_kindness', sa.Integer(), nullable=False),
        sa.Column('mark_freebie', sa.Integer(), nullable=False),
        sa.Column('mark_clarity', sa.Integer(), nullable=False),
        sa.Column('lecturer_id', sa.Integer(), nullable=False),
        sa.Column('review_status', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('uuid'),
        schema='STG_RATING',
    )
    op.create_table(
        'lecturer',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('first_name', sa.String(), nullable=False),
        sa.Column('last_name', sa.String(), nullable=False),
        sa.Column('middle_name', sa.String(), nullable=False),
        sa.Column('subject', sa.String(), nullable=True),
        sa.Column('avatar_link', sa.String(), nullable=True),
        sa.Column('timetable_id', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_RATING',
    )
    op.create_table(
        'lecturer_user_comment',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('lecturer_id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('create_ts', sa.DateTime(), nullable=False),
        sa.Column('update_ts', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_RATING',
    )
    op.create_group(
        "test_dwh_stg_dubinushka_manual_read"
        if os.getenv("ENVIRONMENT") != "production"
        else "prod_dwh_stg_dubinushka_manual_read"
    )
    op.create_group(
        "test_dwh_stg_dubinushka_manual_write"
        if os.getenv("ENVIRONMENT") != "production"
        else "prod_dwh_stg_dubinushka_manual_write"
    )
    op.create_group(
        "test_dwh_stg_dubinushka_manual_all"
        if os.getenv("ENVIRONMENT") != "production"
        else "prod_dwh_stg_dubinushka_manual_all"
    )
    op.create_group(
        "test_dwh_stg_rating_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rating_read"
    )
    op.create_group(
        "test_dwh_stg_rating_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rating_write"
    )
    op.create_group(
        "test_dwh_stg_rating_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rating_all"
    )
    op.grant_on_schema(
        (
            "test_dwh_stg_dubinushka_manual_read"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_dubinushka_manual_read"
        ),
        "STG_DUBINUSHKA_MANUAL",
    )
    op.grant_on_schema(
        (
            "test_dwh_stg_dubinushka_manual_write"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_dubinushka_manual_write"
        ),
        "STG_DUBINUSHKA_MANUAL",
    )
    op.grant_on_schema(
        (
            "test_dwh_stg_dubinushka_manual_all"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_dubinushka_manual_all"
        ),
        "STG_DUBINUSHKA_MANUAL",
    )
    op.grant_on_schema(
        "test_dwh_stg_rating_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rating_read",
        "STG_RATING",
    )
    op.grant_on_schema(
        "test_dwh_stg_rating_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rating_write",
        "STG_RATING",
    )
    op.grant_on_schema(
        "test_dwh_stg_rating_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rating_all",
        "STG_RATING",
    )
    op.grant_on_table(
        (
            "test_dwh_stg_dubinushka_manual_read"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_dubinushka_manual_read"
        ),
        ['SELECT'],
        '"STG_DUBINUSHKA_MANUAL".comment',
    )
    op.grant_on_table(
        (
            "test_dwh_stg_dubinushka_manual_write"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_dubinushka_manual_write"
        ),
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_DUBINUSHKA_MANUAL".comment',
    )
    op.grant_on_table(
        (
            "test_dwh_stg_dubinushka_manual_all"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_dubinushka_manual_all"
        ),
        ['ALL'],
        '"STG_DUBINUSHKA_MANUAL".comment',
    )
    op.grant_on_table(
        (
            "test_dwh_stg_dubinushka_manual_read"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_dubinushka_manual_read"
        ),
        ['SELECT'],
        '"STG_DUBINUSHKA_MANUAL".lecturer',
    )
    op.grant_on_table(
        (
            "test_dwh_stg_dubinushka_manual_write"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_dubinushka_manual_write"
        ),
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_DUBINUSHKA_MANUAL".lecturer',
    )
    op.grant_on_table(
        (
            "test_dwh_stg_dubinushka_manual_all"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_dubinushka_manual_all"
        ),
        ['ALL'],
        '"STG_DUBINUSHKA_MANUAL".lecturer',
    )
    op.grant_on_table(
        "test_dwh_stg_rating_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rating_read",
        ['SELECT'],
        '"STG_RATING".lecturer',
    )
    op.grant_on_table(
        "test_dwh_stg_rating_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rating_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_RATING".lecturer',
    )
    op.grant_on_table(
        "test_dwh_stg_rating_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rating_all",
        ['ALL'],
        '"STG_RATING".lecturer',
    )
    op.grant_on_table(
        "test_dwh_stg_rating_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rating_read",
        ['SELECT'],
        '"STG_RATING".comment',
    )
    op.grant_on_table(
        "test_dwh_stg_rating_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rating_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_RATING".comment',
    )
    op.grant_on_table(
        "test_dwh_stg_rating_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rating_all",
        ['ALL'],
        '"STG_RATING".comment',
    )
    op.grant_on_table(
        "test_dwh_stg_rating_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rating_read",
        ['SELECT'],
        '"STG_RATING".lecturer_user_comment',
    )
    op.grant_on_table(
        "test_dwh_stg_rating_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rating_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_RATING".lecturer_user_comment',
    )
    op.grant_on_table(
        "test_dwh_stg_rating_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rating_all",
        ['ALL'],
        '"STG_RATING".lecturer_user_comment',
    )
    op.grant_on_table(
        (
            "test_dwh_stg_dubinushka_manual_read"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_dubinushka_manual_read"
        ),
        ['SELECT'],
        '"STG_DUBINUSHKA_MANUAL".comment',
    )
    op.grant_on_table(
        (
            "test_dwh_stg_dubinushka_manual_write"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_dubinushka_manual_write"
        ),
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_DUBINUSHKA_MANUAL".comment',
    )
    op.grant_on_table(
        (
            "test_dwh_stg_dubinushka_manual_all"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_dubinushka_manual_all"
        ),
        ['ALL'],
        '"STG_DUBINUSHKA_MANUAL".comment',
    )
    op.grant_on_table(
        (
            "test_dwh_stg_dubinushka_manual_read"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_dubinushka_manual_read"
        ),
        ['SELECT'],
        '"STG_DUBINUSHKA_MANUAL".lecturer',
    )
    op.grant_on_table(
        (
            "test_dwh_stg_dubinushka_manual_write"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_dubinushka_manual_write"
        ),
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_DUBINUSHKA_MANUAL".lecturer',
    )
    op.grant_on_table(
        (
            "test_dwh_stg_dubinushka_manual_all"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_dubinushka_manual_all"
        ),
        ['ALL'],
        '"STG_DUBINUSHKA_MANUAL".lecturer',
    )
    op.grant_on_table(
        "test_dwh_stg_rating_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rating_read",
        ['SELECT'],
        '"STG_RATING".comment',
    )
    op.grant_on_table(
        "test_dwh_stg_rating_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rating_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_RATING".comment',
    )
    op.grant_on_table(
        "test_dwh_stg_rating_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rating_all",
        ['ALL'],
        '"STG_RATING".comment',
    )
    op.grant_on_table(
        "test_dwh_stg_rating_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rating_read",
        ['SELECT'],
        '"STG_RATING".lecturer',
    )
    op.grant_on_table(
        "test_dwh_stg_rating_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rating_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_RATING".lecturer',
    )
    op.grant_on_table(
        "test_dwh_stg_rating_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rating_all",
        ['ALL'],
        '"STG_RATING".lecturer',
    )
    op.grant_on_table(
        "test_dwh_stg_rating_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rating_read",
        ['SELECT'],
        '"STG_RATING".lecturer_user_comment',
    )
    op.grant_on_table(
        "test_dwh_stg_rating_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rating_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_RATING".lecturer_user_comment',
    )
    op.grant_on_table(
        "test_dwh_stg_rating_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rating_all",
        ['ALL'],
        '"STG_RATING".lecturer_user_comment',
    )


def downgrade():
    op.revoke_on_table(
        "test_dwh_stg_rating_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rating_all",
        ['ALL'],
        '"STG_RATING".lecturer_user_comment',
    )
    op.revoke_on_table(
        "test_dwh_stg_rating_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rating_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_RATING".lecturer_user_comment',
    )
    op.revoke_on_table(
        "test_dwh_stg_rating_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rating_read",
        ['SELECT'],
        '"STG_RATING".lecturer_user_comment',
    )
    op.revoke_on_table(
        "test_dwh_stg_rating_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rating_all",
        ['ALL'],
        '"STG_RATING".lecturer',
    )
    op.revoke_on_table(
        "test_dwh_stg_rating_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rating_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_RATING".lecturer',
    )
    op.revoke_on_table(
        "test_dwh_stg_rating_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rating_read",
        ['SELECT'],
        '"STG_RATING".lecturer',
    )
    op.revoke_on_table(
        "test_dwh_stg_rating_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rating_all",
        ['ALL'],
        '"STG_RATING".comment',
    )
    op.revoke_on_table(
        "test_dwh_stg_rating_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rating_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_RATING".comment',
    )
    op.revoke_on_table(
        "test_dwh_stg_rating_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rating_read",
        ['SELECT'],
        '"STG_RATING".comment',
    )
    op.revoke_on_table(
        (
            "test_dwh_stg_dubinushka_manual_all"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_dubinushka_manual_all"
        ),
        ['ALL'],
        '"STG_DUBINUSHKA_MANUAL".lecturer',
    )
    op.revoke_on_table(
        (
            "test_dwh_stg_dubinushka_manual_write"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_dubinushka_manual_write"
        ),
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_DUBINUSHKA_MANUAL".lecturer',
    )
    op.revoke_on_table(
        (
            "test_dwh_stg_dubinushka_manual_read"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_dubinushka_manual_read"
        ),
        ['SELECT'],
        '"STG_DUBINUSHKA_MANUAL".lecturer',
    )
    op.revoke_on_table(
        (
            "test_dwh_stg_dubinushka_manual_all"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_dubinushka_manual_all"
        ),
        ['ALL'],
        '"STG_DUBINUSHKA_MANUAL".comment',
    )
    op.revoke_on_table(
        (
            "test_dwh_stg_dubinushka_manual_write"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_dubinushka_manual_write"
        ),
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_DUBINUSHKA_MANUAL".comment',
    )
    op.revoke_on_table(
        (
            "test_dwh_stg_dubinushka_manual_read"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_dubinushka_manual_read"
        ),
        ['SELECT'],
        '"STG_DUBINUSHKA_MANUAL".comment',
    )
    op.revoke_on_table(
        "test_dwh_stg_rating_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rating_all",
        ['ALL'],
        '"STG_RATING".lecturer_user_comment',
    )
    op.revoke_on_table(
        "test_dwh_stg_rating_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rating_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_RATING".lecturer_user_comment',
    )
    op.revoke_on_table(
        "test_dwh_stg_rating_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rating_read",
        ['SELECT'],
        '"STG_RATING".lecturer_user_comment',
    )
    op.revoke_on_table(
        "test_dwh_stg_rating_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rating_all",
        ['ALL'],
        '"STG_RATING".comment',
    )
    op.revoke_on_table(
        "test_dwh_stg_rating_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rating_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_RATING".comment',
    )
    op.revoke_on_table(
        "test_dwh_stg_rating_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rating_read",
        ['SELECT'],
        '"STG_RATING".comment',
    )
    op.revoke_on_table(
        "test_dwh_stg_rating_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rating_all",
        ['ALL'],
        '"STG_RATING".lecturer',
    )
    op.revoke_on_table(
        "test_dwh_stg_rating_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rating_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_RATING".lecturer',
    )
    op.revoke_on_table(
        "test_dwh_stg_rating_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rating_read",
        ['SELECT'],
        '"STG_RATING".lecturer',
    )
    op.revoke_on_table(
        (
            "test_dwh_stg_dubinushka_manual_all"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_dubinushka_manual_all"
        ),
        ['ALL'],
        '"STG_DUBINUSHKA_MANUAL".lecturer',
    )
    op.revoke_on_table(
        (
            "test_dwh_stg_dubinushka_manual_write"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_dubinushka_manual_write"
        ),
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_DUBINUSHKA_MANUAL".lecturer',
    )
    op.revoke_on_table(
        (
            "test_dwh_stg_dubinushka_manual_read"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_dubinushka_manual_read"
        ),
        ['SELECT'],
        '"STG_DUBINUSHKA_MANUAL".lecturer',
    )
    op.revoke_on_table(
        (
            "test_dwh_stg_dubinushka_manual_all"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_dubinushka_manual_all"
        ),
        ['ALL'],
        '"STG_DUBINUSHKA_MANUAL".comment',
    )
    op.revoke_on_table(
        (
            "test_dwh_stg_dubinushka_manual_write"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_dubinushka_manual_write"
        ),
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_DUBINUSHKA_MANUAL".comment',
    )
    op.revoke_on_table(
        (
            "test_dwh_stg_dubinushka_manual_read"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_dubinushka_manual_read"
        ),
        ['SELECT'],
        '"STG_DUBINUSHKA_MANUAL".comment',
    )
    op.revoke_on_schema(
        "test_dwh_stg_rating_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rating_all",
        "STG_RATING",
    )
    op.revoke_on_schema(
        "test_dwh_stg_rating_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rating_write",
        "STG_RATING",
    )
    op.revoke_on_schema(
        "test_dwh_stg_rating_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rating_read",
        "STG_RATING",
    )
    op.revoke_on_schema(
        (
            "test_dwh_stg_dubinushka_manual_all"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_dubinushka_manual_all"
        ),
        "STG_DUBINUSHKA_MANUAL",
    )
    op.revoke_on_schema(
        (
            "test_dwh_stg_dubinushka_manual_write"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_dubinushka_manual_write"
        ),
        "STG_DUBINUSHKA_MANUAL",
    )
    op.revoke_on_schema(
        (
            "test_dwh_stg_dubinushka_manual_read"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_dubinushka_manual_read"
        ),
        "STG_DUBINUSHKA_MANUAL",
    )
    op.drop_table('lecturer_user_comment', schema='STG_RATING')
    op.drop_table('lecturer', schema='STG_RATING')
    op.drop_table('comment', schema='STG_RATING')
    op.drop_table('lecturer', schema='STG_DUBINUSHKA_MANUAL')
    op.drop_table('comment', schema='STG_DUBINUSHKA_MANUAL')
    op.delete_group(
        "test_dwh_stg_rating_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rating_all"
    )
    op.delete_group(
        "test_dwh_stg_rating_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rating_write"
    )
    op.delete_group(
        "test_dwh_stg_rating_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rating_read"
    )
    op.delete_group(
        "test_dwh_stg_dubinushka_manual_all"
        if os.getenv("ENVIRONMENT") != "production"
        else "prod_dwh_stg_dubinushka_manual_all"
    )
    op.delete_group(
        "test_dwh_stg_dubinushka_manual_write"
        if os.getenv("ENVIRONMENT") != "production"
        else "prod_dwh_stg_dubinushka_manual_write"
    )
    op.delete_group(
        "test_dwh_stg_dubinushka_manual_read"
        if os.getenv("ENVIRONMENT") != "production"
        else "prod_dwh_stg_dubinushka_manual_read"
    )
    op.drop_table_schema("STG_RATING")
    op.drop_table_schema("STG_DUBINUSHKA_MANUAL")
