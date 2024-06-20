import setuptools  # 导入setuptools打包工具
from datetime import datetime
from maker_obj import maker_obj

# 读取文件README.md
with open("README.md", "r", encoding="utf-8") as f:
    README = f.read()

obj = maker_obj()

aaa = dict(
    name="astmain",  # 用自己的名替换其中的YOUR_USERNAME_
    # version="0.0.15",  # 包版本号，便于维护版本,保证每次发布都是版本都是唯一的
    version="0.0." + str(obj["version"]),  # 包版本号，便于维护版本,保证每次发布都是版本都是唯一的
    author="astmain",  # 作者，可以写自己的姓名
    author_email="1311192345@qq.com",  # 作者联系方式，可写自己的邮箱地址
    description="更新时间:" + datetime.now().strftime("%Y_%m_%d__%H_%M_%S "),  # 包的简述
    long_description=README,  # 包的详细介绍，一般在README.md文件内
    long_description_content_type="text/markdown",
    url="https://github.com",  # 自己项目地址，比如github的项目地址
    keywords=["python", "tools"],
    # install_requires=["requests"],
    install_requires=obj["install_requires"],
    packages=setuptools.find_packages(),
    # entry_points={ "console_scripts" : ['mwjApiTest = mwjApiTest.manage:run'] }, #安装成功后，在命令行输入mwjApiTest 就相当于执行了mwjApiTest.manage.py中的run了
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # 对python的最低版本要求

)

setuptools.setup(**aaa)

"""
python push.py develop


py

import astmain
astmain.con()



# 编译
python push_py.py sdist 
python -m   twine upload    dist/*



"""

r"""
C:\Users\Administrator


PyPI recovery codes
a64f1299d6e73953
97c7e2555a19b771
50088d4844a9c952
7715f45f82c03fe3
3120d031b98a50f0
6d2019c7bc0d00e8
c3f4d0420ca5ae40
a3ae8f1b7bb7219f


a64f1299d6e73953
97c7e2555a19b771
50088d4844a9c952
7715f45f82c03fe3
3120d031b98a50f0
6d2019c7bc0d00e8
c3f4d0420ca5ae40
a3ae8f1b7bb7219f


python -m pip install --user --upgrade setuptools wheel
python -m pip install --user --upgrade twine



"""
