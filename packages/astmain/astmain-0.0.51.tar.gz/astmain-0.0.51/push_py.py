import time

# 读取 TOML 文件
with open('pyproject.toml', 'r', encoding='utf-8') as toml_file:
    import toml

    config = toml.load(toml_file)

# 访问配置数据
print(config)
version = config["project"]["version"]
print("version            :", version)
version1 = version.split(".")[0]
version2 = version.split(".")[1]
version3 = version.split(".")[2]

version = str(version1) + "." + str(version2) + "." + str(int(version3) + 1)
print("version            :", version)

config["project"]["version"] = version

# 写入 TOML 文件
with open('pyproject.toml', 'w', encoding='utf-8') as toml_file:
    import pytoml

    pytoml.dump(config, toml_file)


def run_cmd_run(cmd_str='', echo_print=1):
    """
    执行cmd命令，不显示执行过程中弹出的黑框
    备注：subprocess.run()函数会将本来打印到cmd上的内容打印到python执行界面上，所以避免了出现cmd弹出框的问题
    :param cmd_str: 执行的cmd命令
    :return:
    """
    from subprocess import run
    if echo_print == 1:
        print('\n执行cmd指令="{}"'.format(cmd_str))
    run(cmd_str, shell=True)


def run_open_borwser(str1):
    import webbrowser
    webbrowser.open(str1)


def run_file_delete(file_path):
    import shutil, os
    if os.path.exists(file_path):
        shutil.rmtree(file_path)
        print("ok File deleted successfully.")
    else:
        print("no File does not exist.")


run_cmd_run('      conda     activate           sss111')
time.sleep(1)

# 打包和发布
run_cmd_run('     flit publish    ')
run_open_borwser("https://pypi.org/project/astmain/")

# # 删除文件夹_结束时
run_file_delete('dist')

print("上传完成:=======================            ", f"pip install  astmain=={version}")

# run_cmd_run(f"pip install  astmain=={version}")

"""

pip uninstall astmain  &&  pip install   astmain


"""