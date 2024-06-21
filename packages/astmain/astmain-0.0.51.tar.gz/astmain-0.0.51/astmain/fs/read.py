import shutil, os, pathlib


def read(my_file_path):
    my_error = ""
    # 判断绝对路径
    # if not os.path.isabs(my_file_path):
    #     my_error = my_error + f"1请检查路径是不是绝对路径|      {my_file_path}"

    # 判断存在文件吗
    if not os.path.exists(my_file_path):
        my_error = my_error + f"2请检查路径是否存在      |       {my_file_path}"

    if not my_error == "":
        print("fs.read            my_error:", my_error)

    # ========================================================================

    with open(my_file_path, 'r', encoding='utf-8') as f:
        return f.read()


#
# def read(my_path):
#     # if not self.is_error():
#     #     return self.my_error
#
#
#     with open(my_path, 'r', encoding='utf-8') as f:
#         return f.read()


if __name__ == '__main__':
    res1 = read(r"E:\AAA\xxx\ast_chrome\a08_驱动测试_cookie_打包_发布\astmain_py222\astmain\fs\aaa.txt")
    print("res1            :", res1)

    res2 = read(r"E:\AAA\xxx\ast_chrome\a08_驱动测试_cookie_打包_发布\astmain_py222\astmain\fs\maker_config.json")
    print("res2            :", res2)
