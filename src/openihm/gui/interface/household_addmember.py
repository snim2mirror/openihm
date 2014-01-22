from model.alchemy_schema import Household, Householdmember
import alchemy.household as household
from data.db import session_scope
from datetime import date


class AddHouseHoldMemberLogic(object):

    def __init__(self, hhid, pid, memberid=None):
        self.household = Household(pid=pid, hhid=hhid)
        self.memberid = memberid

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

    def getExistingMember(self):
        with session_scope() as session:
            member = self._getExistingMember(session)
            session.expunge(member) # make the item usable outside the session.
            return member

    def _getExistingMember(self, session):
        house = self.household
        personid = self.memberid
        member = session.query(Householdmember).filter(Householdmember.hhid == house.hhid, Householdmember.pid == house.pid, Householdmember.personid == personid).first()
        return member

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
            if self.memberid:
                member = self._getExistingMember(session)
                member.sex = sex
                member.yearofbirth = yearofbirth
                member.headofhousehold = headhousehold
                member.reason = reason
                member.whereto = whereto
                member.periodaway = periodaway
                member.personid = memberid
                self.memberid = memberid
                # end of session implicitly writes data.
            else:
                household.addMember(session, self.household, memberid,
                                    yearofbirth, headhousehold, sex,
                                    education, periodaway, reason, whereto)
        return True
