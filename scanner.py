import os
import shutil

from error_type import ErrorType


class PBScanner:
    def __init__(self, root_dir, scan_mode, dst_dir_path=None):
        self.root_dir = root_dir
        if self.root_dir[-1] != '/':
            self.root_dir += '/'

        if scan_mode == "copy":
            # 将root_dir内的pdf文件复制到dst_dir内
            if not os.path.exists(dst_dir_path):
                os.mkdir(dst_dir_path)
            if dst_dir_path[-1] != '/':
                dst_dir_path += '/'
            _files = os.listdir(self.root_dir)
            for _f in _files:
                _path = self.root_dir + _f
                if not os.path.isdir(_path) and _path.split('.')[-1] == "pdf":  # TODO 是否复制已经存在的文件夹？
                    shutil.copyfile(_path, dst_dir_path + _f)
            self.scan_dir = dst_dir_path
        else:
            self.scan_dir = self.root_dir

    def scan(self):
        scan_create_folders(self.scan_dir)


def scan_create_folders(scan_dir):
    """
    用于扫描文件夹并对每个pdf创建对应文件夹和md文件
    :param scan_dir:
    :return:
    """
    files = os.listdir(scan_dir)
    for f in files:
        postfix = f.split('.')[-1]
        name = f[:len(postfix) + 1]
        sub_dir_path = scan_dir + name + '/'
        if not os.path.exists(sub_dir_path):
            # 将pdf文件移动至同名文件夹，如果已经存在同名文件夹，则不创建md文件
            os.mkdir(sub_dir_path)
            os.mknod(sub_dir_path + name + ".md")  # 创建md文件
        shutil.move(scan_dir + f, sub_dir_path + f)

    return True


def scan_dir_file(dir_root):
    """
    递归地扫描文件夹下文件，返回dict形式的树状结构
    :param dir_root:
    :return:
    """
    if not os.path.exists(dir_root):
        return None
    ret = dict()
    if not os.path.isdir(dir_root):  # 如果路径非文件夹，则返回{当前文件名:当前文件路径}
        name = dir_root.split('/')[-1]
        ret[name] = dir_root
        return ret

    if dir_root[-1] != '/':
        dir_root += '/'
    root_name = dir_root.split('/')[-2]
    files = os.listdir(dir_root)
    cur_list = []
    for f in files:
        f_path = dir_root + f
        if os.path.isdir(f_path):
            f_path += '/'
        cur_list.append(scan_dir_file(f_path))
    # TODO sort?
    ret[root_name] = cur_list

    return ret


class DocList:
    def __init__(self, root_dir):
        self.root_dir = root_dir
        self.docs = scan_dir_file(self.root_dir)  # 如果 self.root_dir不存在则 self.docs=None



def scan(root_dir, scan_mode, dst_dir_path=None):
    if not os.path.exists(root_dir):
        return ErrorType(101)  # "Root dir path does not exist."
    if scan_mode not in ["inplace", "copy"]:
        return ErrorType(102)  # "Scan mode is invalid."

    scanner = PBScanner(root_dir, scan_mode, dst_dir_path)


if __name__ == "__main__":
    dir_root = "/Users/yunhangwang/Desktop/projs/PaperBox/test_dir"
    ret = scan_dir_file(dir_root)
    print(ret)
