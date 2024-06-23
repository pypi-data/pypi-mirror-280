from setuptools import setup, find_packages

setup(
name='pivotr',
version='0.1.0',
author='Maturon Miner III',
author_email='maturon@protonmail.com',
description='A remote command execution and pivoting framework',
packages=find_packages(),
install_requires=['netifaces', 'scp'],
classifiers=[
'Programming Language :: Python :: 3',
'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
'Operating System :: POSIX :: Linux',
],
python_requires='>=3.6',
)