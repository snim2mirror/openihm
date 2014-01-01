from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation
from sqlalchemy.dialects.mysql import *

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

