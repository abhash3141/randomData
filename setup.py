from setuptools import setup, find_packages

setup(
	name='randomData',
	version='0.0.1',
	url='www.github.com/abhash3141/randomData',
	license='GNU',
	author='Abhash',
	packages=find_packages(),
	install_requires=['PyQt5','pandas','sqlalchemy','nltk','numpy','jupyter','python-twitter'],
	entry_points={},
	extras_require={'dev':['flake8',]}
)

