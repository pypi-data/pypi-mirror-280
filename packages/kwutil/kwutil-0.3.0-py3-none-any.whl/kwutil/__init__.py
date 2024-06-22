"""
The kwutil Module
=================

+------------------+------------------------------------------------------+
| Read the docs    | https://kwutil.readthedocs.io                        |
+------------------+------------------------------------------------------+
| Gitlab (main)    | https://gitlab.kitware.com/computer-vision/kwutil    |
+------------------+------------------------------------------------------+
| Github (mirror)  | https://github.com/Kitware/kwutil                    |
+------------------+------------------------------------------------------+
| Pypi             | https://pypi.org/project/kwutil                      |
+------------------+------------------------------------------------------+

The Kitware utility module.

This module is for small, pure-python utility functions. Dependencies are
allowed, but they must be small and highly standard packages (e.g. rich,
psutil, ruamel.yaml).

"""
__version__ = '0.3.0'

__autogen__ = """
mkinit ~/code/kwutil/kwutil/__init__.py --lazy_loader
mkinit ~/code/kwutil/kwutil/__init__.py
"""


__submodules__ = {
    'copy_manager': ['CopyManager'],
    'partial_format': [],
    'slugify_ext': [],
    'util_environ': ['envflag'],
    'util_eval': [],
    'util_exception': [],
    'util_json': [],
    'util_locks': [],
    'util_parallel': ['coerce_num_workers'],
    'util_path': [],
    'util_pattern': [],
    'util_progress': ['ProgressManager'],
    'util_resources': [],
    'util_time': ['datetime', 'timedelta'],
    'util_windows': [],
    'util_random': [],
    'util_yaml': ['Yaml'],
}

import sys

if sys.version_info[0:2] >= (3, 7):

    import lazy_loader
    __getattr__, __dir__, __all__ = lazy_loader.attach(
        __name__,
        submodules={
            'copy_manager',
            'partial_format',
            'slugify_ext',
            'util_environ',
            'util_eval',
            'util_exception',
            'util_json',
            'util_locks',
            'util_parallel',
            'util_path',
            'util_pattern',
            'util_progress',
            'util_random',
            'util_resources',
            'util_time',
            'util_windows',
            'util_yaml',
        },
        submod_attrs={
            'copy_manager': [
                'CopyManager',
            ],
            'util_environ': [
                'envflag',
            ],
            'util_parallel': [
                'coerce_num_workers',
            ],
            'util_progress': [
                'ProgressManager',
            ],
            'util_time': [
                'datetime',
                'timedelta',
            ],
            'util_yaml': [
                'Yaml',
            ],
        },
    )


else:
    # Cant do lazy loading in 3.6
    from kwutil import copy_manager
    from kwutil import partial_format
    from kwutil import slugify_ext
    from kwutil import util_environ
    from kwutil import util_eval
    from kwutil import util_exception
    from kwutil import util_json
    from kwutil import util_locks
    from kwutil import util_parallel
    from kwutil import util_path
    from kwutil import util_pattern
    from kwutil import util_progress
    from kwutil import util_random
    from kwutil import util_resources
    from kwutil import util_time
    from kwutil import util_windows
    from kwutil import util_yaml

    from kwutil.copy_manager import (CopyManager,)
    from kwutil.util_environ import (envflag,)
    from kwutil.util_parallel import (coerce_num_workers,)
    from kwutil.util_progress import (ProgressManager,)
    from kwutil.util_time import (datetime, timedelta)
    from kwutil.util_yaml import (Yaml,)


__all__ = ['CopyManager', 'ProgressManager', 'Yaml', 'coerce_num_workers',
           'copy_manager', 'datetime', 'timedelta', 'envflag',
           'partial_format', 'slugify_ext', 'util_environ', 'util_eval',
           'util_exception', 'util_json', 'util_locks', 'util_parallel',
           'util_path', 'util_pattern', 'util_progress', 'util_random',
           'util_resources', 'util_time', 'util_windows', 'util_yaml']
