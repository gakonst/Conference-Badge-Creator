try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Conference Badge Creator',
    'author': 'Georgios Konstantopoulos',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'georgkonst@ece.auth.gr',
    'version': '1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)