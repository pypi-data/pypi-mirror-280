import typing
if typing.TYPE_CHECKING:
    from .core import Usys

import sqlalchemy as sa
from sqlalchemy import Engine, create_engine

from pyuu.common import *
from pyuu.trivial import *
from pyuu.path import Path
from pyuu.env import AppEnv, SysEnv
from pyuu.project import ProjPath


class PkgMngrBase:
    def __init__(self, usys:'Usys', PATH:ProjPath):
        self.usys=usys
        self.PATH=PATH

    def register(self, update):
        pass


