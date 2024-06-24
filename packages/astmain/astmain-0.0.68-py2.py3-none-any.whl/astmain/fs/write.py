import shutil, os, pathlib, json


def write(my_path, xxx):
    if isinstance(xxx, dict) or isinstance(xxx, list):
        print("write.字典和数组")
        with open(my_path, 'w+', encoding="utf-8") as f:
            json_str = json.dumps(xxx, ensure_ascii=False, indent=4)
            f.write(json_str)
            print("write.存储完成", my_path)
            return json_str



    elif isinstance(xxx, str):
        print("write.字符")
        with open(my_path, 'w+', encoding="utf-8") as f:
            f.write(xxx)
            print("write.存储完成", my_path)
            return xxx
    else:
        print("write.其它类型")
        return xxx


if __name__ == '__main__':
    res1 = write(r"./dist1111.txt", "222")
    print("res1            :", res1)
