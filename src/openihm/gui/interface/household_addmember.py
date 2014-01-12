from model.alchemy_schema import Household
import alchemy.household as household
from data.db import session_scope
from datetime import date


class AddHouseHoldMemberLogic(object):

    def __init__(self, hhid, pid):
        self.household = Household(pid=pid, hhid=hhid)

    def thisYear(self):
        return date.today().year

    def yearOfBirth(self, age):
        thisyear = self.thisYear()
        if age is not None and age != "":
            yearOfBirth = thisyear - int(age)
            return "%i" % yearOfBirth
        return None

    def age(self, yearOfBirth):
        thisyear = self.thisYear()
        age = thisyear - int(yearOfBirth)
        return "%i" % age

    def saveMember(self, sex, age, yearofbirth, headOfHousehold, periodaway,
                   reason, whereto):
        education = ""
        if sex == "Male":
            memberid = "m%s" % age
        else:
            memberid = "f%s" % age
        if headOfHousehold:
            headhousehold = "Yes"
        else:
            headhousehold = "No"

        with session_scope() as session:
            household.addMember(session, self.household, memberid,
                                yearofbirth, headhousehold, sex,
                                education, periodaway, reason, whereto)
        return True
