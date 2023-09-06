import ast
import os
from os import listdir
from os.path import isfile, join


ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for folder in ['DM', 'DWH', 'ODS', 'STG']:
    onlyfiles = [f for f in listdir(ROOT_DIR + '/' + folder) if isfile(join(ROOT_DIR + '/' + folder, f))]
    onlyfiles.remove('README.md')
    onlyfiles.remove('__init__.py')
    __all__ = []

    for file in onlyfiles:
        file_path = ROOT_DIR + '/' + folder + '/' + file
        with open(file_path, 'r', encoding='utf-8') as f:
            tree = ast.parse(f.read())

        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                __all__.append(node.name)
