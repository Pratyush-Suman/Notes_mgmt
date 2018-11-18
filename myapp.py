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
	Name = request.form['Name']
	USN = request.form['USN']
	Branch = request.form['Branch']
	sem = request.form['sem']
	section = request.form['section']
	Email_Id = request.form['Email_Id']
	Mobile_Number = request.form['Mobile_Number']
	passwd = request.form['passwd']

	flag = insert_student_details(Name,USN,Branch,sem,section,Mobile_Number,Email_Id,passwd) 

	if flag == 0:
		return render_template('student2.html', message = 'USN IS ALREADY REGISTERED!!')

	elif flag == 1:
		return render_template('first.html')

@app.route("/verify_teacher", methods = ['POST'])
def verify_teacher_info():
	Tname = request.form['TName']
	ID_no = request.form['ID_no']
	dept = request.form['dept']
	TEmail_Id = request.form['TEmail_Id']
	TMobile_Number = request.form['TMobile_Number']
	tpwd = request.form['tpwd']

	flag = insert_teacher_details(Tname,ID_no,dept,TMobile_Number,TEmail_Id,tpwd)

	if flag == 0:
		return render_template('teacher2.html', message = 'ID_no IS ALREADY REGISTERED!!')

	elif flag == 1:
		return render_template('first.html')

if __name__ == '__main__':
	app.run(debug=True)