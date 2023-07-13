from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    return render_template('login.html',boolean=True)

@auth.route('/logout')
def logout():
    return '<h1>Logout</h1>'

@auth.route('sign-up',methods=['GET','POST'])
def sing_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater more than 4 character', category='error')
        elif len(first_name) < 2:
            flash('Name must be greater than 1 character!', category='error')
        elif password1 != password2:
            flash('Password dont\'t match!', category='error')
        elif len(password1) < 7:
            flash('Password must be greater than 7 character!', category='error')
        else:
            flash('Create new user successfully!', category='success')
            


    return render_template('sign_up.html')