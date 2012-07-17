import unittest
from openihm.data.config import Config

class dummy_config:

    def dbinfo(self):
        return { 'a' : 'b' }

class TestConfig(unittest.TestCase):

    def test_dbinfo(self):
        Config.set_config(dummy_config())
        self.assertEqual(Config.dbinfo(), { 'a' : 'b' })

if __name__ == '__main__':
    unittest.main()
