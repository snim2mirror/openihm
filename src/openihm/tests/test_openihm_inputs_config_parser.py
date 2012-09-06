import unittest
from inputs.config_parser import OpenIHMConfig
import io


class TestOpenIHMConfig(unittest.TestCase):
    def test___init__(self):
        open_ihm_config = OpenIHMConfig()

    def test_database_config(self):
        open_ihm_config = OpenIHMConfig()

        expected = {
            'host': 'localhost',
            'database': 'openihmdb',
            'user': 'openihm',
            'password': 'ihm2010',
            'port': 3306,
            'superuser': 'root',
            'superuser_password': '',
        }
        self.assertEqual(expected, open_ihm_config.database_config())

    def test_read_config_file(self):
        open_ihm_config = OpenIHMConfig()
        config_file = """
[database]
superuser = master
superuser_password = password
port = 3307
        """
        open_ihm_config.readfp(io.BytesIO(config_file))
        expected = {
            'host': 'localhost',
            'database': 'openihmdb',
            'user': 'openihm',
            'password': 'ihm2010',
            'port': 3307,
            'superuser': 'master',
            'superuser_password': 'password',
        }
        self.assertEqual(expected, open_ihm_config.database_config())

    def test_read_config_file_port_default(self):
        open_ihm_config = OpenIHMConfig()
        config_file = """
[database]
superuser = master
superuser_password = password
        """
        open_ihm_config.readfp(io.BytesIO(config_file))
        expected = {
            'host': 'localhost',
            'database': 'openihmdb',
            'user': 'openihm',
            'password': 'ihm2010',
            'port': 3306,
            'superuser': 'master',
            'superuser_password': 'password',
        }
        self.assertEqual(expected, open_ihm_config.database_config())

    def test_database_config_dbinfo(self):
        open_ihm_config = OpenIHMConfig()
        expected = {
            'host': 'localhost',
            'database': 'openihmdb',
            'user': 'openihm',
            'password': 'ihm2010',
            'charset': 'utf8',
            'use_unicode': True,
            'get_warnings': True,
        }
        self.assertEqual(expected, open_ihm_config.dbinfo())

    def test_sqlalchemy_config(self):
        open_ihm_config = OpenIHMConfig()
        expected = 'mysql+mysqldb://openihm:ihm2010@localhost/openihmdb'
        self.assertEqual(expected,
                        open_ihm_config.sqlalchemy_connection_string())

    def test_sqlalchemy_config_file(self):
        open_ihm_config = OpenIHMConfig()
        config_file = """
[database]
superuser = master
superuser_password = password
driver = mysql+mysqlconnector
        """
        open_ihm_config.readfp(io.BytesIO(config_file))
        expected = 'mysql+mysqlconnector://master:password@localhost/openihmdb'
        self.assertEqual(expected,
                    open_ihm_config.sqlalchemy_superuser_connection_string())

if __name__ == '__main__':
    unittest.main()
