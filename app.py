import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
import models as dbHandler

UPLOAD_FOLDER = 'D:\GIT\FlaskDB\static'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','JPG'])
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
	return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/login')
def login():
	print("Login Loaded")
	return render_template('index.html')

"""
@app.route('/OneSided', methods=['POST','GET'])
def makematch():
	print("OneSided");
	if request.method == 'POST':
"""

@app.route('/dashboard', methods=['POST', 'GET'])
def home():
	if request.method=='POST':
		username = request.form['username']
		password = request.form['password']
		count = dbHandler.checkUser(username,password)
		if count[0][0]>=1:
			print("USER EXISTS")			
			users = dbHandler.findGender(username)
			gender = users[0][0]
			data = dbHandler.retrieveUserDetails(gender)
			if username == "admin":
				return render_template('admin.html', users = data)
			return render_template('dashboard.html',users = data,currentlogin = username)
		else:
			print("USER DOESNT EXIST")
			return render_template('welcome.html')
	else:
		return render_template('index.html')


@app.route('/reg')
def reg():
	return render_template('welcome.html')

@app.route('/register', methods=['POST','GET'])
def register():
	print("REGISTER REACHED")
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		email = request.form['email']
		age = request.form['age']
		gender = request.form['gender']
		imagename = request.form['image1']
		description = request.form['descriptn']
		image = "/static/" + request.form['image1'].split("\\")[2]
		print(image)
		if 'image' not in request.files:
			print("No File Selected")
			return render_template('welcome.html')
		file = request.files['image']
		print(file)
		if file.filename == '':
			print("Koi File select nahi kiya")
			return render_template('welcome.html') 
		if file and allowed_file(file.filename):
			print("Selected")
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
		dbHandler.insertUserDetails(username,password,age,image,gender,email,description)
		return render_template('index.html')
	else:
		return render_template('welcome.html')

if __name__ == '__main__':
	app.run(debug=True)