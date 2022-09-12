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
        self.item_list = dict()

    def add_item(self, doc_item: PBDocItem):
        if not isinstance(doc_item, PBDocItem):
            return ErrorType(401)  # Invalid item type.

    def del_item(self, k):
        if k not in self.item_list:
            return ErrorType(405)  # Key error: not exist.
        self.item_list.pop(k)
        return True

    def revise_item(self, k, revised_item):
        """
        修改item（先删除再添加）
        :param k:
        :param revised_item:
        :return:
        """
        if k not in self.item_list:
            return ErrorType(405)  # Key error: not exist.
        if not isinstance(revised_item, PBDocItem):
            return ErrorType(401)  # Invalid item type.
        self.item_list[k] = revised_item
        return True

    def resume_from_file(self, json_resume_path):
        """
        从json文件反序列化
        :param json_resume_path:
        :return:
        """
        if not os.path.exists(json_resume_path):
            pass  # TODO
        with open(json_resume_path, 'rb', encoding="utf-8") as f:
            list_dict = json.load(f)
        ks = list_dict.keys()
        ks.sort()
        for k in ks:
            data = list_dict[k]
            _item = PBDocItem()
            _item.resume(data)
            k = int(k)
            self.item_list[k] = _item

        return True

    def serialize(self, json_save_path):
        """
        序列化到json文件
        :param json_save_path:
        :return:
        """
        data_dict = dict()
        for k in self.item_list.keys():
            data_dict[k] = self.item_list[k].serialize()

        with open(json_save_path, 'w', encoding="utf-8") as f:
            json.dump(data_dict, f, ensure_ascii=False)

        return True
