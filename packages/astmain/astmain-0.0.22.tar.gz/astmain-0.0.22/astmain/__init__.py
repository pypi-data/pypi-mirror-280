import os
import requests
from .fs import delete
from .fs import read


def con():
    print("conconconconconconconconconcon            :", 111111111111)


def fss(file_path, text):
    try:
        with open(file_path, "w", encoding='utf-8') as f:
            f.write(text)

        print("成功  fss          :", 1)
    except Exception as error:
        print("失败  fss         :", str(error))
