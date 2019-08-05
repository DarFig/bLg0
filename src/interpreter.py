# -*- coding: utf-8 -*-

import os
#import json


def get_all_pk_posts()->list:
    return os.listdir(Configure.folder())
    

def get_all_posts()->list:
    answer = []
    pks = get_all_pk_posts()
    for pk in pks:
        answer.append(get_content_from_pk(pk))
    return answer


def get_content_from_pk(pk:str)->dict:
    answer = {}
    with open(Configure.folder() + str(pk).replace('.json','')+".json", 'r') as content:
        answer = eval(content.read())
        return answer


class Configure:

    @staticmethod
    def folder():
        return "src/_posts/" 


    @staticmethod
    def header()->list:
        return ["title","tags", "references"]

    @staticmethod
    def body()->list:
        return ["intro", "body"]

    @staticmethod
    def footer()->list:
        return ["label"]


    