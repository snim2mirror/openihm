import ConfigParser


class OpenIHMConfig(ConfigParser.SafeConfigParser):

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
