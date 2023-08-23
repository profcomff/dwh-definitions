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


@Operations.implementation_for(CreateGroupOp)
def create_group(operations, operation):
    name = operation.group_name
    operations.execute(f'CREATE GROUP {name}')
    schema = f'{name.split("_")[-3]}_{name.split("_")[-2]}'.upper()
    operations.execute(f'GRANT USAGE ON SCHEMA {schema} TO {name}')


@Operations.implementation_for(DeleteGroupOp)
def delete_group(operations, operation):
    name = operation.group_name
    operations.execute(f'DROP GROUP {name}')