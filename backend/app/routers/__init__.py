"""业务模块路由汇总。

这里统一按别名导入再暴露 ROUTERS：模块名有可能和内置名撞车（某个业务模块就叫 dict、list
这种名字时），按名字直接 import 会把内置类型覆盖掉，函数注解在运行时求值就会报
'module' object is not subscriptable。
"""
from __future__ import annotations

from app.routers import tablefmt as router_tablefmt
from app.routers import compact as router_compact
from app.routers import compress as router_compress
from app.routers import metadata as router_metadata
from app.routers import snapshot as router_snapshot
from app.routers import branch as router_branch
from app.routers import rollback as router_rollback
from app.routers import partition as router_partition
from app.routers import iceberg as router_iceberg
from app.routers import catalog as router_catalog
from app.routers import cleanup as router_cleanup
from app.routers import quota as router_quota
from app.routers import lineage as router_lineage
from app.routers import schedule as router_schedule
from app.routers import stats as router_stats
from app.routers import migrate as router_migrate

ROUTERS = [router_tablefmt, router_compact, router_compress, router_metadata, router_snapshot, router_branch, router_rollback, router_partition, router_iceberg, router_catalog, router_cleanup, router_quota, router_lineage, router_schedule, router_stats, router_migrate]
