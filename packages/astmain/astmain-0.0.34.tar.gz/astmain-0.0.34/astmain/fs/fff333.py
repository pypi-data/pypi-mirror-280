import json
import shutil, os, pathlib
from astmain.fs.read import read

from types import SimpleNamespace
from collections import namedtuple


class DotDict(dict):
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__

    def __call__(self, my_func_name, *args, **kwargs):
        print("my_func_name            :", my_func_name)
        result = self.__getitem__(my_func_name)(*args, **kwargs)

        return result


def func111():
    print("ctx            :", 111)


fff333 = DotDict({
    "aaa": 111,
    "read": read,
    "func111": func111
})
# python 帮我把代码   fff333.read().func111() 调用
# python 帮我把  data 转成  可以用  data.func111调用  也可以用 data["func111"]调用


if __name__ == '__main__':
    res1 = fff333.read(r"E:\AAA\xxx\ast_chrome\a08_驱动测试_cookie_打包_发布\astmain_py222\astmain\fs\aaa.txt")
    res2 = fff333["read"](r"E:\AAA\xxx\ast_chrome\a08_驱动测试_cookie_打包_发布\astmain_py222\astmain\fs\aaa.txt").func111()
    print("res1            :", res1)
    print("res2            :", res2)

    # res1 = fff333["read"](r"E:\AAA\xxx\ast_chrome\a08_驱动测试_cookie_打包_发布\astmain_py222\astmain\fs\aaa.txt")
    # print("res1            :", res1)

    # res2 = fff222(r"E:\AAA\xxx\ast_chrome\a08_驱动测试_cookie_打包_发布\astmain_py222\astmain\fs\maker_config.json").read("obj")
    # print("res2            :", type(res2), res2)
