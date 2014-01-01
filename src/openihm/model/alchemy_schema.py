from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation
from sqlalchemy.dialects.mysql import *
from sqlalchemy import or_

DeclarativeBase = declarative_base()
metadata = DeclarativeBase.metadata

class Household(DeclarativeBase):
    __tablename__ = 'households'
    __table_args__ = {}

    hhid = Column(u'hhid', Integer, primary_key=True, autoincrement=False, nullable=False)
    householdname = Column(u'householdname', VARCHAR(length=100), nullable=False)
    totalassetvalue = Column(u'totalassetvalue', DOUBLE(asdecimal=True), nullable=False, server_default=text(u"'0'"))
    totalincomevalue = Column(u'totalincomevalue', DOUBLE(asdecimal=True), nullable=False, server_default=text(u"'0'"))
    totalexpenditure = Column(u'totalexpenditure', DOUBLE(asdecimal=True), nullable=False, server_default=text(u"'0'"))
    dateofcollection = Column(u'dateofcollection', DATE(), nullable=False)
    pid = Column(u'pid', Integer, primary_key=True, nullable=False)
    # ForeignKeyConstraint([u'pid'],
    #                      [u'projects.pid'],
    #                      ondelete='CASCADE', onupdate='CASCADE',
    #                      name=u'fk_households_projects1'),
    # )

def house_search(session, project_id, name, number):
    """
    Searches for house holds within the project with the name or number
    specified.  If name or number are blank strings they are not included
    in the query.  Uses a like query to query the name.
    """
    q = session.query(Household).filter(Household.pid == project_id)
    if name != "":
        name = '%' + name + '%'
        if number == "":
            q = q.filter(Household.householdname.like(name))
        else:
            q = q.filter(or_(Household.householdname.like(name), 
                                Household.hhid == number))
    elif number != "":
        q = q.filter(Household.hhid == number)
    return q

