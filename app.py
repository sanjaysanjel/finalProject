from flask import Flask, render_template,url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'fa1883355361f2cd59551a148a4e10db'

posts = [
	{ 
		'author': 'Rick Bailey',
		'title': 'Impact of Blockchain in Nepalese Society',
		'content':'Blockchain is one of the fastest growing technology and with companies like Deerwalk and Logpoint sharing interest',
		'date_posted':'Feb 8, 2019'
	},

	{ 
		'author': 'Mogran Chained',
		'title': 'What is tomorrow ?',
		'content':'tomorrow is holiday. I prefer not to speak about it cause if I did, I would be in big trouble',
		'date_posted':'Feb 7, 2019'
	}

]

@app.route('/')
@app.route("/home")
def home_page():
   return render_template('home.html',posts=posts)


@app.route('/about')
def about():
   return render_template('about.html',title="About")



@app.route("/register")
def register():
	form = RegistrationForm()
	return render_template('register.html',title="Register",form=form)

@app.route("/login")
def login():
	form = LoginForm()
	return render_template('login.html',title="Login",form=form)


if __name__ == '__main__':
   app.run(debug=True)