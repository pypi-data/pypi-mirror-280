import sys
import os

# from cx_Freeze import setup, Executable
from setuptools import setup, find_packages

build_exe_options = {
    'packages': [
        'common',
        'logs',
        'server',
    ]
}


setup(name="My_Server_Chat_129m",
      version='1.0',
      description='Server Chat',
      authors='Maksim',
      author_mail='himsecurety@mail.ru',
      packages= find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome']
      )


# setup(
#     name='server',
#     version='1.0',
#     description='server_chat',
#     options={
#         'build_exe': build_exe_options
#     },
#     executables=[Executable(
#         'server.py',
#         target_name='server.exe'
#     )]
# )
