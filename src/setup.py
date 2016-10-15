try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'CParse data from excel or dictionary.txt file and print it on your badge.',
    'author': 'Georgios Konstantopoulos',
    'url': 'github.com/1337GAK/Conference-Badge-Creator',
    'download_url': 'Where to download it.',
    'author_email': 'georgkonst@ece.auth.gr',
    'version': '1.0',
    'install_requires': ['PIL','openpyxl'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'Conference Badge Creator'
}

setup(**config)
