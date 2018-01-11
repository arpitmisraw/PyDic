from setuptools import setup

setup(
	name='PyDic',
	version=1.0,
	py_modules=[
		'main',
	],
	install_requires=[
		'bs4',
		'BeautifulSoup',
		'PyDictionary',
	],
	entry_points={
		'console_scripts':[
		'main=main:cli',
		]
	},
)
