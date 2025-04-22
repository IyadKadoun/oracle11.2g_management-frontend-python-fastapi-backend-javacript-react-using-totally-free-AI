from sqlalchemy import Column, Integer, String,Numeric
from .database import Base

class JABICENTER(Base):
    __tablename__ = "JABICENTER"
    NB = Column(Numeric(3), primary_key=True)
    NAME = Column(String(100))

class COLLECTOR(Base):
    __tablename__ = "COLLECTOR"
    USERNAME = Column(String(40), primary_key=True)
    TOPMARGIN = Column(Numeric(4))
    LEFTMARGIN = Column(Numeric(4))
    SCOP = Column(String(4000))
    CENTER = Column(String(3))
    BILLREP = Column(Numeric(1))
    ACCNB = Column(String(20))
    ACCNO = Column(String(20))
    JABICENTER = Column(Numeric(3))
    ACCNOFEE = Column(String(30))
    ACCNOR = Column(String(30))
    ACCNOC = Column(String(30))
    CANWORK = Column(String(1), nullable=False)
    JABIINCOME = Column(String(40))
    PAYTO = Column(Numeric(2))
    SCOPTYPE = Column(String(10))
    COLLTYPE = Column(Numeric(1))
    DEFSCOP = Column(String(4000))
    ACCREBUILDTAX = Column(String(30))
    ACCARMTAX = Column(String(30))
    ACCARMMAHALITAX = Column(String(30))
    DEPT = Column(String(2), nullable=False)
    MAXBILLVAL = Column(Numeric(10))
    MAXPAYMENT = Column(Numeric(10))
    RASEEDNULLDAYS = Column(Numeric(3))
    ISSUETYPE = Column(String(1))
    STOPMI = Column(Numeric(2))
    STOPHH = Column(Numeric(2))
    CANPRINT = Column(String(1))
    CANMODIFY = Column(String(1))

class CLEARANCETYP(Base):
    __tablename__ = "CLEARANCETYP"
    NB = Column(Numeric(6), primary_key=True)
    NAME = Column(String(100))