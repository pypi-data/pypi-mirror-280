import typing
if typing.TYPE_CHECKING:
    from ..core import Usys
from .common import *

__all__=['PkgService']

class PkgService:
    def __init__(self, usys:'Usys'):
        self.ctx = usys.DbCtx

    @property
    def TABLE(self):
        return self.ctx.core.TABLE
    
    @property
    def engine(self):
        return self.ctx.core.engine

    def get_pkg_path(self, pkg_id, version):
        pass

    def begin(self):
        return self.engine.begin()

    def register_pkg(self, pkg_id, version, path, *, update=True, conn:sa.Connection=None):
        TABLE=self.TABLE
        engine=self.engine

        version=nvl(version, '')

        def impl(conn:sa.Connection):
            stmt=sa.insert(TABLE.Pkg).values(pkg_id=pkg_id, version=version, path=str(path))
            if update:
                self.unregister_pkg(pkg_id, version, conn=conn)
                conn.execute(stmt)
            else:
                conn.execute(stmt)

        if conn is None:
            with self.begin() as conn:
                impl(conn)
        else:
            impl(conn)


    def unregister_pkg(self, pkg_id, version='', *, conn:sa.Connection=None):
        TABLE=self.TABLE
        engine=self.engine
        Pkg=TABLE.Pkg

        version=nvl(version, '')

        def impl(conn:sa.Connection):
            stmt=sa.delete(Pkg).where(util.make_stmt_eqs(TABLE.get_keys_map(TABLE.Pkg), dict(pkg_id=pkg_id, version=version)))
            conn.execute(stmt)

        if conn is None:
            with self.begin() as conn:
                impl(conn)
        else:
            impl(conn)
        


