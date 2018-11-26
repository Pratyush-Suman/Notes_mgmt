import sqlite3

def connect():
	conn = sqlite3.connect("./proDB2.db")
	cur = conn.cursor()
	return conn,cur

#Creating tables
def creation():
	conn,cur = connect()
	
	cur.execute("DROP TABLE IF EXISTS student_details;")
	cur.execute("DROP TABLE IF EXISTS teacher_details;")
	cur.execute("DROP TABLE IF EXISTS student_notes;")
	cur.execute("DROP TABLE IF EXISTS uploaded_notes;")
	cur.execute("DROP VIEW IF EXISTS uplnotelist;")
	cur.execute("DROP TRIGGER IF EXISTS date_time;")

	cur.execute("CREATE TABLE student_details(SId integer primary key autoincrement default 1001, Name varchar(30),USN varchar(10) unique,Branch char(5),sem integer,section char,Mobile_Number bigint(10),Email_id varchar(40),passwd varchar(20),Login_set char default 'S');")
	cur.execute("INSERT INTO student_details (Name,USN,Branch,sem,section,Mobile_Number,Email_id,passwd) values('Anish R A','4NI16CS001','CSE',5,'A',9012345678,'anishra123@gmail.com','anish123');")
	cur.execute("INSERT INTO student_details (Name,USN,Branch,sem,section,Mobile_Number,Email_id,passwd) values('Vijith K','4NI16ME003','CSE',5,'B',9123456780,'vijithk123@gmail.com','vijith123');")
	cur.execute("INSERT INTO student_details (Name,USN,Branch,sem,section,Mobile_Number,Email_id,passwd) values('','4NI16','',,'',,'123@gmail.com','123');")
	cur.execute("INSERT INTO student_details (Name,USN,Branch,sem,section,Mobile_Number,Email_id,passwd) values('','4NI16','',,'',,'123@gmail.com','123');")


	cur.execute("CREATE TABLE teacher_details(TId integer primary key autoincrement default 2001,Tname varchar(30),ID_no varchar(11) unique,dept varchar(30),TMobile_Number bigint(10),TEmail_Id varchar(40),tpwd varchar(20),Login_set char default 'T');")
	cur.execute("INSERT INTO teacher_details (Tname,ID_no,dept,TMobile_Number,TEmail_Id,tpwd) values('Satya Nadella','5NI2001CS01','CSE',8012345679,'satyanadela123@gmail.com','satya123');")
	cur.execute("INSERT INTO teacher_details (Tname,ID_no,dept,TMobile_Number,TEmail_Id,tpwd) values('Sundar Pichai','5NI1998CS03','CSE',8123456790,'sundarpichai123@gmail.com','sundar123');")

	cur.execute("CREATE TABLE student_notes(NId integer primary key autoincrement default 3001, SId integer, Subject varchar(30), Title varchar(30), Notes text ,FOREIGN KEY (SId) REFERENCES student_details(SId));")
	cur.execute("INSERT INTO student_notes (SId,Subject,Title,Notes) values(1,'Operating System','Deadlocks','four conditions must hold for there to be a (resource) deadlock: 1. Mutual exclusion condition. 2. Hold-and-wait condition. 3.No-preemption condition. 4.Circular wait condition.');")
	cur.execute("INSERT INTO student_notes (SId,Subject,Title,Notes) values(2,'TM','BLAHBLAHBLAHBLAH','BLAHBLAHBLAHBLAHBLAHBLAHBLAHBLAHBLAHBLAHBLAHBLAHBLAH');")
 
	cur.execute("CREATE TABLE uploaded_notes(UNId integer primary key autoincrement default 4001, TId integer , Subject varchar(30), Title varchar(30), Notes text, Branch char(5), sem integer, section char, Uploaded_On datetime,FOREIGN KEY (TId) REFERENCES teacher_details(TId));")
	cur.execute("INSERT INTO uploaded_notes (TId,Subject,Title,Notes,Branch,sem,section) values(1,'DCN','WiMAX','Fixed and Mobile Services','CSE',5,'A');")
	cur.execute("INSERT INTO uploaded_notes (TId,Subject,Title,Notes,Branch,sem,section) values(2,'SS','Assembler Directives','RESW BYTE WORD RESW','CSE',5,'B');")

	cur.execute("CREATE VIEW uplnotelist AS SELECT T.Tname,U.Subject,U.Title,U.Notes,U.Branch,U.sem,U.section,U.Uploaded_On from teacher_details T, uploaded_notes U where T.TId=U.TId;")

	cur.execute('''CREATE TRIGGER date_time AFTER INSERT ON uploaded_notes  
					FOR EACH ROW 
					BEGIN
					  UPDATE uploaded_notes set Uploaded_On = datetime('now','localtime') where UNId = new.UNId;
					END;''')


	conn.commit()
	conn.close()

