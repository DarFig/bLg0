# -*- coding: utf-8 -*-
from src import app
from flask import render_template



@app.route('/blog')
@app.route('/blog', methods=['GET'])
def blog():
    title = "BLG0"
    return render_template('_views/blog.html',webTitle=title)