import ast

import os
from setuptools import find_packages, setup

PACKAGE_NAME = 'pathstr'

path = os.path.join(os.path.dirname(__file__), PACKAGE_NAME, '__init__.py')

with open(path, 'r') as file:
    t = compile(file.read(), path, 'exec', ast.PyCF_ONLY_AST)
    for node in (n for n in t.body if isinstance(n, ast.Assign)):
        if len(node.targets) != 1:
            continue

        name = node.targets[0]
        if not isinstance(name, ast.Name) or \
                name.id not in ('__version__', '__version_info__', 'VERSION'):
            continue

        v = node.value
        if isinstance(v, ast.Str):
            version = v.s
            break
        if isinstance(v, ast.Tuple):
            r = []
            for e in v.elts:
                if isinstance(e, ast.Str):
                    r.append(e.s)
                elif isinstance(e, ast.Num):
                    r.append(str(e.n))
            version = '.'.join(r)
            break

# Get the long description from the README file
with open(os.path.join(os.path.dirname(__file__), 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pathstr',

    version=version,

    description='Path string library helps developers to work with strings path. It works similar to standard pathlib.',
    long_description=long_description,

    url='https://github.com/alfred82santa/pathstr',

    author='Alfred Santacatalina',
    author_email='alfred82santa@gmail.com',

    license='LGPLv3',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    # What does your project relate to?
    keywords='string path',
    packages=find_packages(),

    install_requires=[]
)
