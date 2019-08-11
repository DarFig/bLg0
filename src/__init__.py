# -*- coding: utf-8 -*-

from flask import Flask


app = Flask(__name__)

#data_base_uri = ""
#app.config['SQLAlCHEMY_DATABASE_URI'] = data_base_uri
#app.config['SQLAlCHEMY_TRACK_MODIFICATIONS'] = True
#db = SQLAlchemy(app)

import src.views
