from flask import Flask, render_template, url_for, flash, redirect, request, jsonify, make_response
from flask_cors import CORS
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = '831a771e9625df1f95574f071746fa49'

@app.route("/", methods=["POST", "GET"])
def home():
    return render_template('home.html', title="Home")

@app.route("/about")
def about():
    return render_template('about.html', title="About")


@app.route("/timetable")
def timetable():
    return render_template('about.html', title="About")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@innopolis.com" and form.password.data == "password":
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
