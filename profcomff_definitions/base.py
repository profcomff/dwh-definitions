import re
from typing import Any

from definitions.custom_scripts.schemas import add_table_schema_to_model
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import as_declarative, configure_mappers
from sqlalchemy import Table


def _recursive_merge(a: dict, b: dict) -> None:
    """Helper function for recursive_merge"""
    for key, val in b.items():
        if key in a and isinstance(a[key], dict) and isinstance(val, dict):
            _recursive_merge(a[key], val)
            continue
        a[key] = val


def recursive_merge(a: dict, b: dict) -> dict:
    """Returns a copy of 'a', recursively-updated with 'b'
    (acts like recursive dict .update operator)
    """
    ret = a.copy()
    _recursive_merge(ret, b)
    return ret


def sensitive(cls):
    """Mark table as sensitive

    Sets 'info.sensitive' attribute to True. This attribute can be accessed in
    definitions-lib in table comparator with
    metadata_table_code.info.get("sensitive", False)
    """
    new_table_args = recursive_merge(cls.__table_args__, {"info": {"sensitive": True}, "extend_existing": True})
    # Private function from sqlalchemy/sql/schema.py:Table
    # Can be replaced with cls.__table__ = Table(...), but will be less optimal
    cls.__table__._init_existing(**new_table_args)
    return cls


def encrypted(id_column: str, key_table: str | None):
    """Mark table as encrypted

    - id_column: encryption keys are going to be generated for all rows and
      will be unique for each `id_column` value. Should be a name of primary
      key in a table.

    - key_table (optional): table name to store keys in. If unspecified,
      generated automatically (check generated migration scripts for the actual
      name)

    Sets 'info.encrypted' attribute to True, and adds information about
    encryption in 'info.encryption' attribute.

    Attributes can be accessesed in definitions-lib in table comparator with
    metadata_table_code.info.get("attribute-name", default_value);
    """

    def encrypted_decorator(cls):
        new_table_args = recursive_merge(
            cls.__table_args__,
            {
                "info": {
                    # "sensitive": True, # Not needed since table is encrypted anyways
                    "encrypted": True,
                    "encryption": {"id": id_column, "key": key_table},
                },
                "extend_existing": True,
            },
        )
        # See comment in function "sensitive"
        cls.__table__._init_existing(**new_table_args)
        return cls

    return encrypted_decorator


@as_declarative()
class Base:
    """Base class for all database entities"""

    @classmethod
    @declared_attr
    def __tablename__(cls) -> str:
        """Generate database table name automatically.
        Convert CamelCase class name to snake_case db table name.
        """
        return re.sub(r"(?<!^)(?=[A-Z])", "_", cls.__name__).lower()

    @classmethod
    @property
    def __table_args__(cls) -> dict[str, Any]:
        schema = f'{cls.__module__.split(".")[-2].upper()}_{cls.__module__.split(".")[-1].upper()}'
        add_table_schema_to_model(schema, Base.metadata)
        return_dict = {
            'schema': schema,
            'comment': cls.__doc__,
            'info': {
                'sensitive': getattr(cls, "__sensitive__", False),
                'encrypted': getattr(cls, "__encrypted__", False),
            },
        }
        recursive_merge(return_dict, getattr(cls, "__table_args_overwrite__", {}))
        return return_dict

    def __repr__(self) -> str:
        attrs = []
        for c in self.__table__.columns:
            attrs.append(f"{c.name}={getattr(self, c.name)}")
        return "{}({})".format(self.__class__.__name__, ", ".join(attrs))
