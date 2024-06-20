import os
import locale
import platform
from dataclasses import dataclass
from tkinter import NO

from pyuu.project import *
from pyuu.trivial import *

__all__=[
    'SysEnv',
    'AppEnv',
]


@dataclass
class SysEnv:
    # platform:str
    # arch:str
    # vars:dict
    # shell_encoding:str

    def __init__(self):
        self.platform=platform.system().lower()
        self.arch=platform.machine().lower()
        self.vars=os.environ    # system enviroment variables
        self.shell_encoding=locale.getpreferredencoding(False)



@dataclass
class AppEnv:
    pass
    # def __init__(self, 
    #              root_path=None,
    #              name='',
    #              PATH=None
    #              ):
    #     pass
        # if PATH is None:
        #     root_path = Path(root_path)
        #     PATH = make_project_path(root_path, name)
        
