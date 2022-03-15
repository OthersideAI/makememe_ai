import secrets, os
from PIL import Image
from flask import render_template, flash, redirect, url_for, request
from makememe import app, db, bcrypt
from makememe.forms import RegistrationForm, LoginForm, UpdateAccountForm
from makememe.models import Users, Post, Meme, Feedback
from makememe.make import make
from flask_login import login_user, current_user, logout_user, login_required




@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    if current_user.is_authenticated: 
        user = Users.query.filter_by(id=current_user.id).first()
        authenticated = True
        is_beta = user.is_beta
        if request.method == 'POST': 
            description = request.form['description']
            meme = make(description, current_user.id)
        else:
            meme = {
                'meme': 'default.png',
            }
    else:
        is_beta = False
        authenticated = False
        meme = {
            'meme': 'default.png',
        }
    image_file = url_for('static', filename=meme['meme'])
    
    return render_template('home.html', image_file=image_file, authenticated=authenticated)


@app.route('/make',  methods=['GET', 'POST'])
def make():
    return { "meme": "https://makememe.ai/static/default.png" }
