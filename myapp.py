from flask import Flask, render_template,request
from db_queries import *

app = Flask(__name__)

creation()

@app.route('/', methods = ['GET','POST'])
def landing_page():
	return render_template('first.html')

@app.route('/student2.html', methods = ['GET','POST'])
def student_signup():
	return render_template('student2.html')

@app.route('/teacher2.html', methods = ['GET','POST'])
def teacher_signup():
	return render_template('teacher2.html')

@app.route('/login2.html', methods = ['GET','POST'])
def login_page():
	return render_template('login2.html')

@app.route("/verify_student", methods = ['POST'])
def verify_student_info():
	name = request.form['Name']
	usn = request.form['USN']
	branch = request.form['Branch']
	sem = request.form['sem']
	sec = request.form['section']
	email = request.form['Email_Id']
	mobile = request.form['Mobile_Number']
	pwrd = request.form['passwd']

	insert_student_details(name,usn,branch,sem,sec,mobile,email,pwrd) 

	return render_template('first.html')

@app.route("/verify_teacher", methods = ['POST'])
def verify_teacher_info():
	tname = request.form['TName']
	tid = request.form['TId']
	dept = request.form['dept']
	temail = request.form['TEmail_Id']
	tmobile = request.form['TMobile_Number']
	tpwd = request.form['tpwd']

	insert_teacher_details(tname,tid,dept,tmobile,temail,tpwd)

	return render_template('first.html')

if __name__ == '__main__':
	app.run(debug=True)