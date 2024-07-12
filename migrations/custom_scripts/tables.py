from alembic.autogenerate import comparators
from sqlalchemy import text
import os
from .operations_schemas import CreateTableSchemaOp, DropTableSchemaOp
from .operations_groups import CreateGroupOp, DeleteGroupOp, GrantOnSchemaOp, RevokeOnSchemaOp
from .operations_tables import GrantRightsOp, RevokeRightsOp

@comparators.dispatch_for("table")
def compare_table(autogen_context, modify_table_ops, s, tname, metadata_table_db, metadata_table_code):
    print(metadata_table_db, metadata_table_code, tname)
    # new_table_schema = str(metadata_table_code).split(".")[0]
    database_tables = ['.'.join(table_info) for table_info in autogen_context.connection.execute(text(f"select table_schema, table_name from information_schema.tables where table_schema='{s}'")).fetchall()]
    if str(metadata_table_db) == 'None':
        for render_scope in ['read', 'write', 'all']:
            group_name = (
                f'test_dwh_{s}_{render_scope}'.lower()
                if os.getenv("ENVIRONMENT") != "production"
                else f'prod_dwh_{s}_{render_scope}'.lower()
            )
            scopes = []
            match render_scope:
                case 'read':
                    scopes = ['SELECT']
                case 'write':
                    scopes = ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT']
                case 'all':
                    scopes = ['ALL']

            modify_table_ops.ops.append(GrantRightsOp(table_name=str(metadata_table_code), scopes=scopes, group_name=group_name))

    elif str(metadata_table_code) == 'None':
        for render_scope in ['read', 'write', 'all']:
            group_name = (
                f'test_dwh_{s}_{render_scope}'.lower()
                if os.getenv("ENVIRONMENT") != "production"
                else f'prod_dwh_{s}_{render_scope}'.lower()
            )
            scopes = []
            match render_scope:
                case 'read':
                    scopes = ['SELECT']
                case 'write':
                    scopes = ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT']
                case 'all':
                    scopes = ['ALL']

            modify_table_ops.ops.append(RevokeRightsOp(table_name=str(metadata_table_db), scopes=scopes, group_name=group_name))
    # print(metadata_table_exists, metadata_table, s, tname)
    # elif not metadata_table_exists:
    #     print(metadata_table)