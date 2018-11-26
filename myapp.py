from flask import Flask, render_template,request
from db_queries import *

app = Flask(__name__)

user_info = None
user_info1 = []
tnote = None

creation()

@app.route('/', methods = ['GET','POST'])
def landing_page():
	return render_template('first.html')

@app.route('/first.html', methods = ['GET','POST'])
def home_page():
	global user_info ,user_info1
	user_info = None
	user_info1 = []
	return render_template('first.html')

@app.route('/about.html', methods = ['GET','POST'])
def about_page():
	return render_template('about.html')

@app.route('/student2.html', methods = ['GET','POST'])
def student_signup():
	return render_template('student2.html')

@app.route('/teacher2.html', methods = ['GET','POST'])
def teacher_signup():
	return render_template('teacher2.html')

@app.route("/verify_student", methods = ['POST'])
def register_student():
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
def register_teacher():
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


@app.route('/login2.html', methods = ['GET','POST'])
def login_page():
	return render_template('login2.html')

@app.route("/verify_login", methods = ['POST'])
def verify_login():

	global user_info ,user_info1

	if request.method == 'POST':

		username = request.form['username']
		password = request.form['password']

		flag,data  = verify_user(username,password)

		if flag == 0:
			return render_template('login2.html', message = 'WRONG USERNAME OR PASSWORD!!!')

		elif flag == 'S':
			user_info = data
			 
			for i in user_info[0]:
				user_info1.append(i)

			return render_template('stu_home.html', Name = user_info1[1] )

		elif flag == 'T':
			user_info = data
			 
			for i in user_info[0]:
				user_info1.append(i)

			return render_template('tea_home.html', Name = user_info1[1] )

@app.route('/stu_home.html',methods = ['GET','POST'])
def student_homepage():
	global user_info
	return render_template('stu_home.html', Name = user_info1[1])

@app.route('/stu_profile.html',methods = ['GET','POST'])
def student_profilepage():
	return render_template('stu_profile.html', user_info1 = user_info1)

@app.route('/stu_pro_upd.html',methods = ['GET','POST'])
def student_proupdpage():
	return render_template('stu_pro_upd.html')

@app.route('/stu_notes_list.html',methods = ['GET','POST'])
def student_notelistpage():

	snote = Spernote(user_info1[0])

	return render_template('stu_notes_list.html', snote = snote)

@app.route('/stu_add_note.html',methods = ['GET','POST'])
def student_addnotepage():
	return render_template('stu_add_note.html', user_info1 = user_info1)

@app.route('/upl_notes_list.html',methods = ['GET','POST'])
def student_uplnotelist():

	tsnote = Suplnote(user_info1[3],user_info1[4],user_info1[5])

	return render_template('upl_notes_list.html', tsnote = tsnote)


##Student Profile Update
@app.route('/profile_updated', methods = ['POST'])
def profile_updated():
	if request.method == 'POST':

		Mobile_Number = request.form['Mobile_Number']
		if Mobile_Number == "":
			Mobile_Number = user_info1[6]
		Email_Id = request.form['Email_Id']
		if Email_Id == "":
			Email_Id = user_info1[7]
		passwd = request.form['passwd']
		if passwd == "":
			passwd = user_info1[8]

		upd_pro_stu(user_info1[2],Mobile_Number,Email_Id,passwd)
		
		user_info1[6] = Mobile_Number
		user_info1[7] = Email_Id
		user_info1[8] = passwd

		return render_template('stu_profile.html', user_info1 = user_info1)

##Student Adding notes
@app.route('/add_note', methods = ['POST'])
def add_note():
	
	Subject = request.form['Subject']
	title = request.form['title']
	stu_note = request.form['stu_note']

	insert_note(user_info1[0],Subject,title,stu_note) 

	return student_notelistpage()



@app.route('/tea_home.html',methods = ['GET','POST'])
def teacher_homepage():
	return render_template('tea_home.html', Name = user_info1[1])

@app.route('/tea_profile.html',methods = ['GET','POST'])
def teacher_profilepage():
	return render_template('tea_profile.html', user_info1 = user_info1)

@app.route('/tea_pro_upd.html',methods = ['GET','POST'])
def teacher_proupdpage():
	return render_template('tea_pro_upd.html')

@app.route('/tea_notes_list.html',methods = ['GET','POST'])
def teacher_notelistpage():

	tnote = Tuploaded_notes(user_info1[0])
	
	return render_template('tea_notes_list.html', tnote = tnote)

@app.route('/tea_upl_note.html',methods = ['GET','POST'])
def teacher_uplnotepage():
	return render_template('tea_upl_note.html', user_info1 = user_info1)

@app.route('/Tprofile_updated', methods = ['POST'])
def Tprofile_updated():
	if request.method == 'POST':

		TMobile_Number = request.form['TMobile_Number']
		if TMobile_Number == "":
			TMobile_Number = user_info1[4]
		TEmail_Id = request.form['TEmail_Id']
		if TEmail_Id == "":
			TEmail_Id = user_info1[5]
		tpwd = request.form['tpwd']
		if tpwd == "":
			tpwd = user_info1[6]

		upd_pro_tea(user_info1[2],TMobile_Number,TEmail_Id,tpwd)
		
		user_info1[4] = TMobile_Number
		user_info1[5] = TEmail_Id
		user_info1[6] = tpwd

		return render_template('tea_profile.html', user_info1 = user_info1)

@app.route('/Note_uploaded', methods = ['POST'])
def Note_uploaded():
	if request.method == 'POST':

		Subject = request.form["Subject"]
		Title = request.form["Title"]
		Notes = request.form["Notes"]
		Branch = request.form["Branch"]
		sem = request.form["sem"]
		section = request.form["section"]

		tea_upl_note(user_info1[0],Subject,Title,Notes,Branch,sem,section)

		return teacher_notelistpage()









if __name__ == '__main__':
	app.run(debug=True)