from model.alchemy_schema import Householdmember


def remove_members(session, hhid, pid, people_ids):
    q = session.query(Householdmember).filter(Householdmember.hhid == hhid,
                                              Householdmember.pid == pid,
                                              Householdmember.personid.in_(people_ids))
    q.delete(synchronize_session=False)
