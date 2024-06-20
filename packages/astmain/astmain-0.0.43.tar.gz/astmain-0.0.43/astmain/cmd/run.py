from subprocess import run as subprocess_run


def run(cmd_str='', echo_print=1):
    """
    执行cmd命令，不显示执行过程中弹出的黑框
    备注：subprocess.run()函数会将本来打印到cmd上的内容打印到python执行界面上，所以避免了出现cmd弹出框的问题
    :param cmd_str: 执行的cmd命令
    :return:
    """

    if echo_print == 1:
        print('\n执行cmd指令="{}"'.format(cmd_str))
    subprocess_run(cmd_str, shell=True)
