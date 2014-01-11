from sqlalchemy import or_
from model.alchemy_schema import Household, Householdmember

def remove_house(session, project_id, numbers):
    q = session.query(Household).filter(Household.pid == project_id, Household.hhid.in_(numbers))
    q.delete(synchronize_session=False)

def search(session, project_id, name='', number=''):
    """
    Searches for households within the project with the name or number
    specified.  If name or number are blank strings they are not included
    in the query.  Uses a like query to query the name.
    """
    q = session.query(Household).filter(Household.pid == project_id)
    params = []
    if name != "":
        params.append(Household.householdname.like('%' + name + '%'))
    if number != "":
        params.append(Household.hhid == number)
    if len(params) > 0:
        q = q.filter(or_(*params))
    return q

def memberSearch(session, house):
    q = session.query(Householdmember).filter(Householdmember.hhid == house.hhid, Householdmember.pid == house.pid)
    return q

def existsMember(session, house, personid):
    return memberSearch(session, house).filter(Householdmember.personid == personid).count() > 0

def addMember(session, house, personid, yearofbirth, headhousehold, sex, education, periodaway, reason, whereto):
    # the person id is a combination of the sex and age so multiple people of the same age/sex
    # require a little tweaking
    # sN....
    num = 1
    # take care of twins
    oldpersonid = personid
    while existsMember(session, house, personid):
        personid = oldpersonid +"_%i" % num
        num = num + 1
    m = Householdmember(education=education, sex=sex, periodaway=periodaway, 
                        personid=personid, yearofbirth=yearofbirth,
                        whereto=whereto, hhid=house.hhid, pid=house.pid,
                        headofhousehold=headhousehold, reason=reason)
    session.add(m)
