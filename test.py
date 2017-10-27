import os
from yatr import Document

DIR = os.path.abspath(os.path.dirname(__file__))

#-------------------------------------------------------------------------------

def find_yamlfiles(path):
    for dirpath, _, fnames in os.walk(path):
        for fname in fnames:
            if fname.endswith('.yml'):
                yield os.path.join(dirpath, fname)

#-------------------------------------------------------------------------------

def test():
    for fpath in find_yamlfiles(os.path.join(DIR, 'yatrfiles')):
        print(fpath)
        doc = Document.from_path(fpath)
        doc.env.resolve_macros()
        # If we get here, it validated

#-------------------------------------------------------------------------------

if __name__ == '__main__':
    test()