#Insertion Queries
##Student Table
def insert_student_details(Name,USN,Branch,sem,section,Mobile_Number,Email_Id,passwd):
	conn,cur = connect()
	
	cur.execute("SELECT * FROM student_details where USN = ?;",(USN,))
	data = cur.fetchall()

	if(data):
		conn.close()
		return 0

	else:
		cur.execute("INSERT INTO student_details (Name,USN,Branch,sem,section,Mobile_Number,Email_id,passwd) values(?, ?, ?, ?, ?, ?, ?,?);", [Name,USN,Branch,sem,section,Mobile_Number,Email_Id,passwd])
		conn.commit()
		conn.close()
		return 1

##Teacher Table
def insert_teacher_details(Tname,ID_no,dept,TMobile_Number,TEmail_Id,tpwd):
	conn,cur = connect()

	cur.execute("SELECT * FROM teacher_details where ID_no = ?;",(ID_no,))
	data = cur.fetchall()

	if(data):
		conn.close()
		return 0

	else:
		cur.execute("INSERT INTO teacher_details (Tname,ID_no,dept,TMobile_Number,TEmail_Id,tpwd) values(?,?,?,?,?,?);",[Tname,ID_no,dept,TMobile_Number,TEmail_Id,tpwd])
		conn.commit()
		conn.close()

#Determine user type and return the respective home page after login

def verify_user(username,password):
	
	conn,cur = connect()

	cur.execute("SELECT * FROM student_details WHERE USN = ? AND passwd = ?;",(username,password))

	data = cur.fetchall()

	if(data):
		conn.close()
		return 'S',data

	else:
		cur.execute("SELECT * FROM teacher_details WHERE ID_no = ? AND tpwd = ?;",(username,password))

		data = cur.fetchall()

		if(data):
			conn.close()
			return 'T',data

		else:
			conn.close()
			return 0,None


def upd_pro_stu(USN,Mobile_Number,Email_Id,passwd):
	conn,cur = connect()

	cur.execute("UPDATE student_details SET Mobile_Number = ?,Email_id = ?,passwd = ? WHERE USN = ?;",(Mobile_Number,Email_Id,passwd,USN))
	
	conn.commit()
	conn.close()

#Student Add Notes
def insert_note(stu_ID,Subject,title,stu_note):
	conn,cur = connect()

	cur.execute("INSERT INTO student_notes (SId,Subject,Title,Notes) values(?,?,?,?);",[stu_ID,Subject,title,stu_note])

	conn.commit()
	conn.close()

##Student's Personal Notes List
def Spernote(SId):

	conn,cur = connect()

	cur.execute("SELECT * from student_notes WHERE SId=?;",[SId])

	Stuuplnote = cur.fetchall()

	conn.close()

	return Stuuplnote


##Uploaded notes by teacher in student account
def Suplnote(Branch,sem,section):

	conn,cur = connect()

	cur.execute("SELECT Tname,Subject,Title,Notes,Uploaded_On FROM uplnotelist WHERE Branch = ? AND sem = ? AND section = ?;",[Branch,sem,section])

	Supnote = cur.fetchall()

	conn.close()

	return Supnote


##Teacher Profile Update
def upd_pro_tea(ID_no,TMobile_Number,TEmail_Id,tpwd):
	conn,cur = connect()

	cur.execute("UPDATE teacher_details SET TMobile_Number = ?,TEmail_id = ?,tpwd = ? WHERE ID_no = ?;",(TMobile_Number,TEmail_Id,tpwd,ID_no))
	
	conn.commit()
	conn.close()

##Teacher to upload note
def tea_upl_note(TId,Subject,Title,Notes,Branch,sem,section):
	conn,cur = connect()

	cur.execute("INSERT INTO  uploaded_notes (TId,Subject,Title,Notes,Branch,sem,section) values(?,?,?,?,?,?,?);", [TId,Subject,Title,Notes,Branch,sem,section])

	conn.commit()
	conn.close()

##List of uploaded notes by teacher in his account
def Tuploaded_notes(TId):

	conn,cur = connect()

	cur.execute("SELECT * from uploaded_notes WHERE TId=?;",[TId])

	Teauplnote = cur.fetchall()

	conn.close()
	return Teauplnote