from setuptools import find_packages, setup

def long_description():
    with open('README.md') as f:
        return f.read()

setup(
    name = 'pyven',
    version = '94',
    description = 'Manage development of multiple Python projects',
    long_description = long_description(),
    long_description_content_type = 'text/markdown',
    url = 'https://pypi.org/project/pyven/',
    author = 'foyono',
    author_email = 'shrovis@foyono.com',
    packages = find_packages(),
    py_modules = [],
    install_requires = ['aridity>=67', 'diapyr>=27', 'lagoon>=24', 'setuptools>=44.1.1', 'twine>=1.15.0', 'venvpool>=10'],
    package_data = {'': ['*.pxd', '*.pyx', '*.pyxbld', '*.arid', '*.aridt']},
    entry_points = {'console_scripts': ['drmake=pyven.drmake:main', 'gclean=pyven.gclean:main', 'launch=pyven.launch:main', 'minreqs=pyven.minreqs:main', 'pipify=pyven.pipify:main', 'release=pyven.release:main', 'tasks=pyven.tasks:main', 'tryinstall=pyven.tryinstall:main', 'tests=pyven.tests.__init__:main']},
)
