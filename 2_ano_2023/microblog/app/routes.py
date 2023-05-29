from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	user = {'username' : 'Gilberto Gil'}
	posts = [
{
	'author' : {'username' : 'Guilherme'},
	'body' : 'Nossa, adoro a aula de TI!'
},
{
	'author' : {'username' : 'Gabi'},
	'body' : 'Tem dia que parece noite...'	
}
	]
	return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requisitado para usuário {}, remember_me = {}'.format(form.username.data, form.remember_me.data))
		return redirect(url_for('index'))


	return render_template('login.html', title='Login', form = form)
