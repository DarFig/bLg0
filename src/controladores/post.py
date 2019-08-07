# -*- coding: utf-8 -*-

from src import app
from flask import render_template
from ..interpreter import get_content_from_pk


@app.route('/post', methods=['GET'])
@app.route('/post/<int:pk>', methods=['GET'])
def post(pk):
    title = "BLG0"
    post = get_content_from_pk(pk)
    return render_template('_views/post.html',webTitle=title, post=post)
