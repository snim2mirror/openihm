import unittest
import datetime
from gui.interface.mixins import MySQLMixin
from database_helper import DatabaseHelper


class TestMySQLMixin(unittest.TestCase):
    """
    In order to use these tests you need to have a config file named
    test_openihm.cfg in the directory you are running the tests from
    (i.e. the src directory).

        [database]
        superuser = root
        superuser_password = s00pers3cur3
        database = test_openihm
        user = openihm
        password = ihm2012

    This should contain database credentials for a database that exists
    in mysql for testing.  This database will be toyed around with a lot.
    Obviously avoid pointing it at a database you care about...

    """

    def setUp(self):
        self.helper = DatabaseHelper(self)
        self.helper.start_tests()

    def tearDown(self):
        # drop the database
        self.helper.end_tests()

    def test_executeMultipleResultsQueries(self):
        self.helper.setup_clean_db()
        mixin = MySQLMixin()
        queries = [
        """
            insert into projects
                (projectname, description, currency)
            values
                ('test', 'a simple test', 'GBP')""",
        """
            insert into projects
                (projectname, description, currency)
            values
                ('test2', 'simple test', 'AUS')""",
        ]
        mixin.executeMultipleUpdateQueries(queries)
        exp = [
            [(u'test', None, None, u'a simple test', u'GBP')],
            [(u'test2', None, None, u'simple test', u'AUS')]
        ]
        s_queries = [
        """
        select projectname, startdate, enddate, description, currency
        from projects limit 1
        """,
        """
        select projectname, startdate, enddate, description, currency
        from projects limit 1 offset 1
        """,
        ]
        self.assertEqual(exp, mixin.executeMultipleResultsQueries(s_queries))

    def test_executeMultipleUpdateQueries(self):
        self.helper.setup_clean_db()
        my_sql_mixin = MySQLMixin()
        queries = [
        """
            insert into projects
                (projectname, description, currency)
            values
                ('test', 'a simple test', 'GBP')""",
        """
            insert into projects
                (projectname, description, currency)
            values
                ('test2', 'simple test', 'AUS')""",
        ]
        my_sql_mixin.executeMultipleUpdateQueries(queries)
        expected = [
            (u'test', None, None, u'a simple test', u'GBP'),
            (u'test2', None, None, u'simple test', u'AUS')
        ]
        query = """
        select projectname, startdate, enddate, description, currency
        from projects
        """
        self.assertEqual(expected, my_sql_mixin.executeResultsQuery(query))

    def test_executeResultsQuery(self):
        self.helper.setup_clean_db()
        my_sql_mixin = MySQLMixin()
        my_sql_mixin.executeUpdateQuery("""
            insert into projects
                (projectname, description, currency)
            values
                ('test', 'a simple test', 'GBP')""")
        expected = [(2, u'test', None, None, u'a simple test', u'GBP')]
        query = 'select * from projects'
        self.assertEqual(expected, my_sql_mixin.executeResultsQuery(query))

    def test_executeUpdateQueryWithParams(self):
        self.helper.setup_clean_db()
        my_sql_mixin = MySQLMixin()
        p = ['test3', '2012-06-04', 'description', 'LIR']
        my_sql_mixin.executeUpdateQuery("""
            insert into projects
                (projectname, startdate, enddate, description, currency)
            values
                (%s, %s, '2013-07-03', %s, %s)""", p)
        expected = [(2, u'test3', datetime.date(2012, 6, 4),
                    datetime.date(2013, 7, 3), u'description', u'LIR')]
        query = 'select * from projects'
        self.assertEqual(expected, my_sql_mixin.executeResultsQuery(query))

    def test_executeUpdateQuery(self):
        self.helper.setup_clean_db()
        my_sql_mixin = MySQLMixin()
        my_sql_mixin.executeUpdateQuery("""
            insert into projects
                (projectname, description, currency)
            values
                ('test', 'a simple test', 'GBP')""")
        expected = [(2, u'test', None, None, u'a simple test', u'GBP')]
        query = 'select * from projects'
        self.assertEqual(expected, my_sql_mixin.executeResultsQuery(query))


if __name__ == '__main__':
    unittest.main()
