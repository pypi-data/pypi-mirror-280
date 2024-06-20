import shutil, os, pathlib


def write(my_path,xxx):
    my_error = ""
    # # 判断绝对路径
    # if not os.path.isabs(my_path):
    #     my_error = my_error + f"1请检查路径是不是绝对路径|      {my_path}"

    # 判断存在文件吗
    if not os.path.exists(my_path):
        my_error = my_error + f"2请检查路径是否存在      |       {my_path}"

    if not my_error == "":
        print("fs.read            my_error:", my_error)

    # ========================================================================


    if isinstance(xxx,dict) or isinstance(xxx,list):
        print("write.字段和数组")
        with open(my_path, 'w+', encoding="utf-8") as f:
            json_str= json.dumps(xxx,ensure_ascii=False, indent=4)
            f.write(json_str)
            return json_str


    
    elif isinstance(xxx,str):
        print("write.字符")
        with open(my_path, 'w+', encoding="utf-8") as f:
            f.write(xxx)
            return xxx
    else:
        print("write.其它类型")
        return xxx










if __name__ == '__main__':
    res1 = write(r"C:\Users\Administrator\Desktop\astmain_py222\aaa222.txt","222")
    print("res1            :", res1)

 
