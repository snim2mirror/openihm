import unittest
from openihm.data.databaseinitialiser import DatabaseInitialiser, DbConfig
from openihm.inputs.config_parser import OpenIHMConfig
from openihm.data.config import Config
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

    def setUp(self):
        config = OpenIHMConfig()
        read = config.read('test_openihm.cfg')
        self.assertEqual(len(read), 1, 'Need test_openihm.cfg setup with database parameters') 
        Config.set_config(config)
        self.dbconfig = config.database_config()
        self.config = DbConfig(**self.dbconfig)
        # the module uses a lot of relative paths
        # assuming they are in the openihm directory
        # FIXME: perhaps I should use a different directory to
        # allow me to use a test version of the SQL schema.
        os.chdir('tests')

    def tearDown(self):
        # drop the database
        os.chdir('..')
        pass

    def test___init__(self):
        database_initialiser = DatabaseInitialiser(self.config)
        # FIXME: this test is probably bogus 
        # we're really just checking we manage to create the 
        # object okay.
        expected = "latest update on 2012-05-16" 
        self.assertEqual(expected, database_initialiser.latestupdatestring)

    def test_createDatabase(self):
        database_initialiser = DatabaseInitialiser(self.config)
        self.clear_database()
        self.setup_db_file('openihmdb_mysql.sql')
        assert database_initialiser.createDatabase()

    def setup_clean_db(self, database_initialiser):
        self.clear_database()
        self.setup_db_file('openihmdb_mysql.sql')
        self.grant_permissions()
        assert database_initialiser.createDatabase()

    def grant_permissions(self):
        c = self.config
        # FIXME: can I parametise this properly?
        self._execute_instruction("grant all on %s.* to %s@localhost identified by '%s'" % (c.database, c.user, c.password))

    def clear_database(self):
        self._execute_instruction('delete from dbupdate');

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
            if not any([ x.match(line) for x in skip_statements ]):
                line = remove_db_name.sub('', line)
                out.write(line)
        f.close()
        out.close()

    def _execute_instruction(self, query, data = None):
        """
        Yet another wrapper around execute 
        """ 
        db = Connect( **self.config.superuser_dbinfo().copy() )
        cursor = db.cursor()
        cursor.execute(query, data);
        db.commit()
        db.close()

    @unittest.expectedFailure
    def test_cropsExist(self):
        database_initialiser = DatabaseInitialiser(self.config)
        self.setup_clean_db(database_initialiser)
        # FIXME: push some data into the relevant table.
        #self._execute_instruction('insert into setup_foods_crops values (%s)')
        assert database_initialiser.cropsExist()

    def test_databaseUpToDate(self):
        database_initialiser = DatabaseInitialiser(self.config)
        self.setup_clean_db(database_initialiser)
        assert database_initialiser.databaseUpToDate()

    def test_initialiseDB(self):
        database_initialiser = DatabaseInitialiser(self.config)
        # database_initialiser = DatabaseInitialiser(config)
        # self.assertEqual(expected, database_initialiser.initialiseDB())
        assert False # TODO: implement your test here

    def test_insertStartupCrops(self):
        database_initialiser = DatabaseInitialiser(self.config)
        self.setup_clean_db(database_initialiser)
        self.setup_db_file('openihmdb_mysql_fix59.sql')
        assert database_initialiser.insertStartupCrops()

    def test_updateDatabase(self):
        database_initialiser = DatabaseInitialiser(self.config)
        # database_initialiser = DatabaseInitialiser(config)
        # self.assertEqual(expected, database_initialiser.updateDatabase())
        assert False # TODO: implement your test here

if __name__ == '__main__':
    unittest.main()
