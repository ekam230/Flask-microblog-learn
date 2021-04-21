# -*- coding: utf-8 -*-
from flask import render_template
from flask_migrate import current
from requests.api import post
from app import app
from flask import request
from app.models import User, Post
from datetime import datetime

@app.route('/')
@app.route('/index')
def index():
    page = request.args.get('page', 1, type=int)
    # current_user= User.query.get(1)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(
        page, app.config['POSTS_PER_PAGE'], False)
    def dt():
        return datetime.today().year
    return render_template('index.html', title='Home', 
                           posts=posts.items, dt=dt) # datetime=datetime.today().year