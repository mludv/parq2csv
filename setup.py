import sys
from setuptools import setup, find_packages

with open("README.md") as f:
    long_description = f.read()

setup(
    name='parq2csv',
    version='0.1.1',
    description="Command line tool to transform Apache Parquet files to CSV on the go",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Maximilian Ludvigsson',
    author_email='maxiludvigsson@gmail.com',
    url='https://github.com/mludv/parq2csv',
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    packages=find_packages(),
    platforms='any',
    install_requires=[
        'pandas>=0.22.0',
        'pyarrow>=0.11.0',
    ],
    entry_points={
        'console_scripts': [
            'parq2csv = parq2csv.main:main',
        ]
    },
)
