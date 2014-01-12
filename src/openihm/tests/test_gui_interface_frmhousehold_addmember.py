import unittest
from gui.interface.household_addmember import AddHouseHoldMemberLogic
from database_helper import DatabaseHelper
from data.db import session_scope
from model.alchemy_schema import Household
import datetime

class TestAddHouseHoldMemberLogic(unittest.TestCase):
    def test___init__(self):
        add_house_hold_member_logic = AddHouseHoldMemberLogic(10, 10)

    def test_age(self):
        add_house_hold_member_logic = AddHouseHoldMemberLogic(10, 10)
        # make the tests work on different dates.
        AddHouseHoldMemberLogic.thisYear = lambda x: 2014 
        self.assertEqual("4", add_house_hold_member_logic.age("2010"))

    def test_saveMember(self):
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
            house1 = Household(hhid=40, householdname='Test', pid=2, dateofcollection=datetime.date(2012,6,4))
            session.add(house1)
        add_house_hold_member_logic = AddHouseHoldMemberLogic(40, 2)
        assert add_house_hold_member_logic.saveMember('Male', "10", "2004", "No", "", "", "")
        self.helper.end_tests()

    def test_yearOfBirth(self):
        add_house_hold_member_logic = AddHouseHoldMemberLogic(10, 10)
        AddHouseHoldMemberLogic.thisYear = lambda x: 2014
        self.assertEqual("2010", add_house_hold_member_logic.yearOfBirth("4"))

if __name__ == '__main__':
    unittest.main()
