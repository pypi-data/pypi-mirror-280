import json
import shutil, os, pathlib
from astmain.fs.read import read

from types import SimpleNamespace
from collections import namedtuple
fff222 = dict(read=read)
fff222=SimpleNamespace(**fff222)

if __name__ == '__main__':
    res1 = fff222.read(r"E:\AAA\xxx\ast_chrome\a08_驱动测试_cookie_打包_发布\astmain_py222\astmain\fs\aaa.txt")
    print("res1            :", res1)

    # res2 = fff222(r"E:\AAA\xxx\ast_chrome\a08_驱动测试_cookie_打包_发布\astmain_py222\astmain\fs\maker_config.json").read("obj")
    # print("res2            :", type(res2), res2)
