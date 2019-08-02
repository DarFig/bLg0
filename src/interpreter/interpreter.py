# -*- coding: utf-8 -*-

import os
import json

class Interpreter:

    def __init__(self, folder:str="src/_posts"):
        self._folder = folder

    def get_all_posts(self)->list:
        return os.listdir(self._folder)
        

    def get_content(self, file:str)->dict:
        with open(file, 'r') as content:
            return json.loads(content.read())[0]

