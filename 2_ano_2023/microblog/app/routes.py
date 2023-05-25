from flask import render_template
from app import app

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
