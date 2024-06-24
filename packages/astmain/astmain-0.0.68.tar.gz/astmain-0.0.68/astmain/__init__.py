import os
import requests

# 文件操作
from .fs import delete
from .fs import read
from .fs import write
from .fs import cwd


import fs
import desco



# 数据转化
from .to import num


# 操作系统指令
from .cmd import run


def test():
    print("test            :", 15160)
