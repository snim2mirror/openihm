import unittest
from data.db import session_scope
from database_helper import DatabaseHelper
import datetime
from model.alchemy_schema import Household, Householdcharacteristic, Project
import alchemy.household as household
import alchemy.household_members as household_members


class TestRemoveMembers(unittest.TestCase):

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
            q = household.search(session, 1, '', '')
            self.assertEqual(q.count(), 0)
            house1 = Household(hhid=40, householdname='Test', pid=2, dateofcollection=datetime.date(2012,6,4))
            house2 = Household(hhid=55, householdname='A Test 2', pid=2, dateofcollection=datetime.date(2012,6,4))
            house3 = Household(hhid=42, householdname='Test 3', pid=3, dateofcollection=datetime.date(2012,6,4))
            session.add(house1)
            session.add(house2)
            session.add(house3)
            household.addMember(session, house2, 'm4', '2010', 'No', 'Male', '', '', '', '')
            c = Householdcharacteristic(characteristic='Test', charvalue='a', hhid=42, pid=3)
            session.add(c)

    def tearDown(self):
        # drop the database
        self.helper.end_tests()

    def test_remove_members(self):
        with session_scope() as session:
            household_members.remove_members(session, 40, 2, ['m4'])

if __name__ == '__main__':
    unittest.main()
