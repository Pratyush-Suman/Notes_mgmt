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

	cur.execute("CREATE TABLE student_details(SId integer primary key autoincrement default 1001, Name varchar(30),USN varchar(10) unique,Branch char(5),sem integer,section char,Mobile_Number bigint(10),Email_id varchar(40),passwd varchar(20),Login_set char default 'S');")
	cur.execute("INSERT INTO student_details (Name,USN,Branch,sem,section,Mobile_Number,Email_Id,passwd) values('Anish R A','4NI16CS001','CSE',5,'A',9012345678,'anishra123@gmail.com','anish123');")
	cur.execute("INSERT INTO student_details (Name,USN,Branch,sem,section,Mobile_Number,Email_Id,passwd) values('Vijith K','4NI16ME003','MECH',5,'M',9123456780,'vijithk123@gmail.com','vijith123');")


	cur.execute("CREATE TABLE teacher_details(TId integer primary key autoincrement default 2001,Tname varchar(30),ID_no varchar(11) unique,dept varchar(30),TMobile_Number bigint(10),TEmail_Id varchar(40),tpwd varchar(20),Login_set char default 'T');")
	cur.execute("INSERT INTO teacher_details (Tname,ID_no,dept,TMobile_Number,TEmail_Id,tpwd) values('Satya Nadella','5NI2001CS01','CSE',8012345679,'satyanadela123@gmail.com','satya123');")
	cur.execute("INSERT INTO teacher_details (Tname,ID_no,dept,TMobile_Number,TEmail_Id,tpwd) values('Sundar Pichai','5NI1998CS03','CSE',8123456790,'sundarpichai123@gmail.com','sundar123');")


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
		cur.execute("INSERT INTO student_details (Name,USN,Branch,sem,section,Mobile_Number,Email_Id,passwd) values(?, ?, ?, ?, ?, ?, ?,?);", [Name,USN,Branch,sem,section,Mobile_Number,Email_Id,passwd])
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