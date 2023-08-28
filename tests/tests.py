from sqlalchemy import text


def test_schema_creation(engine, migration):
    with engine.connect() as conn:
        query = text("select schema_name from information_schema.schemata")
        result = [sch[0] for sch in conn.execute(query)]

        assert 'TESTS_DATABASE' in result


def test_group_creation(engine, migration):
    with engine.connect() as conn:
        query = text("SELECT * FROM pg_group")
        result = set(obj[0] for obj in conn.execute(query))
        check = {'test_dwh_tests_database_read', 'test_dwh_tests_database_write', 'test_dwh_tests_database_all'}

        assert check.issubset(result)


def test_table_rights(engine, migration):
    scopes = [
        {'SELECT'},
        {'SELECT', 'INSERT', 'UPDATE', 'DELETE', 'TRUNCATE'},
        {'SELECT', 'UPDATE', 'TRIGGER', 'DELETE', 'TRUNCATE', 'INSERT', 'REFERENCES'},
    ]
    groups = ['test_dwh_tests_database_read', 'test_dwh_tests_database_write', 'test_dwh_tests_database_all']
    with engine.connect() as conn:
        for i in range(len(groups)):
            query = text(f"SELECT privilege_type FROM information_schema.role_table_grants WHERE grantee='{groups[i]}'")
            assert scopes[i] == set([right[0] for right in conn.execute(query)])
