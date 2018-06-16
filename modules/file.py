'''Yatr extension module for file operations.'''

from yatr import Env
env = Env()

#-------------------------------------------------------------------------------
# replace_in_file

@env.task('replace-in-file', display=('path', 'pattern', 'repl'))
def replace_in_file(env, *args, **kwargs):
    import re

    path = kwargs['path']
    pattern = kwargs['pattern']
    repl = kwargs['repl']

    with open(path, 'r') as f:
        txt = f.read()

    txt = re.sub(pattern, repl, txt)

    with open(path, 'w') as f:
        f.write(txt)

#-------------------------------------------------------------------------------
