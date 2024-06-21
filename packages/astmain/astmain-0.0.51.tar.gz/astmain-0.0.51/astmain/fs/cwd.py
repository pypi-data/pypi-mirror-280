import os
def cwd(my_path=""):
    if (my_path):

        current_dir = os.getcwd()
        return os.path.join(current_dir,my_path)
    else:
        return os.getcwd()

