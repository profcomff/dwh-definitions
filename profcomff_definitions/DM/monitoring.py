from datetime import date

from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class DbMonitoringSnp(Base):
    """
    Snapshot table that shows sizes for all tables in DWH
    """

    id: Mapped[int]
    table_name: Mapped[str] = mapped_column(
        comment="Table name with schema name, ex. \"STG_TIMETABLE\".\"events_groups\""
    )
    table_schema: Mapped[str] = mapped_column(comment="Table schema, need for detalization, ex.\"STG_TIMETABLE\"")
    table_size_mb: Mapped[int] = mapped_column(comment="Table size in MB (int), ex. 8")
    indexes_size_mb: Mapped[int] = mapped_column(comment="Table indexes size in MB(int), ex.5")
    total_size_mb: Mapped[int] = mapped_column(comment="Table total size in MB(int), ex. 13")
    state_dt: Mapped[date] = mapped_column(comment="Date of snapshot, ex. 2024-11-12")
    __mapper_args__ = {"primary_key": ["id", "state_dt"]}  # Used only to correctly map ORM object to sql table
