# -*- coding: utf-8 -*-
from src import app
from flask import render_template



@app.route('/about')
@app.route('/about', methods=['GET'])
def about():
    title = "BLG0"
    return render_template('_views/about.html',webTitle=title)