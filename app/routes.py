from flask import render_template
from app import app

#Decoraters
@app.route('/')
@app.route('/index')
#view Function
def index():
    user = {'username': 'Javaughn'}
    posts = [
            {'author': {"username": 'John'}, 'body': 'Beautiful Day in New York'},
            {'author': {'username': 'Jim'}, 'body': 'The avengers are so cool'}]
    return render_template('index.html',title='Home',user=user, posts=posts)