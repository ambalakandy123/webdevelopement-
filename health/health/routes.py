from flask import render_template, url_for, flash, redirect
from health import app, db, bcrypt
from health.forms import RegistrationForm, LoginForm
from health.models import User, Post

posts = [    {
        'author':'Ranjith ak',
        'title':'advice consultant',
        'content':'first post',
        'date_posted':'july 1,2020'
    },
    {
        'author':'priya ak',
        'title':'advice consultant',
        'content':'second post',
        'date_posted':'july 3,2020'
    }
]
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title= 'Register', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@health.com' and form.password.data == 'password':
             flash('You have been logged in', 'success')
             return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check username or password', 'danger')
    return render_template('login.html', title='Login', form=form)