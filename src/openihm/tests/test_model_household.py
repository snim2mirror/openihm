import unittest
from database_helper import DatabaseHelper

from data.db import session_scope
from model.alchemy_schema import house_search, Household

class TestModelHouseHold(unittest.TestCase):
    """
    In order to use these tests you need to have a config file named
    test_openihm.cfg in the directory you are running the tests from
    (i.e. the src directory).

        [database]
        superuser = root
        superuser_password = s00pers3cur3
        database = test_openihm
        user = openihm
        password = ihm2012

    This should contain database credentials for a database that exists
    in mysql for testing.  This database will be toyed around with a lot.
    Obviously avoid pointing it at a database you care about...

    """

    def setUp(self):
        self.helper = DatabaseHelper()
        self.config = self.helper.getConfig()
        self.helper.start_tests()

    def tearDown(self):
        # drop the database
        self.helper.end_tests()

    def test_household_search(self):
        self.helper.setup_clean_db()
        with session_scope() as session:
            self.assertEqual(session.query(Household).count(), 0)
            q = house_search(session, 1, '', '')
            self.assertEqual(q.count(), 0)
            # FIXME: things to test,
            # a) no effective paramaters
            # b) just number
            # c) just name
            # d) both
            # e) like works
            # f) count and results work as expected.
            # g) ensure different projects don't clash
