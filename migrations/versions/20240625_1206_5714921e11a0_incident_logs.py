"""incident_logs

Revision ID: 5714921e11a0
Revises: 7a18bd9ff633
Create Date: 2024-06-25 12:06:54.755277

"""

import os

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '5714921e11a0'
down_revision = '7a18bd9ff633'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'incident_hint',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('msk_record_loaded_dttm', sa.DateTime(), nullable=False, comment='Поле нарезки лога'),
        sa.Column(
            'container_name', sa.String(), nullable=False, comment='Имя контейнера, в котором произошла ошибочка'
        ),
        sa.Column('message', sa.String(), nullable=False, comment='Сообщение об ошибке'),
        sa.Column('create_ts', sa.DateTime(), nullable=False, comment='Время, когда произошла ошибка'),
        sa.PrimaryKeyConstraint('id'),
        schema='DM_INFRA_LOGS',
        comment='Информация об ошибках по контейнерам',
    )
    op.grant_on_table(
        "test_dwh_dm_infra_logs_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_infra_logs_read",
        ['SELECT'],
        '"DM_INFRA_LOGS".incident_hint',
    )
    op.grant_on_table(
        "test_dwh_dm_infra_logs_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_infra_logs_write",
        ['SELECT', 'INSERT', 'DELETE', 'UPDATE', 'TRUNCATE'],
        '"DM_INFRA_LOGS".incident_hint',
    )
    op.grant_on_table(
        "test_dwh_dm_infra_logs_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_infra_logs_all",
        ['ALL'],
        '"DM_INFRA_LOGS".incident_hint',
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.revoke_on_table(
        "test_dwh_dm_infra_logs_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_infra_logs_all",
        ['ALL'],
        '"DM_INFRA_LOGS".incident_hint',
    )
    op.revoke_on_table(
        "test_dwh_dm_infra_logs_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_infra_logs_write",
        ['SELECT', 'INSERT', 'DELETE', 'UPDATE', 'TRUNCATE'],
        '"DM_INFRA_LOGS".incident_hint',
    )
    op.revoke_on_table(
        "test_dwh_dm_infra_logs_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_infra_logs_read",
        ['SELECT'],
        '"DM_INFRA_LOGS".incident_hint',
    )
    op.drop_table('incident_hint', schema='DM_INFRA_LOGS')
