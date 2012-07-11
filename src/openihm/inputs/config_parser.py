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
        ConfigParser.SafeConfigParser.__init__(self, self.defaults,
                                                allow_no_value=True)

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
                'port': '3306',
                'superuser': 'root',
                'superuser_password': '',
            }
        """
        try:
            return {
                'host':               self.get('database', 'host'),
                'database':           self.get('database', 'database'),
                'user':               self.get('database', 'user'),
                'password':           self.get('database', 'password'),
                'port':               self.get('database', 'port'),
                'superuser':          self.get('database', 'superuser'),
                'superuser_password': self.get('database',
                                                  'superuser_password'),
            }
        except ConfigParser.NoSectionError, e:
            return self.defaults

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
                'charset', 'utf8',
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

