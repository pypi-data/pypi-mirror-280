import datetime

from write_add import write_add



def log(info):
    time1 = "error|||"+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "|||"
    content =  "error|||"+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "|||" + info
    write_add(r"C:\Users\Administrator\Desktop\log.txt", content)



if __name__ == '__main__':
    log("11111111111111")
