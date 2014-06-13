from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String, DateTime, Time
from decimal import Decimal
from sqlalchemy import Numeric

engine = create_engine('sqlite:///:swp_flares.db')
Base = declarative_base()

class Xrayflux(Base):
    __tablename__ = 'Xrayflux'
    
    id = Column(Integer, primary_key=True, nullable=False)
    ut_datetime = Column(DateTime, nullable = False)
    short = Column(Numeric(14,12))
    longx = Column(Numeric(14,12))
    
    def __repr__(self):
        return "<Xrayflux({},{},{})>".format(self.ut_datetime, self.short, self.longx)


class Solarsoft(Base):
    __tablename__ = 'Solarsoft'
    
    event =Column(Integer, primary_key=True, nullable=False)
    ut_datetime = Column(DateTime, nullable = False)
    peak = Column(Time, nullable=False)
    goes_class = Column(Numeric(14,12))
    derived_time = Column(String(20))
    
	def __repr__(self):
    		return "<Solarsoft({},{},{},{})>".format(self.ut_datetime, self.peak, self.goes_class, self.derived_time)


Base.metadata.create_all(engine)   
session = Session(bind=engine)



