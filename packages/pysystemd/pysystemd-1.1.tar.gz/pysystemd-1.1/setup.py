from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pysystemd',
    packages=['pysystemd'],
    version='1.1',
    description='A systemd binding Library in Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='alimiracle',
    author_email='alimiracle@riseup.net',
    url='https://codeberg.org/alimiracle/pysystemd',
    license='LGPL v3',
    keywords=['services', 'init', 'systemd'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Operating System :: POSIX :: Linux',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
