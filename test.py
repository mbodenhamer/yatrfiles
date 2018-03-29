import os
from yatr.main import _main

DIR = os.path.abspath(os.path.dirname(__file__))

#-------------------------------------------------------------------------------

def find_yamlfiles(path):
    for dirpath, _, fnames in os.walk(path):
        for fname in fnames:
            if os.path.basename(dirpath) != 'test':
                if fname.endswith('.yml'):
                    yield os.path.join(dirpath, fname)

#-------------------------------------------------------------------------------

def test():
    for fpath in find_yamlfiles(os.path.join(DIR, 'yatrfiles')):
        print(fpath)
        _main('-f', fpath, '--validate')

#-------------------------------------------------------------------------------

if __name__ == '__main__':
    test()
