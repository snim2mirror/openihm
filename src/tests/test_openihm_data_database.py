import unittest
from database_helper import DatabaseHelper
from openihm.data.database import Database
import os


class TestDatabase(unittest.TestCase):
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
        self.config = self.helper.getConfig()
        self.helper.start_tests()

    def tearDown(self):
        # drop the database
        self.helper.end_tests()

    def test___init__(self):
        database = Database()
        self.assertEqual(self.config.dbinfo(), database.config)

    def test_close(self):
        database = Database()
        database.open()
        database.close()

    @unittest.expectedFailure
    def test_databaseExists(self):
        database = Database()
        assert database.databaseExists()

    @unittest.expectedFailure
    def test_databaseServerRunning(self):
        database = Database()
        assert database.databaseServerRunning()

    def test_execDefinitionQuery(self):
        self.helper.setup_clean_db()
        database = Database()
        database.open()
        database.execDefinitionQuery('create table simples (test int)')
        database.close()
        # and just to provie it's there to put something into.
        database.open()
        database.execUpdateQuery('insert into simples values (3)')
        database.close()

    def test_execSelectQuery(self):
        self.helper.setup_clean_db()
        self.helper.execute_instruction("""
            insert into projects
                (projectname, startdate, enddate, description, currency)
            values
                ('test', 2012-06-04, 2013-07-03, 'a simple test', 'GBP')""")
        database = Database()
        query = 'select * from projects'
        database.open()
        self.assertEqual([(2, u'test', None, None, u'a simple test', u'GBP')],
                        database.execSelectQuery(query))
        database.close()

    def test_execUpdateQuery(self):
        self.helper.setup_clean_db()
        database = Database()
        database.open()
        database.execUpdateQuery("""
            insert into projects
                (projectname, startdate, enddate, description, currency)
            values
                ('test', 2012-06-04, 2013-07-03, 'a simple test', 'GBP')""")
        query = 'select * from projects'
        self.assertEqual([(2, u'test', None, None, u'a simple test', u'GBP')],
                        database.execSelectQuery(query))
        database.close()

    def test_open(self):
        database = Database()
        database.open()

if __name__ == '__main__':
    unittest.main()
