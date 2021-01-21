from lib.utils.plugin import import_plugin
from .hive_metastore_loader import HMSMetastoreLoader
from .mysql_metastore_loader import MysqlMetastoreLoader
from .thrifthive_metastore_loader import HMSThriftMetastoreLoader
from .sqlalchemy_metastore_loader import SqlAlchemyMetastoreLoader

ALL_PLUGIN_METASTORE_LOADERS = import_plugin(
    "metastore_plugin", "ALL_PLUGIN_METASTORE_LOADERS", []
)


ALL_METASTORE_LOADERS = [
    HMSMetastoreLoader,
    MysqlMetastoreLoader,
    HMSThriftMetastoreLoader,
    SqlAlchemyMetastoreLoader,
] + ALL_PLUGIN_METASTORE_LOADERS