# -*- coding: utf-8 -*-

import os



# posts

def get_all_pk_posts()->list:
    return os.listdir(Configure.post_folder())
    

def get_all_posts(limit:int=0)->list:
    answer = []
    pks = get_all_pk_posts()
    for pk in pks:
        if "base" not in pk and "about" not in pk:
            answer.append(get_content_from_pk(pk))
            limit-=1
            if limit is 0:
                break
    return answer


def get_content_from_pk(pk:str)->dict:
    answer = {}
    with open(Configure.post_folder() + str(pk).replace('.json','')+".json", 'r') as content:
        answer = eval(content.read())
        return answer


# proy

def get_all_pk_proys()->list:
    return os.listdir(Configure.proy_folder())

def get_all_proy(limit:int=0)->list:
    answer = []
    pks = get_all_pk_proys()
    for pk in pks:
        if "base" not in pk:
            answer.append(get_proy_from_pk(pk))
            limit-=1
            if limit is 0:
                break
    return answer

def get_proy_from_pk(pk:str)->dict:
    answer = {}
    with open(Configure.proy_folder() + str(pk).replace('.json','')+".json", 'r') as content:
        answer = eval(content.read())
        return answer


class Configure:

    @staticmethod
    def post_folder():
        return "src/_posts/" 

    @staticmethod
    def proy_folder():
        return "src/_proy/"

    @staticmethod
    def header()->list:
        return ["title","tags", "references"]

    @staticmethod
    def body()->list:
        return ["intro", "body"]

    @staticmethod
    def footer()->list:
        return ["label"]


    