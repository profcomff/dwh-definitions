import os
import sys


__version__ = '1.0.0'  # Не менять, работает автоматика


dir_path = os.path.dirname(os.path.abspath(__file__))
tables = []
for folder in ['STG', 'DWH', 'DM', 'ODS']:
    files_in_dir = [f[:-3] for f in os.listdir(dir_path + '/' + folder) if f.endswith('.py') and f != '__init__.py']
    for f in files_in_dir:
        mod = __import__('.'.join([__name__, folder, f]), fromlist=[f])
        to_import = [getattr(mod, x) for x in dir(mod) if isinstance(getattr(mod, x), type)]
        for i in to_import:
            tables.append([i.__name__, i])
            try:
                setattr(sys.modules[__name__], i.__name__, i)
            except AttributeError:
                pass
