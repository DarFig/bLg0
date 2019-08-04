# -*- coding: utf-8 -*-

from src import app
from flask import render_template


@app.route('/post', methods=['GET'])
def post():
    title = "BLG0"
    return render_template('_views/post.html',webTitle=title)
