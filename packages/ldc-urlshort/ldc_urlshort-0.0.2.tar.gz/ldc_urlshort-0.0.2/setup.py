from setuptools import setup

setup(
    name='ldc-urlshort',
    version='0.0.2',
    description='A simple package to shorten URLs',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='Pratik Kumar',
    author_email='pratik.kumar@lendenclub.com',
    packages=['urlshort', 'urlshort.migrations'],
	classifiers=[
		"Intended Audience :: Developers",
		"Programming Language :: Python :: 3",
		"Topic :: Utilities"
	],
    install_requires=[
        'Django>=3.2.16',
        'djangorestframework>=3.14.0',
        'python-dateutil',
    ],
	include_package_data=True
)