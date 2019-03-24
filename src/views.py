# -*- coding: utf-8 -*-
from src import app
from flask import render_template

@app.route('/')
@app.route('/', methods=['GET'])
def index():
    title = "BLG0"
    return render_template('_views/index.html',webTitle=title)