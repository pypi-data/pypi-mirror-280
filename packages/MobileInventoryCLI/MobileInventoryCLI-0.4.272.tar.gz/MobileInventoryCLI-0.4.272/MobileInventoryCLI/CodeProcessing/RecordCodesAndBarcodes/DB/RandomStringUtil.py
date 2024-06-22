from MobileInventoryCLI.CodeProcessing.RecordCodesAndBarcodes.DB.db import *


class RandomString(BASE,Template):
	__tablename__="RandomString"
	RID=Column(Integer,primary_key=True)
	RString=Column(String)
	CDateTime=Column(DateTime)
	CDate=Column(Date)
	CTime=Column(Time)
	AgeLimit=Column(Float)
	
	def __init__(self,**kwargs):
		for k in kwargs.keys():
			if k in [s.name for s in self.__table__.columns]:
				setattr(self,k,kwargs.get(k))
				
				
				
RandomString.metadata.create_all(ENGINE)