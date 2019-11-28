import subprocess as sp
import pymysql
import pymysql.cursors

def addmem():
	try:
		row = {}
		print("Enter Member details: ")
		row["MID"] = input("MID: ")
		row["Fname"] = input("Fname: ")
		row["Mname"] = input("Mname: ")
		row["Lname"] = input("Lname: ")
		address=input("Address(Street Locality): ")
		row["Street"] = address.split(" ")[0]
		row["Locality"] = address.split(" ")[1]
		row["Weight"] = int(input("Weight: "))
		row["Gender"] = input("Gender: ")
		row["DOB"] = input("DOB (YYYY-MM-DD): ")
		row["CID"] = input("Course ID: ")
		row["TID"] = input("Trainer ID: ")
		row["Age"] = 2019-int(row["DOB"].split("-")[0])
		query="INSERT INTO MEMBERS(MID,Fname,Mname,Lname,Weight,Gender,DOB,Age,CID,TID) VALUES('%s','%s','%s','%s','%d','%s','%s','%d','%s','%s')" %(row["MID"],row["Fname"],row["Mname"],row["Lname"],row["Weight"],row["Gender"],row["DOB"],row["Age"],row["CID"],row["TID"])
		query1="INSERT INTO MEMBER_ADDRESS(MID,Street,Locality) VALUES('%s','%s','%s')" %(row["MID"],row["Street"],row["Locality"])
	
		cur.execute(query)
		con.commit()    
		cur.execute(query1)
		con.commit() 
		print("Member Added")

	except Exception as e:
		con.rollback()
		print("Failed to insert into database")
		print (">>>>>>>>>>>>>", e)   

def addtr():
	
	try:
		row={}
		print("Enter Trainer details: ")
		row["TID"] = input("TID: ")
		row["Fname"] = input("Fname: ")
		row["Mname"] = input("Mname: ")
		row["Lname"] = input("Lname: ")
		address =  input("Address(Street Locality): ")
		row["Street"] = address.split(" ")[0]
		row["Locality"] = address.split(" ")[1]
		row["Weight"] = int(input("Weight: "))
		row["Gender"] = input("Gender: ")
		row["Age"] = int(input("Age: "))
		row["Salary"] = int(input("Salary: "))
		row["Level"] = int(input("Level: "))

		query="INSERT INTO TRAINERS(TID,Fname,Mname,LName,Weight,Gender,Age,Salary,Level) VALUES('%s','%s','%s','%s','%d','%s','%d','%d','%d')" %(row["TID"],row["Fname"],row["Mname"],row["Lname"],row["Weight"],row["Gender"],row["Age"],row["Salary"],row["Level"])
		query1="INSERT INTO TRAINER_ADDRESS(TID,Street,Locality) VALUES('%s','%s','%s')" %(row["TID"],row["Street"],row["Locality"])
	
		cur.execute(query)
		con.commit()    
		cur.execute(query1)
		con.commit() 
		print("Trainer Added")

	except Exception as e:
		con.rollback()
		print("Failed to insert into database")
		print (">>>>>>>>>>>>>", e) 
		print(query)

def additem():
	
		row={}
		oid=int(input("Enter '1' for clothes,'2' for shoes,'3' for food: "))
		if(oid==1):
			row["PID"] = input("PID: ")
			row["Type1"] = input("Type of product: ")
			row["Cost"]= int(input("Cost: "))
			row["Size"] = input("Size: ")
			row["Type2"] = input("Type of clothes: ")
			query="INSERT INTO GYM_PRODUCTS(PID,Cost,Type) VALUES('%s','%d','%s')" %(row["PID"],row["Cost"],row["Type1"])
			query1="INSERT INTO CLOTHES(PID,Type,Size) VALUES('%s','%s','%s')" %(row["PID"],row["Type2"],row["Size"])

		elif(oid==2):
			row["PID"] = input("PID: ")
			row["Type1"] = input("Type of product: ")
			row["Cost"]= int(input("Cost: "))
			row["Size"] = input("Size: ")
			row["Brand"] = input("Brand: ")
			query="INSERT INTO GYM_PRODUCTS(PID,Cost,Type) VALUES('%s','%d','%s')" %(row["PID"],row["Cost"],row["Type1"])
			query1="INSERT INTO SHOES(PID,Size,Brand) VALUES('%s','%s','%s')" %(row["PID"],row["Size"],row["Brand"])

		elif(oid==3):
			row["PID"] = input("PID: ")
			row["Type1"] = input("Type of product: ")
			row["Cost"]= int(input("Cost: "))
			row["Brand"] = input("Brand: ")
			row["Calorie"] = input("Calorie: ")
			query="INSERT INTO GYM_PRODUCTS(PID,Cost,Type) VALUES('%s','%d','%s')" %(row["PID"],row["Cost"],row["Type1"])
			query1="INSERT INTO FOOD(PID,Brand,Calorie) VALUES('%s','%s','%s')" %(row["PID"],row["Brand"],row["Calorie"])

		try:
			cur.execute(query)
			con.commit()    
			cur.execute(query1)
			con.commit() 
			print("Item Added")

		except Exception as e:
			con.rollback()
			print("Failed to insert into database")
			print (">>>>>>>>>>>>>", e)   

