import ConfigParser

class OpenIHMConfig(ConfigParser.SafeConfigParser):

    def __init__(self):
        ConfigParser.SafeConfigParser.__init__(self, { 
            'host': 'localhost',
            'database': 'openihmdb',
            'user': 'openihm',
            'password': 'ihm2010',
            'port': '3306',
            'superuser': 'root', 
            'superuser_password': '',
        },
        allow_no_value=True)

    def database_config(self):
        # FIXME: need to deal gracefully with config file not existing.
        return {
            'host':                 self.get('database', 'host'),
            'database':             self.get('database', 'database'),
            'user':                 self.get('database', 'user'),
            'password':             self.get('database', 'password'),
            'port':                 self.get('database', 'port'),
            'superuser':            self.get('database', 'superuser'),
            'superuser_password':   self.get('database', 'superuser_password'),
        }

