import shutil, os, pathlib, json


def write_add(my_path, xxx):
    if isinstance(xxx, dict) or isinstance(xxx, list):
        print("write.字典和数组")
        with open(my_path, 'a+', encoding="utf-8") as f:
            json_str = json.dumps(xxx, ensure_ascii=False, indent=4)
            f.write(json_str + "\n")
            print("write.存储完成", my_path)
            return True



    elif isinstance(xxx, str):
        print("write.字符")
        with open(my_path, 'a+', encoding="utf-8") as f:
            f.write(xxx + "\n")
            print("write.存储完成", my_path)
            return True
    else:
        print("write.其它类型")
        return False


if __name__ == '__main__':
    res1 = write_add(r"./dist1111.txt", "222")
    print("res1            :", res1)
