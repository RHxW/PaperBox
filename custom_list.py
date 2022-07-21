import os
import json

from doc_item import PBDocItem
from error_type import ErrorType


class CustomList:
    """
    自定义列表
    此处有两种类型的列表：
    1. 只有标题和对应短评
    2. 在包含标题和对应短评的基础上还有原文件和文档文件  TODO
    """
    def __init__(self):
        self.clist = dict()

    def add_item(self, doc_item: PBDocItem):
        if not isinstance(doc_item, PBDocItem):
            return ErrorType(401)  # Invalid item type.
        pass

    def serialize(self, des_path):
        pass

    def deserualize(self, file_path):
        pass
