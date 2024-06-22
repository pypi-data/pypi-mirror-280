import os
from dektools.file import remove_path
from dektools.shell import shell_wrapper
from .tmpl import ProjectGenerator


def build_target(path, data=None):
    data = data or {}
    data_default = dict(entry='main.py', name='main')
    ProjectGenerator(path, {**data_default, **data}).render()
    for fn in ['build', 'dist']:
        remove_path(os.path.join(path, fn))
    shell_wrapper(f'pyinstaller .pyinstaller.spec', chdir=path)
