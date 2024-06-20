import json
import shutil, os, pathlib


class fff:
    def __init__(self, my_path):
        self.my_path = my_path
        pass
        self.my_error = ""

    def is_error(self):


    def read(self, typeof="str"):
        if not self.is_error():
            return self.my_error

        if typeof == "str":
            with open(self.my_path, 'r', encoding='utf-8') as f:
                return f.read()

        if typeof == "obj":
            with open(self.my_path, 'r', encoding='utf-8') as f:
                return json.load(f)


if __name__ == '__main__':
    res1 = fff(r"E:\AAA\xxx\ast_chrome\a08_驱动测试_cookie_打包_发布\astmain_py222\astmain\fs\aaa.txt").read()
    print("res1            :", res1)

    res2 = fff(r"E:\AAA\xxx\ast_chrome\a08_驱动测试_cookie_打包_发布\astmain_py222\astmain\fs\maker_config.json").read("obj")
    print("res2            :", type(res2), res2)
