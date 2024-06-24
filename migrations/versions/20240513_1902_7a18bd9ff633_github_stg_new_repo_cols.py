"""Github STG new repo cols

Revision ID: 7a18bd9ff633
Revises: 7353088d02ce
Create Date: 2024-05-13 19:02:03.331968

"""

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '7a18bd9ff633'
down_revision = '7353088d02ce'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'profcomff_repo',
        sa.Column('security_and_analysis_secret_scanning_status', sa.String(), nullable=True),
        schema='STG_GITHUB',
    )
    op.add_column(
        'profcomff_repo',
        sa.Column('security_and_analysis_secret_scanning_push_protection_status', sa.String(), nullable=True),
        schema='STG_GITHUB',
    )
    op.add_column(
        'profcomff_repo',
        sa.Column('security_and_analysis_dependabot_security_updates_status', sa.String(), nullable=True),
        schema='STG_GITHUB',
    )
    op.add_column(
        'profcomff_repo',
        sa.Column('security_and_analysis_secret_scanning_validity_checks_status', sa.String(), nullable=True),
        schema='STG_GITHUB',
    )
    op.alter_column('profcomff_issue', 'id', existing_type=sa.INTEGER(), type_=sa.BIGINT(), schema='STG_GITHUB')


def downgrade():
    op.alter_column('profcomff_issue', 'id', existing_type=sa.BIGINT(), type_=sa.INTEGER(), schema='STG_GITHUB')
    op.drop_column(
        'profcomff_repo', 'security_and_analysis_secret_scanning_validity_checks_status', schema='STG_GITHUB'
    )
    op.drop_column('profcomff_repo', 'security_and_analysis_dependabot_security_updates_status', schema='STG_GITHUB')
    op.drop_column(
        'profcomff_repo', 'security_and_analysis_secret_scanning_push_protection_status', schema='STG_GITHUB'
    )
    op.drop_column('profcomff_repo', 'security_and_analysis_secret_scanning_status', schema='STG_GITHUB')
