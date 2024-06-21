import sys
import os

# from cx_Freeze import setup, Executable
from setuptools import setup, find_packages

build_exe_options = {
    'packages': [
        'common',
        'logs',
        'client',
        'sqlite3',
        'dlls',
    ]
}

setup(name="My_Client_129m",
      version='1.0',
      description='client Chat',
      authors='Maksim',
      author_mail='himsecurety@mail.ru',
      packages= find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome']
      )

