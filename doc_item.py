import os
from error_type import ErrorType


class PBDocItem:
    def __init__(self):
        self.name = None
        self.file_path = None
        self.review = None
        self.url_path = None

    def create_new(self, name, file_path="", url_path="", review=""):
        if not name:
            return ErrorType(201)  # Doc item's name should not be empty or null.
        self.name = name
        self.file_path = file_path
        self.url_path = url_path
        self.review = review
        return True

    def add_review(self, review):
        self.review = review
        return True

    def resume(self, data_dict):
        self.name = data_dict["name"]
        self.file_path = data_dict["file_path"]
        self.url_path = data_dict["url_path"]
        self.review = data_dict["review"]
        return True

    def serialize(self):
        data_dict = dict()
        data_dict["name"] = self.name
        data_dict["file_path"] = self.file_path
        data_dict["url_path"] = self.url_path
        data_dict["review"] = self.review
        return data_dict
