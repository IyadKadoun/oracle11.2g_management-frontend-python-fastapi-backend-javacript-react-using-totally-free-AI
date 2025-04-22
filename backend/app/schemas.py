from pydantic import BaseModel

class JABICENTERBase(BaseModel):
    NB: int
    NAME: str

    class Config:
        orm_mode = True

class COLLECTORBase(BaseModel):
    USERNAME: str
    TOPMARGIN: int | None = None
    LEFTMARGIN: int | None = None
    SCOP: str | None = None
    CENTER: str | None = None
    BILLREP: int | None = None
    ACCNB: str | None = None
    ACCNO: str | None = None
    JABICENTER: int | None = None
    ACCNOFEE: str | None = None
    ACCNOR: str | None = None
    ACCNOC: str | None = None
    CANWORK: str
    JABIINCOME: str | None = None
    PAYTO: int | None = None
    SCOPTYPE: str | None = None
    COLLTYPE: int | None = None
    DEFSCOP: str | None = None
    ACCREBUILDTAX: str | None = None
    ACCARMTAX: str | None = None
    ACCARMMAHALITAX: str | None = None
    DEPT: str
    MAXBILLVAL: int | None = None
    MAXPAYMENT: int | None = None
    RASEEDNULLDAYS: int | None = None
    ISSUETYPE: str | None = None
    STOPMI: int | None = None
    STOPHH: int | None = None
    CANPRINT: str | None = None
    CANMODIFY: str | None = None

    class Config:
        orm_mode = True

class CLEARANCETYPBase(BaseModel):
    NB: int
    NAME: str

    class Config:
        orm_mode = True