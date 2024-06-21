import shutil, os, pathlib


def delete(file_path):
    my_error = ""
    # # 判断绝对路径
    # if not os.path.isabs(file_path):
    #     my_error = my_error + f"1请检查路径是不是绝对路径|      {file_path}"

    # 判断存在文件吗
    if not os.path.exists(file_path):
        my_error = my_error + f"2请检查路径是否存在      |       {file_path}"

    # 执行_删除文件
    if pathlib.Path(file_path).is_file():
        os.remove(file_path)

    # 执行_删除文件夹
    if pathlib.Path(file_path).is_dir():
        shutil.rmtree(file_path, ignore_errors=True)

    if not my_error == "":
        print("fs.delete            my_error:", my_error)


if __name__ == '__main__':
    # run_file_delete("aaa.txt")
    delete(r"E:\AAA\xxx\ast_chrome\a08_驱动测试_cookie_打包_发布\astmain_py222\astmain\fs\aaa.txt")
