import os

from alembic.autogenerate import comparators

from .operations_tables import GrantRightsOp, RevokeRightsOp


@comparators.dispatch_for("table")
def compare_table(autogen_context, modify_table_ops, s, tname, metadata_table_db, metadata_table_code):
    if str(metadata_table_db) == 'None':
        sensitive = metadata_table_code.info.get('sensitive', False)
        for render_scope in ['read', 'write', 'all']:
            group_name = (
                f'test_{"sensitive_" if sensitive else ""}dwh_{s}_{render_scope}'.lower()
                if os.getenv("ENVIRONMENT") != "production"
                else f'prod_{"sensitive_" if sensitive else ""}dwh_{s}_{render_scope}'.lower()
            )

            scopes = []
            match render_scope:
                case 'read':
                    scopes = ['SELECT']
                case 'write':
                    scopes = ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT']
                case 'all':
                    scopes = ['ALL']

            if sensitive:
                modify_table_ops.ops.append(CreateGroupOp(group_name=group_name))

            modify_table_ops.ops.append(
                GrantRightsOp(table_name=str(metadata_table_code), scopes=scopes, group_name=group_name)
            )

    elif str(metadata_table_code) == 'None':
        sensitive = metadata_table_db.info.get('sensitive', False)
        for render_scope in ['read', 'write', 'all']:
            group_name = (
                f'test_{"sensitive_" if sensitive else ""}dwh_{s}_{render_scope}'.lower()
                if os.getenv("ENVIRONMENT") != "production"
                else f'prod_{"sensitive_" if sensitive else ""}dwh_{s}_{render_scope}'.lower()
            )
            scopes = []
            match render_scope:
                case 'read':
                    scopes = ['SELECT']
                case 'write':
                    scopes = ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT']
                case 'all':
                    scopes = ['ALL']

            modify_table_ops.ops.append(
                RevokeRightsOp(table_name=str(metadata_table_db), scopes=scopes, group_name=group_name)
            )

            if sensitive:
                modify_table_ops.ops.append(DeleteGroupOp(group_name=group_name))
