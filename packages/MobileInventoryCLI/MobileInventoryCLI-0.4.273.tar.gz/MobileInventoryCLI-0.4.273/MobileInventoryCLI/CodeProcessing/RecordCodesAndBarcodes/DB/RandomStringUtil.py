from MobileInventoryCLI.CodeProcessing.RecordCodesAndBarcodes.DB.db import *
from password_generator import PasswordGenerator
import pint,os
from datetime import datetime,timedelta,date,time


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

class RandomStringUtilUi:
	

	def deleteOutDated(self,RID):
		with Session(ENGINE) as session:
			q=session.query(RandomString).filter(RandomString.RID==RID).first()
			print(f"Deleting {q}")
			session.delete(q)
			session.commit()
			session.flush()

	def checkForOutDated(self):
		with Session(ENGINE) as session:
			results=session.query(RandomString).all()
			ct=len(results)
			print(f"{Fore.light_green}len({Fore.light_salmon_3a}History{Fore.light_green}){Fore.medium_violet_red}={Fore.green_yellow}{ct}{Style.reset}")
			for num,i in enumerate(results):
				if i:
					if (datetime.now()-i.CDateTime).total_seconds() >= i.AgeLimit:
						print("need to delete expired! -> {num+1}/{ct} -> {i}")
						self.deleteOutDated(i.RID)

	def mkTextLower(self,text,data):
		return text.lower()

	def mkText(self,text,data):
		return text

	def mkInt(self,text,data):
		try:
			if text in ['']:
				return 0
			else:
				return int(text)
		except Exception as e:
			print(e)
			

	def __init__(self,parent,engine):
		self.checkForOutDated()
		self.term_cols=os.get_terminal_size().columns
		self.term_lines=os.get_terminal_size().lines
		ageLimit=float(pint.UnitRegistry().convert(15,"days","seconds"))
		self.ageLimit=ageLimit
		self.helpText=f'''
	ls rid,lrid,list rid,lsrid - show by id
	rm rid,rrid,rem rid,rmrid,delrid,del rid,del_rid - delete by id
	last,latest,ltst - show last created
	new,n,g,gen,generate - create a new RandomString
	show all,show_all,all,sa - show all created RandomStrings


	*Please Note that anything over the age of {ageLimit} secs will be deleted
	automatically
'''
		while True:
			fieldname='Menu'
			mode='RS'
			h=f'{Prompt.header.format(Fore=Fore,mode=mode,fieldname=fieldname,Style=Style)}'
			doWhat=Prompt.__init2__(None,func=self.mkTextLower,ptext=f"{h}Do What?",helpText=self.helpText,data=None)
			if doWhat in [None,]:
				return
			elif doWhat in ['new','n','g','gen','generate']:
				x=PasswordGenerator()
				x.minlen=16
				rstring=x.generate()				
				cdt=datetime.now()
				ctime=time(cdt.hour,cdt.minute,cdt.second)
				cdate=date(cdt.year,cdt.month,cdt.day)
				print(cdate,ctime,cdt,ageLimit,rstring,sep="\n")
				with Session(ENGINE) as session:
					npwd=RandomString(RString=rstring,AgeLimit=ageLimit,CTime=ctime,CDate=cdate,CDateTime=cdt)
					session.add(npwd)
					session.commit()
					session.refresh(npwd)
					print(npwd,"Created!")
			elif doWhat in ['last','latest','ltst']:
				with Session(ENGINE) as session:
					last=session.query(RandomString).order_by(RandomString.RID.asc()).first()
					age=(datetime.now()-last.CDateTime).total_seconds()
					print(last,f'{Fore.orange_red_1}CurrentAge(Days){Fore.light_steel_blue}={Fore.green_yellow}{round(pint.UnitRegistry().convert(age,"seconds","days"),3)}{Style.reset}',sep="\n")
			elif doWhat in ['show all','show_all','all','sa']:
				with Session(ENGINE) as session:
					everything=session.query(RandomString).order_by(RandomString.RID.asc()).all()
					ct=len(everything)
					
					for num,last in enumerate(everything):
						age=(datetime.now()-last.CDateTime).total_seconds()
						msg=f'''{'-'*round(self.term_lines/2)}
{Fore.light_green}{num+1}/{Fore.light_red}{ct}{Style.reset} -> {last}
{Fore.orange_red_1}CurrentAge(Days){Fore.light_steel_blue}={Fore.green_yellow}{round(pint.UnitRegistry().convert(age,"seconds","days"),3)}{Style.reset} 
'''
						print(msg)
			elif doWhat in ['ls rid','lrid','list rid','lsrid']:
				with Session(ENGINE) as session:
					mode='RS'
					h=f'{Prompt.header.format(Fore=Fore,mode=mode,fieldname=fieldname,Style=Style)}'
					rid=Prompt.__init2__(None,func=self.mkInt,ptext=f"{h}RID",helpText=self.helpText,data=None)
					if rid not in  [None,] and not isinstance(rid,tuple):
						last=session.query(RandomString).filter(RandomString.RID==rid).first()
						if last != None:
							age=(datetime.now()-last.CDateTime).total_seconds()
							print(last,f'{Fore.orange_red_1}CurrentAge(Days){Fore.light_steel_blue}={Fore.green_yellow}{round(pint.UnitRegistry().convert(age,"seconds","days"),3)}{Style.reset}',sep="\n")
						else:
							print(f"{Fore.light_red}No {Fore.orange_red_1}Results{Fore.light_yellow}!{Style.reset}")

			elif doWhat in ['rm rid','rrid','rem rid','rmrid','delrid','del rid','del_rid']:
				with Session(ENGINE) as session:
					mode='RS'
					h=f'{Prompt.header.format(Fore=Fore,mode=mode,fieldname=fieldname,Style=Style)}'
					rid=Prompt.__init2__(None,func=self.mkInt,ptext=f"{h}RID",helpText=self.helpText,data=None)
					if rid not in  [None,] and not isinstance(rid,tuple):
						last=session.query(RandomString).filter(RandomString.RID==rid).first()
						if last != None:
							age=(datetime.now()-last.CDateTime).total_seconds()
							print("Deleting",last,f'{Fore.orange_red_1}CurrentAge(Days){Fore.light_steel_blue}={Fore.green_yellow}{round(pint.UnitRegistry().convert(age,"seconds","days"),3)}{Style.reset}',sep="\n")
							session.delete(last)
							session.commit()
							session.flush()
						else:
							print(f"{Fore.light_red}No {Fore.orange_red_1}Results{Fore.light_yellow}!{Style.reset}")
