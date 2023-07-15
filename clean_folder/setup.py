from setuptools import setup

setup(
    name='clean_folder',
    version='1.0',
    author='Viacheslav Artemenko',
    author_email='v.a.artemenko1990@gmail.com',
    description='A package for cleaning folders',
    packages=['clean_folder'],
    entry_points={
        'console_scripts': [
            'clean-folder=clean_folder.main:main'
        ]
    },
)