from alembic.operations import MigrateOperation, Operations


@Operations.register_operation("create_table_schema")
class CreateTableSchemaOp(MigrateOperation):
    def __init__(self, table_schema_name):
        self.table_schema_name = table_schema_name

    @classmethod
    def create_table_schema(cls, operations, table_schema_name, **kw):
        op = CreateTableSchemaOp(table_schema_name, **kw)
        return operations.invoke(op)

    def reverse(self):
        return DropTableSchemaOp(self.table_schema_name)


@Operations.register_operation("drop_table_schema")
class DropTableSchemaOp(MigrateOperation):
    def __init__(self, table_schema_name):
        self.table_schema_name = table_schema_name

    @classmethod
    def drop_table_schema(cls, operations, table_schema_name, **kw):
        op = DropTableSchemaOp(table_schema_name, **kw)
        return operations.invoke(op)

    def reverse(self):
        return CreateTableSchemaOp(self.table_schema_name)


@Operations.implementation_for(CreateTableSchemaOp)
def create_table_schema(operations, operation):
    if operation.table_schema_name is not None:
        name = "%s" % operation.table_schema_name
    else:
        name = operation.table_schema_name
    operations.execute('CREATE SCHEMA "%s"' % name.upper())


@Operations.implementation_for(DropTableSchemaOp)
def drop_table_schema(operations, operation):
    if operation.table_schema_name is not None:
        name = "%s" % operation.table_schema_name
    else:
        name = operation.table_schema_name
    operations.execute('DROP SCHEMA "%s"' % name.upper())
