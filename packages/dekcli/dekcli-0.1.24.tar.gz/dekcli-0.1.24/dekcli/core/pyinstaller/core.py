import os
from dektools.file import remove_path
from dektools.shell import shell_wrapper
from dekvenv.active import dir_name_venv, sys_paths_relative
from .tmpl import ProjectGenerator


def build_target(path, data=None):
    data = data or {}
    platlib = sys_paths_relative(os.path.join(path, dir_name_venv))['platlib']
    data_default = dict(entry='main.py', name='main', venv=repr(platlib) if os.path.isdir(platlib) else '')
    ProjectGenerator(path, {**data_default, **data}).render()
    for fn in ['build', 'dist']:
        remove_path(os.path.join(path, fn))
    shell_wrapper(f'pyinstaller .pyinstaller.spec', chdir=path)
