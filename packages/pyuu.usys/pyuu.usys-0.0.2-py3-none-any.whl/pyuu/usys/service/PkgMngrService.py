import typing
import importlib
if typing.TYPE_CHECKING:
    from ..core import Usys

import sys

from pyuu.uimport import DictMetaPathFinder

from .common import *

__all__=['PkgMngrService']


class PkgModule:
    class PkgMngr(PkgMngrBase):
        pass

class UsysException(Exception):
    pass

class PkgMngrExistsException(UsysException):
    pass


class PkgMngrService:
    def __init__(self, usys:'Usys'):
        self.usys = usys
        self.ctx = usys.DbCtx
        self.pm_module_map={}
        self.pm_meta_path_finder=DictMetaPathFinder(self.pm_module_map)
        sys.meta_path.append(self.pm_meta_path_finder)

    def create_pkg_mngr_from_repo(self, pkg_id:str=None)->PkgModule.PkgMngr:
        return self.create_pkg_mngr(self.get_pkg_mngr_mod_path(pkg_id), pkg_id)

    def create_pkg_mngr(self, pkg_path:Path, pkg_id:str=None)->PkgModule.PkgMngr:
        assert pkg_path.exists()
        pkg_id = nvl(pkg_id, pkg_path.stem)
        full_module_name=f'pyuu.usys.{pkg_id}'
        if pkg_path_exists := self.pm_module_map.get(full_module_name):
            if pkg_path_exists is not None and Path(pkg_path_exists).resolve()!=pkg_path.resolve():
                raise PkgMngrExistsException
        self.pm_module_map[full_module_name]=pkg_path
        m:PkgModule = importlib.import_module(full_module_name)
        pkg_mngr = m.PkgMngr(self.usys, self.get_mod_path(pkg_id))
        return pkg_mngr
    
    def get_pkg_mngr_mod_path(self, pkg_id):
        pkg_mngr_path=self.usys.PATH.pkg_mngr
        p:Path=pkg_mngr_path/f'{pkg_id}.py'
        if p.exists():
            return p
        p=pkg_mngr_path/pkg_id
        if p.exists():
            return p
    
    def save_pkg_mngr_mod(self, pkg_path:Path):
        pkg_mngr_path=self.usys.PATH.pkg_mngr
        pkg_path.copy_to(pkg_mngr_path)
        
    def get_mod_path(self, name):
        P=self.usys.PATH
        class PATH:
            assets:Path=P.pkg_mngr/name
            data:Path=P.data/'mod/pkg_mngr/data'/name
            cache:Path=P.cache/'mod/pkg_mngr'/name
            tmp:Path=P.tmp/'mod/pkg_mngr'/name
            out:Path=P.out/'mod/pkg_mngr'/name
            export:Path=P.pkg_mngr/name/'export'
        return PATH

    def __del__(self):
        if sys.meta_path:
            sys.meta_path.remove(self.pm_meta_path_finder)


