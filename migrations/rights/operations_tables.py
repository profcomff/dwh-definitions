from alembic.operations import MigrateOperation, Operations


@Operations.register_operation("grant_rights")
class GrantRightsOp(MigrateOperation):
    def __init__(self, group_name, table_name):
        self.group_name = group_name
        self.table_name = table_name

    @classmethod
    def grant_rights(cls, operations, group_name, table_name, **kw):
        op = GrantRightsOp(group_name, table_name, **kw)
        return operations.invoke(op)

    def reverse(self):
        return RevokeRightsOp(self.group_name, self.table_name)


@Operations.register_operation("revoke_rights")
class RevokeRightsOp(MigrateOperation):
    def __init__(self, group_name, table_name):
        self.group_name = group_name
        self.table_name = table_name

    @classmethod
    def revoke_rights(cls, operations, group_name, table_name, **kw):
        op = RevokeRightsOp(group_name, table_name, **kw)
        return operations.invoke(op)

    def reverse(self):
        return GrantRightsOp(self.group_name, self.table_name)


@Operations.implementation_for(GrantRightsOp)
def grant_rights(operations, operation):
    group = operation.group_name
    table = operation.table_name.split('.')
    scope = group.split("_")[-1]
    match scope:
        case 'read':
            operations.execute(f'GRANT SELECT ON TABLE "{table[0]}".{table[1]} TO {group}')
        case 'write':
            operations.execute(f'GRANT SELECT, UPDATE, DELETE, TRUNCATE ON TABLE "{table[0]}".{table[1]} TO {group}')
        case 'all':
            operations.execute(f'GRANT ALL ON TABLE "{table[0]}".{table[1]} TO {group}')


@Operations.implementation_for(RevokeRightsOp)
def revoke_rights(operations, operation):
    group = operation.group_name
    table = operation.table_name.split('.')
    scope = group.split("_")[-1]
    match scope:
        case 'read':
            operations.execute(f'REVOKE SELECT ON TABLE "{table[0]}".{table[1]} FROM {group}')
        case 'write':
            operations.execute(f'REVOKE SELECT, UPDATE, DELETE, TRUNCATE ON TABLE "{table[0]}".{table[1]} FROM {group}')
        case 'all':
            operations.execute(f'REVOKE ALL ON TABLE "{table[0]}".{table[1]} FROM {group}')
