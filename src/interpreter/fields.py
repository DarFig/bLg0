# -*- coding: utf-8 -*-


class Fields:

    @staticmethod
    def header()->list:
        return ["title","tags", "references"]

    @staticmethod
    def body()->list:
        return ["intro", "body"]

    @staticmethod
    def footer()->list:
        return ["label"]

    