import sqlalchemy as sa
from sqlalchemy import Column

from profcomff_definitions.base import Base


class User(Base):
    id = Column(sa.Integer, primary_key=True)
    union_number = Column(sa.String, nullable=True)
    user_agent = Column(sa.String, nullable=True)
    auth_user_id = Column(sa.Integer, nullable=True)
    modify_ts = Column(sa.DateTime, nullable=True)
    create_ts = Column(sa.DateTime, nullable=True)


class ActionsInfo(Base):
    id = Column(sa.Integer, primary_key=True)
    user_id = Column(sa.Integer, nullable=True)
    action = Column(sa.String, nullable=True)
    path_from = Column(sa.String, nullable=True)
    path_to = Column(sa.String, nullable=True)
    additional_data = Column(sa.String, nullable=True)
    create_ts = Column(sa.DateTime, nullable=True)
