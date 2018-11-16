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

	cur.execute("CREATE TABLE student_details(SId integer primary key autoincrement default 1001, Name varchar(30),USN varchar(10) unique,Branch char(5),Semester integer,Section char,Mobile_no bigint(10),Email_id varchar(40),Password varchar(20),Login_set char default 'S');")
	cur.execute("INSERT INTO student_details (Name,USN,Branch,Semester,Section,Mobile_no,Email_id,Password) values('Anish R A','4NI16CS001','CSE',5,'A',9012345678,'anishra123@gmail.com','anish123');")
	cur.execute("INSERT INTO student_details (Name,USN,Branch,Semester,Section,Mobile_no,Email_id,Password) values('Vijith K','4NI16ME003','MECH',5,'M',9123456780,'vijithk123@gmail.com','vijith123');")


	cur.execute("CREATE TABLE teacher_details(TId integer primary key autoincrement default 2001,TName varchar(30),ID_no varchar(11) unique,Department varchar(30),TMobile_no bigint(10),TEmail_id varchar(40),TPassword varchar(20),Login_set char default 'T');")
	cur.execute("INSERT INTO teacher_details (TName,ID_no,Department,TMobile_no,TEmail_id,TPassword) values('Satya Nadella','5NI2001CS01','CSE',8012345679,'satyanadela123@gmail.com','satya123');")
	cur.execute("INSERT INTO teacher_details (TName,ID_no,Department,TMobile_no,TEmail_id,TPassword) values('Sundar Pichai','5NI1998CS03','CSE',8123456790,'sundarpichai123@gmail.com','sundar123');")


	conn.commit()
	conn.close()

#Insertion Queries
##Student Table
def insert_student_details(Name,USN,Branch,Semester,Section,Mobile_no,Email_id,Password):
	conn,cur = connect()
	cur.execute("INSERT INTO student_details (Name,USN,Branch,Semester,Section,Mobile_no,Email_id,Password) values(?, ?, ?, ?, ?, ?, ?,?);", [Name,USN,Branch,Semester,Section,Mobile_no,Email_id,Password])
	conn.commit()
	conn.close()

##Teacher Table
def insert_teacher_details(TName,ID_no,Department,TMobile_no,TEmail_id,TPassword):
	conn,cur = connect()
	cur.execute("INSERT INTO teacher_details (TName,ID_no,Department,TMobile_no,TEmail_id,TPassword) values(?,?,?,?,?,?);",[TName,ID_no,Department,TMobile_no,TEmail_id,TPassword])
	conn.commit()
	conn.close()