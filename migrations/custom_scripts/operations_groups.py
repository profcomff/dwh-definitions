from alembic.operations import MigrateOperation, Operations


@Operations.register_operation("create_group")
class CreateGroupOp(MigrateOperation):
    def __init__(self, group_name):
        self.group_name = group_name

    @classmethod
    def create_group(cls, operations, group_name, **kw):
        op = CreateGroupOp(group_name, **kw)
        return operations.invoke(op)

    def reverse(self):
        return DeleteGroupOp(self.group_name)


@Operations.register_operation("grant_on_schema")
class GrantOnSchemaOp(MigrateOperation):
    def __init__(self, group_name, schema):
        self.group_name = group_name
        self.schema = schema

    @classmethod
    def grant_on_schema(cls, operations, group_name, schema, **kw):
        op = GrantOnSchemaOp(group_name, schema, **kw)
        return operations.invoke(op)

    def reverse(self):
        return RevokeOnSchemaOp(self.group_name, self.schema)


@Operations.register_operation("delete_group")
class DeleteGroupOp(MigrateOperation):
    def __init__(self, group_name):
        self.group_name = group_name

    @classmethod
    def delete_group(cls, operations, group_name, **kw):
        op = DeleteGroupOp(group_name, **kw)
        return operations.invoke(op)

    def reverse(self):
        return CreateGroupOp(self.group_name)


@Operations.register_operation("revoke_on_schema")
class RevokeOnSchemaOp(MigrateOperation):
    def __init__(self, group_name, schema):
        self.group_name = group_name
        self.schema = schema

    @classmethod
    def revoke_on_schema(cls, operations, group_name, schema, **kw):
        op = RevokeOnSchemaOp(group_name, schema, **kw)
        return operations.invoke(op)

    def reverse(self):
        return GrantOnSchemaOp(self.group_name, self.schema)


@Operations.implementation_for(CreateGroupOp)
def create_group(operations, operation):
    name = operation.group_name.lower()
    operations.execute(f'CREATE GROUP {name}')


@Operations.implementation_for(DeleteGroupOp)
def delete_group(operations, operation):
    name = operation.group_name.lower()
    operations.execute(f'DROP GROUP {name}')


@Operations.implementation_for(GrantOnSchemaOp)
def grant_on_schema(operations, operation):
    group = operation.group_name.lower()
    schema = operation.schema.upper()
    operations.execute(f'GRANT USAGE ON SCHEMA "{schema}" TO {group}')


@Operations.implementation_for(RevokeOnSchemaOp)
def revoke_on_schema(operations, operation):
    group = operation.group_name.lower()
    schema = operation.schema.upper()
    operations.execute(f'REVOKE USAGE ON SCHEMA "{schema}" FROM {group}')
