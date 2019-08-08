# -*- coding: utf-8 -*-
from src import app
from flask import render_template

from ..interpreter import get_content_from_pk


@app.route('/about', methods=['GET'])
def about():
    title = "BLG0"
    about = get_content_from_pk("about")
    return render_template('_views/about.html',webTitle=title, about=about)