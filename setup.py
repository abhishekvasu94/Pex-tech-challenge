from setuptools import setup

setup(name="mytool",
	version = "0.1",
	py_modules=['test'],
	install_requires=[
		'Click',
		],
	entry_points='''
		[console_scripts]
		mytool=test:cli
	''',
)
