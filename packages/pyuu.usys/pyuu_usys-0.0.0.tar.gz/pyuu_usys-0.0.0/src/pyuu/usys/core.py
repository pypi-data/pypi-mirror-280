from sqlalchemy import Engine, MetaData
from .common import *
from .util import *
from .service import *

__all__=['Usys']



class Usys(AppEnv):
    name='usys'
    def __init__(self, root_path:Path=None):
        self.sys_env = sys_env = SysEnv()
        root_path = nvl(root_path, sys_env.vars['USYS_PATH'])
        assert root_path

        name = self.name
        root_path = Path(root_path)
        class PATH:
            root = root_path
            assets = root/'assets'
            data = root/'data'
            cache = root/'cache'
            tmp = root/'tmp'
            out = root/'out'

            messey = tmp/'messey'
            export = root/'export'
            test = root/'test'
            test_data = test/'data'

            uu = root/'.uu'             # .uu to indicate root

            secret=data/'secret'
            mod=data/'mod'              # module
            pkg_mngr=mod/'pkg_mngr'/'assets'    
            pm=mod/'pm'                 # app manager

            # ALL_DIRS = [root, assets, data, cache, tmp, out, export, uu, pm]
        self.PATH=PATH

        class DbCtx:
            class core:
                engine=create_sqlite_engine(PATH.data/'core/db.sqlite')
                metadata=MetaData()
                TABLE=make_core_tables(metadata)
                metadata.create_all(engine)

        self.DbCtx=DbCtx
        self.pkg_service=PkgService(self)
        self.pkg_mngr_service=PkgMngrService(self)

        


