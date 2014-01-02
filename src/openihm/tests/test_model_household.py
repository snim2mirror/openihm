import unittest
from database_helper import DatabaseHelper
import datetime

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
        self.helper.setup_clean_db()

        self.helper.execute_instruction("""
            insert into projects
              (projectname, startdate, enddate, description, currency)
            values
              ('test', '2012-06-04', '2013-07-03', 'a simple test', 'GBP')""")
        self.helper.execute_instruction("""
            insert into projects
              (projectname, startdate, enddate, description, currency)
            values
              ('test 2', '2012-06-04', '2013-07-03', 'another simple test', 'GBP')""")
        with session_scope() as session:
            self.assertEqual(session.query(Household).count(), 0)
            q = house_search(session, 1, '', '')
            self.assertEqual(q.count(), 0)
            house1 = Household(hhid=40, householdname='Test', pid=2, dateofcollection=datetime.date(2012,6,4))
            house2 = Household(hhid=55, householdname='A Test 2', pid=2, dateofcollection=datetime.date(2012,6,4))
            house3 = Household(hhid=42, householdname='Test 3', pid=3, dateofcollection=datetime.date(2012,6,4))
            session.add(house1)
            session.add(house2)
            session.add(house3)

    def tearDown(self):
        # drop the database
        self.helper.end_tests()

    def test_household_search(self):
        # a) no effective paramaters
        with session_scope() as session:
            q = house_search(session, 1, '', '')
            self.assertEqual(q.count(), 0)
            q = house_search(session, 2, '', '')
            self.assertEqual(q.count(), 2)
            q = house_search(session, 3, '', '')
            self.assertEqual(q.count(), 1)
            # g) ensure different projects don't clash - gets tested implicitly

    def test_number(self):
        # b) just number
        with session_scope() as session:
            q = house_search(session, 2, name='', number='55')
            self.assertEqual(q.count(), 1)
            q = house_search(session, 2, '', '33')
            self.assertEqual(q.count(), 0)

    def test_name(self):
        # c) just name
        with session_scope() as session:
            q = house_search(session, 3, 'Test 3', '')
            self.assertEqual(q.count(), 1)

    def test_both(self):
        # d) both
        with session_scope() as session:
            q = house_search(session, 2, 'Test', '40')
            self.assertEqual(q.count(), 2)
            q2 = house_search(session, 2, 'A Test', '55')
            self.assertEqual(q2.count(), 1)
            q2 = house_search(session, 2, 'A Test 2', '40')
            self.assertEqual(q2.count(), 2)
            q2 = house_search(session, 2, 'Not', '55')
            self.assertEqual(q2.count(), 1)

    def test_like(self):
        # e) like works
        with session_scope() as session:
            q = house_search(session, 2, 'Test', '')
            self.assertEqual(q.count(), 2)
            q2 = house_search(session, 2, 'A Test', '')
            self.assertEqual(q2.count(), 1)
            q2 = house_search(session, 2, 'A Test 2', '')
            self.assertEqual(q2.count(), 1)
            q2 = house_search(session, 2, 'Not', '')
            self.assertEqual(q2.count(), 0)

    def test_results(self):
        # f) count and results work as expected.
        with session_scope() as session:
            q = house_search(session, 2, '', '')
            self.assertEqual(q.count(), 2)
            l = [ (h.hhid, h.householdname) for h in q ]
            self.assertEqual(l, [(40, 'Test'), (55, 'A Test 2')])
