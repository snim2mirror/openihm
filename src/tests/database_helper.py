import os
from openihm.data.config import Config
from openihm.inputs.config_parser import OpenIHMConfig
from includes.mysql.connector import errors
from includes.mysql.connector import Connect
from openihm.data.databaseinitialiser import DatabaseInitialiser, DbConfig
from openihm.inputs.config_parser import OpenIHMConfig


class DatabaseHelper(object):

    # the module uses a lot of relative paths
    # assuming they are in the openihm directory
    def __init__(self, unittest):
        config = OpenIHMConfig()
        read = config.read('test_openihm.cfg')
        unittest.assertEqual(len(read), 1,
          'Need test_openihm.cfg setup with database parameters')
        Config.set_config(config)
        self.dbconfig = config.database_config()
        self.config = DbConfig(**self.dbconfig)

    def getConfig(self):
        return self.config

    def start_tests(self):
        os.chdir('tests')
        self.create_database()

    def end_tests(self):
        self.drop_database()
        os.chdir('..')

    def setup_clean_db(self):
        database_initialiser = DatabaseInitialiser(self.config)
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
