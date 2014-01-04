from sqlalchemy import or_
from model.alchemy_schema import Household

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
