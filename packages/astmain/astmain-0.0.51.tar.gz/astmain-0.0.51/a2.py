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