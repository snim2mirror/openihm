import os
from data.config import Config
from inputs.config_parser import OpenIHMConfig
from includes.mysql.connector import errors
from includes.mysql.connector import Connect
from data.databaseinitialiser import DatabaseInitialiser, DbConfig
import unittest
import logging
import logging.handlers



class DatabaseHelper(object):

    # the module uses a lot of relative paths
    # assuming they are in the openihm directory
    def __init__(self):
        config = OpenIHMConfig()
        self.real_config = config
        self.test_dir = os.path.dirname(__file__)
        config_file = os.path.join(self.test_dir, '..', 'test_openihm.cfg')
        read = config.read(config_file)
        if len(read) != 1:
            m = 'Need test_openihm.cfg setup with database parameters'
            e = unittest.SkipTest(m)
            raise e
        Config.set_config(config)
        self.dbconfig = config.database_config()
        self.config = DbConfig(**self.dbconfig)

    def getConfig(self):
        return self.config

    def setup_logging(self):
         log = logging.getLogger('sqlalchemy.engine')
         handler = logging.handlers.RotatingFileHandler('tests.log', backupCount=5)
         if not log.handlers:
             log.addHandler(handler)
         levels = { 
            'DEBUG': logging.DEBUG,
            'INFO': logging.INFO,
            'WARN': logging.WARN,
            'ERROR': logging.ERROR,
            'CRITICAL': logging.CRITICAL,
         }
         level = levels.get(self.real_config.db_log_level(), logging.WARN)
         log.setLevel(level)
         log.info('------------------- New test --------------------')
         self.log = log

    def start_tests(self):
        self.setup_logging()
        self.drop_database()
        self.prev_path = os.getcwd()
        os.chdir(self.test_dir)
        self.create_database()
        self.create_indicator_table()

    def end_tests(self):
        os.chdir(self.prev_path)
        self.drop_database()

    def setup_clean_db(self):
        database_initialiser = DatabaseInitialiser(self.config)
        self.setup_db_file('openihmdb_mysql.sql')
        self.grant_permissions()
        assert database_initialiser.createDatabase()

    def grant_permissions(self):
        c = self.config
        # FIXME: can I parametise this properly?
        try:
            self.execute_instruction(
                "grant all on %s.* to %s@localhost identified by '%s'"
                % (c.database, c.user, c.password))
        except:
            # this might fail and be OK if the 'superuser' doesn't have grant permissions
            # and the 'user' has already been granted permissions
            print "warning: failed to grant permissions to use %s database to user %s" % (c.database, c.user)
            print "if you know the user already has the correct permissions you can ignore this warning"

    def setup_db_file(self, filename):
        # FIXME: this is all assuming the tests are run
        # from a particular directory which seems a bit weak.
        base_components = ['data', 'scripts']
        base_path = os.path.join(*base_components)
        script = os.path.join(base_path, filename)
        source_script = os.path.join('..', base_path, filename)
        f = open(source_script, 'r')
        out = open(script, 'w')
        import re
        schema_create = re.compile('create schema', re.I)
        use_statement = re.compile('use.*openihmdb`', re.I)
        grant_statement = re.compile('grant all on ', re.I)
        remove_db_name = re.compile('`openihmdb`\.', re.I)
        db_name = re.compile('`openihmdb`', re.I)
        skip_statements = (schema_create, grant_statement)
        for line in f.readlines():
            if use_statement.match(line):
                line = db_name.sub('`' + self.config.database + '`', line)
            if not any([x.match(line) for x in skip_statements]):
                line = remove_db_name.sub('', line)
                out.write(line)
        f.close()
        out.close()

    def execute_instruction(self, query, data=None):
        """
        Yet another wrapper around execute
        """
        db = Connect(**self.config.superuser_dbinfo().copy())
        cursor = db.cursor()
        cursor.execute(query, data)
        db.commit()
        db.close()
        return cursor

    def execute_select(self, query, data=None):
        """
        Yet another wrapper around queries
        """
        db = Connect(**self.config.superuser_dbinfo().copy())
        cursor = db.cursor()
        cursor.execute(query, data)
        yield cursor.fetchall()
        db.close()

    def create_indicator_table(self):
        # this is an attempt to ensure we don't accidentally
        # blow away a database we're not supposed to.
        self.execute_instruction("""
            create table openihm_test_table (test varchar(1))""")

    def test_indicator_present(self):
        rows = self.execute_select("show tables like 'openihm_test_table'")
        l = [x for x in rows]
        return len(l) == 1

    def drop_database(self):
        try:
            if self.test_indicator_present():
                self._ddl_command('drop database ' + self.config.database)
        except errors.ProgrammingError:
            pass

    def create_database(self):
        self._ddl_command('create database ' + self.config.database)

    def _ddl_command(self, query, params=None):
        config = self.config.superuser_dbinfo().copy()
        del(config['database'])
        db = Connect(**config)
        cursor = db.cursor()
        cursor.execute(query, params)
        db.commit()
        db.close()
