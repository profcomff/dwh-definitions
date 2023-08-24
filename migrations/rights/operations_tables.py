from alembic.operations import MigrateOperation, Operations


@Operations.register_operation("grant_rights")
class GrantRightsOp(MigrateOperation):
    def __init__(self, group_name, scopes, table_name):
        self.group_name = group_name
        self.table_name = table_name
        self.scopes = scopes

    @classmethod
    def grant_rights(cls, operations, group_name, scopes, table_name, **kw):
        op = GrantRightsOp(group_name, scopes, table_name, **kw)
        return operations.invoke(op)

    def reverse(self):
        return RevokeRightsOp(self.group_name, self.scopes, self.table_name)


@Operations.register_operation("revoke_rights")
class RevokeRightsOp(MigrateOperation):
    def __init__(self, group_name, scopes, table_name):
        self.group_name = group_name
        self.table_name = table_name
        self.scopes = scopes

    @classmethod
    def revoke_rights(cls, operations, group_name, scopes, table_name, **kw):
        op = RevokeRightsOp(group_name, scopes, table_name, **kw)
        return operations.invoke(op)

    def reverse(self):
        return GrantRightsOp(self.group_name, self.scopes, self.table_name)


@Operations.implementation_for(GrantRightsOp)
def grant_rights(operations, operation):
    group = operation.group_name.lower()
    table = operation.table_name.split('.')
    scopes = eval(operation.scopes)
    for scope in scopes:
        operations.execute(f'GRANT {scope} ON TABLE {table[0]}.{table[1]} TO {group}')


@Operations.implementation_for(RevokeRightsOp)
def revoke_rights(operations, operation):
    group = operation.group_name.lower()
    table = operation.table_name.split('.')
    scopes = eval(operation.scopes)
    for scope in scopes:
        operations.execute(f'REVOKE {scope} ON TABLE {table[0]}.{table[1]} FROM {group}')
