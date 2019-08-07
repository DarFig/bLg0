# -*- coding: utf-8 -*-
from src import app
from flask import render_template


from ..interpreter import get_all_posts


@app.route('/blog')
@app.route('/blog', methods=['GET'])
def blog():
    title = "BLG0"
    posts = get_all_posts(limit=0)
    return render_template('_views/blog.html',webTitle=title, posts=posts)