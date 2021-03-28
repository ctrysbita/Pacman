import os

base_dir = os.path.abspath(os.path.split(os.path.abspath(os.path.realpath(__file__)))[0])
print(base_dir)