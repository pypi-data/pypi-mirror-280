from .common import *
from sqlalchemy import Column, Integer, MetaData, Table, Text, and_


def create_sqlite_engine(pth:Path):
    if logger.level <=logging.DEBUG:
        debug=True

    pth.prnt.mkdir()
    engine = create_engine(f'sqlite:///{pth}',echo=debug)
    with engine.begin() as conn:
        conn.exec_driver_sql('PRAGMA journal_mode = WAL;')
        conn.exec_driver_sql('PRAGMA synchronous = NORMAL;')
    return engine


def make_cols_map(c, names):
    return {name:c.get(name) for name in names}

def make_core_tables(metadata:MetaData=None):
    if metadata is None:
        metadata = MetaData()

    class TABLE:
        Pkg = Table(
            'Pkg', metadata,
            Column('rid', Integer, primary_key=True, autoincrement=True),
            Column('pkg_id', Text, nullable=False, index=True),
            Column('version', Text, nullable=False,),
            Column('path', Text)
        )

        __keys={
            id(Pkg):make_cols_map(Pkg.c, ['pkg_id', 'version'])
        }

        @staticmethod
        def get_keys_map(pkg):
            return TABLE.__keys[id(pkg)]

    return TABLE


def make_stmt_eqs(cols_map:dict, vals_map:dict):
    eqs=[]
    for k in cols_map:
        if k in vals_map:
            eqs.append(cols_map[k]==vals_map[k])
    return and_(*eqs)

