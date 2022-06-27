from setuptools import find_packages, setup

install_requires = []


setup(
	name='graphicshell',
	packages=find_packages(include=['graphicshell']),
	version='0.0.1',
	description='A graphics library for the terminal',
	author='jormungandr1105',
	license='MIT',
	install_requires=install_requires
)
