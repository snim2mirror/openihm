import unittest
from openihm.data.databaseinitialiser import DatabaseInitialiser, DbConfig
from database_helper import DatabaseHelper


class TestDbConfig(unittest.TestCase):

    def test___init__(self):
        params = {
            'host': 'localhost',
            'database': 'openihmdb',
            'user': 'openihm',
            'password': 'ihm2010',
            'port': 3306,
            'superuser': 'root',
            'superuser_password': '',
        }
        db_config = DbConfig(**params)
        self.assertEqual(db_config.host, 'localhost')

    def test_dbinfo(self):
        params = {
            'host': 'localhost',
            'database': 'openihmdb',
            'user': 'openihm',
            'password': 'ihm2010',
            'port': 3306,
            'superuser': 'root',
            'superuser_password': 'r00tme',
        }
        db_config = DbConfig(**params)
        self.assertEqual(db_config.host, 'localhost')
        expected = {
            'host': 'localhost',
            'database': 'openihmdb',
            'user': 'openihm',
            'password': 'ihm2010',
            'charset': 'utf8',
            'use_unicode': True,
            'get_warnings': True,
        }
        self.assertEqual(expected, db_config.dbinfo())

    def test_superuser_dbinfo(self):
        params = {
            'host': 'localhost',
            'database': 'openihmdb',
            'user': 'openihm',
            'password': 'ihm2010',
            'port': 3306,
            'superuser': 'root',
            'superuser_password': 'r00tme',
        }
        db_config = DbConfig(**params)
        self.assertEqual(db_config.host, 'localhost')
        expected = {
            'host': 'localhost',
            'database': 'openihmdb',
            'user': 'root',
            'password': 'r00tme',
            'charset': 'utf8',
            'use_unicode': True,
            'get_warnings': True,
        }
        self.assertEqual(expected, db_config.superuser_dbinfo())


class TestDatabaseInitialiser(unittest.TestCase):
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
        database_initialiser = DatabaseInitialiser(self.config)
        # FIXME: this test is probably bogus
        # we're really just checking we manage to create the
        # object okay.
        expected = "latest update on 2012-05-16"
        self.assertEqual(expected, database_initialiser.latestupdatestring)

    def test_createDatabase(self):
        database_initialiser = DatabaseInitialiser(self.config)
        self.helper.setup_db_file('openihmdb_mysql.sql')
        assert database_initialiser.createDatabase()

    @unittest.expectedFailure
    def test_cropsExist(self):
        database_initialiser = DatabaseInitialiser(self.config)
        self.helper.setup_clean_db()
        self.helper.setup_db_file('openihmdb_mysql_fix59.sql')
        # FIXME: push some data into the relevant table.
        #self._execute_instruction('insert into setup_foods_crops values (%s)')
        assert database_initialiser.cropsExist()

    def test_databaseUpToDate(self):
        database_initialiser = DatabaseInitialiser(self.config)
        self.helper.setup_clean_db()
        assert database_initialiser.databaseUpToDate()

    def test_initialiseDB(self):
        database_initialiser = DatabaseInitialiser(self.config)
        self.helper.setup_clean_db()
        self.assertEqual({
            'mysqlstarted': True,
            'dbinstalled': True,
            'dbuptodate': True}, database_initialiser.initialiseDB())

    def test_insertStartupCrops(self):
        database_initialiser = DatabaseInitialiser(self.config)
        self.helper.setup_clean_db()
        self.helper.setup_db_file('openihmdb_mysql_fix59.sql')
        assert database_initialiser.insertStartupCrops()

    def test_updateDatabase(self):
        database_initialiser = DatabaseInitialiser(self.config)
        self.helper.setup_clean_db()
        # this isn't much of a check...
        # our coverage isn't very good.
        assert database_initialiser.updateDatabase()


if __name__ == '__main__':
    unittest.main()
