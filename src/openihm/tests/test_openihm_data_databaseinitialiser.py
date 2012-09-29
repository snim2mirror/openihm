import unittest
from data.databaseinitialiser import DatabaseInitialiser, DbConfig
from database_helper import DatabaseHelper
from datetime import date


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

    def test_databaseUpToDate_needupdate(self):
        database_initialiser = DatabaseInitialiser(self.config)
        self.helper.setup_clean_db()
        self.make_db_outofdate()
        assert not database_initialiser.databaseUpToDate()

    def test_databaseUpToDate_fresh_db(self):
        database_initialiser = DatabaseInitialiser(self.config)
        self.helper.setup_clean_db()
        self.helper.execute_instruction('delete from dbupdate')
        assert database_initialiser.databaseUpToDate()

    def make_db_outofdate(self):
        updatestr = "latest update on %s" % (date.min.isoformat())
        self.helper.execute_instruction(
            "update dbupdate set lastupdate = %s", [updatestr])

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

    def test_setupStartupCrops(self):
        database_initialiser = DatabaseInitialiser(self.config)
        self.helper.setup_clean_db()
        self.helper.setup_db_file('openihmdb_mysql_fix59.sql')
        assert database_initialiser.setupStartupCrops()

    def test_updateDatabase(self):
        # NOTE: it might be worth adding a test that compares the new
        # database to the updated database to check they match.
        database_initialiser = DatabaseInitialiser(self.config)
        self.helper.setup_clean_db()
        # this isn't much of a check...
        # our coverage isn't very good.
        assert database_initialiser.updateDatabase()

    def test_updateDatabase_needs_update(self):
        database_initialiser = DatabaseInitialiser(self.config)
        self.helper.setup_clean_db()
        self.make_db_outofdate()
        self.helper.setup_db_file('openihmdb_mysql_update.sql')
        assert database_initialiser.updateDatabase()


if __name__ == '__main__':
    unittest.main()