def upwt():
	kid=int(input("Choose '1' for Member and '2' for Trainer: "))
	if(kid==1):
		mi=input("Enter Member Id: ")
		mw=int(input("Enter new wt: "))
		query="UPDATE MEMBERS SET Weight=%d where MID='%s'" %(mw,mi)
	else:
		ti=input("Enter Trainer Id: ")
		tw=int(input("Enter new wt: "))
		query="UPDATE TRAINERS SET Weight=%d where TID='%s'" %(tw,ti)

	try:
		cur.execute(query)
		con.commit()    
		print("Weight updated")

	except Exception as e:
		con.rollback()
		print("Failed to insert into database")
		print (">>>>>>>>>>>>>", e)   

def upfee():
	cid=input("Enter Course Id: ")
	fee=int(input("Enter new fees: "))
	query="UPDATE COURSE SET FEES=%d where CID='%s'" %(fee,cid)
	
	try:
		cur.execute(query)
		con.commit()    
		print("Fees updated")

	except Exception as e:
		con.rollback()
		print("Failed to insert into database")
		print (">>>>>>>>>>>>>", e)   

def upcost():
	pid=input("Enter product Id: ")
	cos=int(input("Enter new cost: "))
	query="UPDATE GYM_PRODUCTS SET COST=%d where PID='%s'" %(cos,pid)
	
	try:
		cur.execute(query)
		con.commit()    
		print("Cost updated")

	except Exception as e:
		con.rollback()
		print("Failed to insert into database")
		print (">>>>>>>>>>>>>", e)  

def delmem():
	delid=input("Enter Member Id to be deleted: ") 
	query="DELETE FROM MEMBERS where MID='%s'" %(delid)

	try:
		cur.execute(query)
		con.commit()    
		print("Member Deleted")

	except Exception as e:
		con.rollback()
		print("Failed to insert into database")
		print (">>>>>>>>>>>>>", e)  

def prog():
	mid=input("Enter Member Id: ")
	query="SELECT W.HOURS as HOURS,M.AVG_CAL_per_HR as AVG FROM WORKS_FOR as W,MACHINE as M WHERE W.MID='%s' and W.XID=M.XID" %(mid)
	try:
		cur.execute(query)
		con.commit()
		sum = 0;  
		for row in cur:
			sum+=int(row['HOURS'])*int(row['AVG'])
		print("Total Calories: ",sum)

	except Exception as e:
		con.rollback()
		print("Failed to insert into database")
		print (">>>>>>>>>>>>>", e)


def invoice():
	mid=input("Enter Member Id: ")
	query="SELECT P.PID as PID,P.Cost as Cost,P.Type as Type FROM BUYS as B,GYM_PRODUCTS as P where B.MID='%s' AND B.PID=P.PID" %(mid)
	try:
		cur.execute(query)
		con.commit()
		sum = 0; 
		print("PID","\t",'Type',"\t",'Cost')
		for row in cur:
			print(row["PID"],"\t",row['Type'],"\t",row['Cost'])
			sum+=int(row['Cost'])
		print("Total Cost: ",sum)

	except Exception as e:
		con.rollback()
		print("Failed to insert into database")
		print (">>>>>>>>>>>>>", e)  








def dispatch(ch):
	"""
	Function that maps helper functions to option entered
	"""

	if(ch==1): 
		addmem()
	elif(ch==2):
		addtr()
	elif(ch==3):
		additem()
	elif(ch==4):
		upwt()
	elif(ch==5):
		upfee()
	elif(ch==6):
		upcost()
	elif(ch==7):
		delmem()
	elif(ch==8):
		prog()
	elif(ch==9):
		invoice()
	else:
		print("Error: Invalid Option")

while(1):
	tmp = sp.call('clear',shell=True)
	username = input("Username: ")
	password = input("Password: ")

	try:
		con = pymysql.connect(host='localhost',
				user=username,
				password=password,
				db='GYM',
				cursorclass=pymysql.cursors.DictCursor)
		tmp = sp.call('clear',shell=True)

		if(con.open):
			print("Connected")
		else:
			print("Failed to connect")
		tmp = input("Enter any key to CONTINUE>")

		with con:
			cur = con.cursor()
			while(1):
				tmp = sp.call('clear',shell=True)
				print("1.ADD NEW MEMBER TO THE GYM");
				print("2.ADD NEW TRAINER TO THE GYM");
				print("3.ADD NEW ITEM TO INVENTORY");
				print("4.UPDATE WIEGHT OF TRAINER/MEMBER");
				print("5.UPDATE COURSE FEE");
				print("6.UPDATE ITEM COST");
				print("7.DELETE MEMBER");
				print("8.PROGRESS REPORT OF A MEMBER");
				print("9.INVOICE ON PURCHASE of all products BY a MEMBER");
				print("10.LOGOUT");
				ch = int(input("Enter choice> "))
				tmp = sp.call('clear',shell=True)
				if ch==10:
					print("Bye")
					break
				else:
					dispatch(ch)
					tmp = input("Enter any key to CONTINUE>")
			if(ch==10):
				break
	except:
		tmp = sp.call('clear',shell=True)
		print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
		tmp = input("Enter any key to CONTINUE>")
	
