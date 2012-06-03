import unittest
from openihm.inputs.config_parser import OpenIHMConfig


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
            'port': '3306',
            'superuser': 'root',
            'superuser_password': '',
        }
        self.assertEqual(expected, open_ihm_config.database_config())

if __name__ == '__main__':
    unittest.main()
