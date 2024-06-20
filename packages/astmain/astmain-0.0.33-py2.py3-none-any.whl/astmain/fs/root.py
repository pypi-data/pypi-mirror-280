def root():

    import os

    current_dir = os.getcwd()
    print(1, current_dir)


    from pathlib import Path

    current_dir = Path.cwd()
    print(2, current_dir)



    import os

    current_dir = os.path.dirname(os.path.abspath(__file__))
    print(3,   current_dir)


    import os
    import sys

    current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    print(4,  current_dir)
    print(5,  sys.argv)



        # 获取当前脚本文件的绝对路径
    script_path = os.path.abspath(__file__)

    # 获取当前项目的路径
    project_path = os.path.dirname(script_path)
    print(6,project_path)



    from pathlib import Path

    # 获取当前脚本文件的绝对路径
    script_path = Path(__file__).resolve()

    # 获取当前项目的路径
    project_path = script_path.parent
    print(7,project_path)