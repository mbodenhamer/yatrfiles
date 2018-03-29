'''Yatr extension module for yatrfile and extension module development.'''

from yatr import Env
env = Env()

#-------------------------------------------------------------------------------
# cache_all

@env.task('cache_all', display=('path', 'glob', 'urlbase'))
def cache_all(env, *args, **kwargs):
    import fnmatch, os
    from yatr.main import _main

    path = kwargs['path']
    urlbase = kwargs['urlbase']
    glob = kwargs.get('glob', '*')

    for dirpath, _, fnames in os.walk(path):
        for fname in fnames:
            if fnmatch.fnmatch(fname, glob):
                fpath = os.path.join(dirpath, fname)
                relpath = os.path.relpath(fpath, path)
                url = os.path.join(urlbase, relpath)

                if kwargs.get('verbose', False):
                    print('Caching {} -> {}'.format(fpath, url))

                _main('--cache', '-i', fpath, '-o', url)

#-------------------------------------------------------------------------------
