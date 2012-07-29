import unittest
from openihm.data.databaseinitialiser import DatabaseInitialiser, DbConfig
from openihm.inputs.config_parser import OpenIHMConfig
from openihm.data.config import Config
from includes.mysql.connector import errors
from includes.mysql.connector import Connect
import os


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
        config = OpenIHMConfig()
        read = config.read('test_openihm.cfg')
        self.assertEqual(len(read), 1,
          'Need test_openihm.cfg setup with database parameters')
        Config.set_config(config)
        self.dbconfig = config.database_config()
        self.config = DbConfig(**self.dbconfig)
        self.create_database()
        # the module uses a lot of relative paths
        # assuming they are in the openihm directory
        os.chdir('tests')

    def tearDown(self):
        # drop the database
        self.drop_database()
        os.chdir('..')

    def test___init__(self):
        database_initialiser = DatabaseInitialiser(self.config)
        # FIXME: this test is probably bogus
        # we're really just checking we manage to create the
        # object okay.
        expected = "latest update on 2012-05-16"
        self.assertEqual(expected, database_initialiser.latestupdatestring)

    def test_createDatabase(self):
        database_initialiser = DatabaseInitialiser(self.config)
        self.setup_db_file('openihmdb_mysql.sql')
        assert database_initialiser.createDatabase()

    @unittest.expectedFailure
    def test_cropsExist(self):
        database_initialiser = DatabaseInitialiser(self.config)
        self.setup_clean_db(database_initialiser)
        self.setup_db_file('openihmdb_mysql_fix59.sql')
        # FIXME: push some data into the relevant table.
        #self._execute_instruction('insert into setup_foods_crops values (%s)')
        assert database_initialiser.cropsExist()

    def test_databaseUpToDate(self):
        database_initialiser = DatabaseInitialiser(self.config)
        self.setup_clean_db(database_initialiser)
        assert database_initialiser.databaseUpToDate()

    def test_initialiseDB(self):
        database_initialiser = DatabaseInitialiser(self.config)
        self.setup_clean_db(database_initialiser)
        self.assertEqual({
            'mysqlstarted': True,
            'dbinstalled': True,
            'dbuptodate': True}, database_initialiser.initialiseDB())

    def test_insertStartupCrops(self):
        database_initialiser = DatabaseInitialiser(self.config)
        self.setup_clean_db(database_initialiser)
        self.setup_db_file('openihmdb_mysql_fix59.sql')
        assert database_initialiser.insertStartupCrops()

    def test_updateDatabase(self):
        database_initialiser = DatabaseInitialiser(self.config)
        self.setup_clean_db(database_initialiser)
        # this isn't much of a check...
        # our coverage isn't very good.
        assert database_initialiser.updateDatabase()

    def setup_clean_db(self, database_initialiser):
        self.setup_db_file('openihmdb_mysql.sql')
        self.grant_permissions()
        assert database_initialiser.createDatabase()

    def grant_permissions(self):
        c = self.config
        # FIXME: can I parametise this properly?
        self._execute_instruction(
            "grant all on %s.* to %s@localhost identified by '%s'"
            % (c.database, c.user, c.password))

    def setup_db_file(self, filename):
        # FIXME: this is all assuming the tests are run
        # from a particular directory which seems a bit weak.
        base_components = ['data', 'scripts']
        base_path = os.path.join(*base_components)
        script = os.path.join(base_path, filename)
        source_script = os.path.join('..', 'openihm', base_path, filename)
        f = open(source_script, 'r')
        out = open(script, 'w')
        import re
        schema_create = re.compile('create schema', re.I)
        use_statement = re.compile('use.*openihmdb`', re.I)
        grant_statement = re.compile('grant all on ', re.I)
        remove_db_name = re.compile('`openihmdb`\.', re.I)
        skip_statements = (schema_create, use_statement, grant_statement)
        for line in f.readlines():
            if not any([x.match(line) for x in skip_statements]):
                line = remove_db_name.sub('', line)
                out.write(line)
        f.close()
        out.close()

    def _execute_instruction(self, query, data=None):
        """
        Yet another wrapper around execute
        """
        db = Connect(**self.config.superuser_dbinfo().copy())
        cursor = db.cursor()
        cursor.execute(query, data)
        db.commit()
        db.close()

    def drop_database(self):
        self._ddl_command('drop database ' + self.config.database)

    def create_database(self):
        self._ddl_command('create database ' + self.config.database)

    def _ddl_command(self, query, params=None):
        config = self.config.superuser_dbinfo().copy()
        config['database'] = 'mysql'
        db = Connect(**config)
        cursor = db.cursor()
        cursor.execute(query, params)
        db.commit()
        db.close()

if __name__ == '__main__':
    unittest.main()
