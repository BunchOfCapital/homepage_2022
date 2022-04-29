from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():

	user = {
	'username': 'joj'
	}

	items = [
		{
			'author' : {'username': 'yourmum'},
			'quote' : 'suffering is key'
		},
		{
			'author' : {'username': 'god'},
			'quote' : 'get fucked lmao'
		}
	]
	return render_template('index.html', user=user, title="ah, sweet fervor", items=items)

