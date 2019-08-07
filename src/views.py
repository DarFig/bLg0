# -*- coding: utf-8 -*-
from src import app
from flask import render_template


from .controladores.blog import *
from .controladores.about import *
from .controladores.post import *


from .interpreter import get_all_proy, get_all_posts

@app.route('/')
@app.route('/', methods=['GET'])
def index():
    title = "BLG0"
    proys = get_all_proy(limit=3)
    posts = get_all_posts(limit=3)
    return render_template('_views/index.html',webTitle=title, proys=proys, posts=posts)




