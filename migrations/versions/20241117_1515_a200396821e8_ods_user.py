"""ODS.user

Revision ID: a200396821e8
Revises: 9fcb159af046
Create Date: 2024-11-17 15:15:18.545671

"""
from alembic import op
import sqlalchemy as sa
import os


# revision identifiers, used by Alembic.
revision = 'a200396821e8'
down_revision = '9fcb159af046'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('info', sa.Column('user_id', sa.Integer(), nullable=False), schema='ODS_USER')
    op.add_column('info', sa.Column('auth_email', sa.String(), nullable=True), schema='ODS_USER')
    op.add_column('info', sa.Column('vk_name', sa.String(), nullable=True), schema='ODS_USER')
    op.add_column('info', sa.Column('city', sa.String(), nullable=True), schema='ODS_USER')
    op.add_column('info', sa.Column('hometown', sa.String(), nullable=True), schema='ODS_USER')
    op.add_column('info', sa.Column('location', sa.String(), nullable=True), schema='ODS_USER')
    op.add_column('info', sa.Column('github_name', sa.String(), nullable=True), schema='ODS_USER')
    op.add_column('info', sa.Column('telegram_name', sa.String(), nullable=True), schema='ODS_USER')
    op.add_column('info', sa.Column('home_phone_number', sa.String(), nullable=True), schema='ODS_USER')
    op.add_column('info', sa.Column('education_level', sa.String(), nullable=True), schema='ODS_USER')
    op.add_column('info', sa.Column('university', sa.String(), nullable=True), schema='ODS_USER')
    op.add_column('info', sa.Column('group', sa.String(), nullable=True), schema='ODS_USER')
    op.add_column('info', sa.Column('faculty', sa.String(), nullable=True), schema='ODS_USER')
    op.add_column('info', sa.Column('position', sa.String(), nullable=True), schema='ODS_USER')
    op.add_column('info', sa.Column('student_id_number', sa.String(), nullable=True), schema='ODS_USER')
    op.add_column('info', sa.Column('department', sa.String(), nullable=True), schema='ODS_USER')
    op.add_column('info', sa.Column('mode_of_study', sa.String(), nullable=True), schema='ODS_USER')
    op.add_column('info', sa.Column('full_name', sa.String(), nullable=True), schema='ODS_USER')
    op.add_column('info', sa.Column('birth_date', sa.String(), nullable=True), schema='ODS_USER')
    op.add_column('info', sa.Column('photo', sa.String(), nullable=True), schema='ODS_USER')
    op.add_column('info', sa.Column('sex', sa.String(), nullable=True), schema='ODS_USER')
    op.add_column('info', sa.Column('job', sa.String(), nullable=True), schema='ODS_USER')
    op.add_column('info', sa.Column('work_location', sa.String(), nullable=True), schema='ODS_USER')
    op.add_column('info', sa.Column('is_deleted', sa.Boolean(), nullable=True), schema='ODS_USER')
    op.drop_index('ix_ODS_USER_info_id', table_name='info', schema='ODS_USER')
    op.create_index(op.f('ix_ODS_USER_info_user_id'), 'info', ['user_id'], unique=False, schema='ODS_USER')
    op.drop_column('info', 'id', schema='ODS_USER')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('info', sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False), schema='ODS_USER')
    op.drop_index(op.f('ix_ODS_USER_info_user_id'), table_name='info', schema='ODS_USER')
    op.create_index('ix_ODS_USER_info_id', 'info', ['id'], unique=False, schema='ODS_USER')
    op.drop_column('info', 'is_deleted', schema='ODS_USER')
    op.drop_column('info', 'work_location', schema='ODS_USER')
    op.drop_column('info', 'job', schema='ODS_USER')
    op.drop_column('info', 'sex', schema='ODS_USER')
    op.drop_column('info', 'photo', schema='ODS_USER')
    op.drop_column('info', 'birth_date', schema='ODS_USER')
    op.drop_column('info', 'full_name', schema='ODS_USER')
    op.drop_column('info', 'mode_of_study', schema='ODS_USER')
    op.drop_column('info', 'department', schema='ODS_USER')
    op.drop_column('info', 'student_id_number', schema='ODS_USER')
    op.drop_column('info', 'position', schema='ODS_USER')
    op.drop_column('info', 'faculty', schema='ODS_USER')
    op.drop_column('info', 'group', schema='ODS_USER')
    op.drop_column('info', 'university', schema='ODS_USER')
    op.drop_column('info', 'education_level', schema='ODS_USER')
    op.drop_column('info', 'home_phone_number', schema='ODS_USER')
    op.drop_column('info', 'telegram_name', schema='ODS_USER')
    op.drop_column('info', 'github_name', schema='ODS_USER')
    op.drop_column('info', 'location', schema='ODS_USER')
    op.drop_column('info', 'hometown', schema='ODS_USER')
    op.drop_column('info', 'city', schema='ODS_USER')
    op.drop_column('info', 'vk_name', schema='ODS_USER')
    op.drop_column('info', 'auth_email', schema='ODS_USER')
    op.drop_column('info', 'user_id', schema='ODS_USER')
    # ### end Alembic commands ###
