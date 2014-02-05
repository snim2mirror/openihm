import sys
import ConfigParser


class OpenIHMConfig(ConfigParser.SafeConfigParser):

    """
    Configuration file parser based on
    ConfigParser.SafeConfigParser

    The parser is setup with defaults for most of the
    settings.

        config = OpenIHMConfig()
        config.read(CONFIGFILE)

    The config file can contain these directives,

        [database]
        host = host
        database = database
        user = user
        password = userpassword
        port = 3306
        superuser = root
        superuser_password = password
        driver = mysql+mysqldb
        log_level = WARN

    The database log level can be set to INFO to see the SQL queries
    being run by SQLalchemy.
    """

    def __init__(self):
        self.defaults = {
            'host': 'localhost',
            'database': 'openihmdb',
            'user': 'openihm',
            'password': 'ihm2010',
            'port': '3306',
            'superuser': 'root',
            'superuser_password': '',
        }
        # Fix a bug found by a user. This is caused by a change
        # in the stdlib between Python versions 2.6 and 2.7.
        version = sys.version_info
        if version[0] < 3 and version[1] < 7:
            ConfigParser.SafeConfigParser.__init__(self, self.defaults)
        else:
            ConfigParser.SafeConfigParser.__init__(self, self.defaults,
                                                   allow_no_value=True)
        self.defaults['port'] = int(self.defaults['port'])

    def database_config(self):
        """
        Returns a dictionary containing the database configuration
        information.  If it can not load the settings from the
        ini file it simply returns the default settings.

            {
                'host': 'localhost',
                'database': 'openihmdb',
                'user': 'openihm',
                'password': 'ihm2010',
                'port': 3306,
                'superuser': 'root',
                'superuser_password': '',
            }
        """
        # FIXME: should we also be returning utf8 and warnings params
        # here?
        try:
            return {
                'host':               self.get('database', 'host'),
                'database':           self.get('database', 'database'),
                'user':               self.get('database', 'user'),
                'password':           self.get('database', 'password'),
                'port':               self.getint('database', 'port'),
                'superuser':          self.get('database', 'superuser'),
                'superuser_password': self.get('database',
                                               'superuser_password'),
            }
        except ConfigParser.NoOptionError:
            return self.defaults
        except ConfigParser.NoSectionError:
            return self.defaults

    def db_log_level(self):
        try:
            return self.get('database', 'log_level')
        except (ConfigParser.NoOptionError, ConfigParser.NoSectionError):
            return 'WARN'

    def dbinfo(self):
        """
        Returns a dictionary containing the database configuration
        information.  In the format the Config object dbinfo method
        provided it.


            {
                'host': 'localhost',
                'database': 'openihmdb',
                'user': 'openihm',
                'password': 'ihm2010',
                'charset': 'utf8',
                'use_unicode'   : True,
                'get_warnings'  : True,
            }
        """
        config = self.database_config()
        # this makes the config consistent with what is currently returned.
        for key in ['superuser_password', 'superuser', 'port']:
            del config[key]
        config['charset'] = 'utf8'
        for key in ['use_unicode', 'get_warnings']:
            config[key] = True
        return config

    def get_driver(self):
        try:
            return self.get('database', 'driver')
        except ConfigParser.NoOptionError:
            pass
        except ConfigParser.NoSectionError:
            pass
        return 'mysql+mysqldb'

    def sqlalchemy_connection_string(self):
        """
        Returns a connection string for sqlalchemy.  The defaults will produce
        the following connection string,

            mysql+mysqldb://openihm:ihm2010@localhost/openihmdb

        """
        config = self.database_config()
        driver = self.get_driver()
        return "%s://%s:%s@%s/%s" % (driver, config['user'],
                                     config['password'], config['host'],
                                     config['database'])

    def sqlalchemy_superuser_connection_string(self):
        """
        Returns a connection string for the superuser for sqlalchemy.
        The defaults will produce the following connection string,

        Note: this may not work with blank passwords.  Then again it
        might.  I have no way to test it, your mileage may vary.
        """
        config = self.database_config()
        driver = self.get_driver()
        return "%s://%s:%s@%s/%s" % (driver, config['superuser'],
                                     config['superuser_password'],
                                     config['host'], config['database'])
