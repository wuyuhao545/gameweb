from route import app
from flask import render_template,abort,redirect,url_for,flash,session

from forms.login_from import LoginFrom
from project.services.user_service import UserService

@app.route('/')

@app.route('/index.html')
def home_page():
    return render_template('index.html')

@app.route('/about.html')
def about_page():
    return render_template('about.html')


@app.route('/level1')
def level_1_page():
    return render_template('Smashbricks.html')

@app.route('/level2')
def level_2_page():
    return render_template('Flipthecards.html')

@app.route('/level3')
def level_3_page():
    return render_template('BallBattle.html')

@app.route('/level4')
def level_4_page():
    return render_template('jing.html')

@app.route('/login.html',methods=['GET','POST'])
def login_page():
    form = LoginFrom()
    if form.validate_on_submit():
        result = UserService().do_login(username=form.username.data,password=form.password.data)
        if result:
            flash(f'欢迎{form.username.data}回来',category='success')
            return redirect(url_for('home_page'))
        else:
            flash('用户名或密码错误，请重试!', category='danger')
    return render_template('login.html',form=form)

@app.route('/level_complete')
def level_complete():
    # This should be reached after completing the level
    session['level_completed'] = True  # Set the session flag
    return redirect(url_for('article.html'))  # Redirect to the index or main menu page