import sqlalchemy as sa
from sqlalchemy import Column

from profcomff_definitions.base import Base


class User(Base):
    id = Column(sa.Integer, primary_key=True)
    union_number = Column(sa.String)
    user_agent = Column(sa.String)
    auth_user_id = Column(sa.Integer)
    modify_ts = Column(sa.DateTime)
    create_ts = Column(sa.DateTime)


class ActionsInfo(Base):
    """Actions from user"""

    id = Column(sa.Integer, primary_key=True)
    user_id = Column(sa.Integer)
    action = Column(sa.String)
    path_from = Column(sa.String)
    path_to = Column(sa.String)
    additional_data = Column(sa.String)
    create_ts = Column(sa.DateTime)
