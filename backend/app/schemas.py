"""接口出入参模型：列表分页、动作结果与各模块的明细结构。"""
from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PageResult(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int = 1
    size: int = 20


class ActionResult(BaseModel):
    ok: bool
    message: str
    entry: dict[str, Any] | None = None


class EntryPayload(BaseModel):
    """登记或修改一条业务记录时提交的字段集合。"""

    values: dict[str, Any] = Field(default_factory=dict)
    remark: str | None = None



class TablefmtEntry(BaseModel):
    """表格式配置明细结构。"""

    field_0: str | None = None  # 配置编号
    field_1: str | None = None  # 表名称
    field_2: str | None = None  # 格式类型
    field_3: str | None = None  # 分区字段
    field_4: str | None = None  # 主键字段
    field_5: str | None = None  # 排序字段
    field_6: str | None = None  # 版本保留
    field_7: str | None = None  # 配置状态

class CompactEntry(BaseModel):
    """合并任务明细结构。"""

    field_0: str | None = None  # 任务编号
    field_1: str | None = None  # 目标表名
    field_2: str | None = None  # 文件范围
    field_3: str | None = None  # 合并策略
    field_4: str | None = None  # 目标大小
    field_5: str | None = None  # 并行度
    field_6: str | None = None  # 执行耗时
    field_7: str | None = None  # 任务状态

class CompressEntry(BaseModel):
    """压缩配置明细结构。"""

    field_0: str | None = None  # 配置编号
    field_1: str | None = None  # 目标表名
    field_2: str | None = None  # 压缩算法
    field_3: str | None = None  # 压缩字段
    field_4: str | None = None  # 压缩级别
    field_5: str | None = None  # 存储节省
    field_6: str | None = None  # 执行批次
    field_7: str | None = None  # 配置状态

class MetadataEntry(BaseModel):
    """元数据表明细结构。"""

    field_0: str | None = None  # 表编号
    field_1: str | None = None  # 表名称
    field_2: str | None = None  # 字段清单
    field_3: str | None = None  # 分区信息
    field_4: str | None = None  # 统计信息
    field_5: str | None = None  # 最后更新
    field_6: str | None = None  # 数据大小
    field_7: str | None = None  # 表状态

class SnapshotEntry(BaseModel):
    """快照记录明细结构。"""

    field_0: str | None = None  # 快照编号
    field_1: str | None = None  # 表名称
    field_2: str | None = None  # 快照时间
    field_3: str | None = None  # 快照版本
    field_4: str | None = None  # 快照大小
    field_5: str | None = None  # 保留天数
    field_6: str | None = None  # 创建方式
    field_7: str | None = None  # 快照状态

class BranchEntry(BaseModel):
    """分支记录明细结构。"""

    field_0: str | None = None  # 分支编号
    field_1: str | None = None  # 表名称
    field_2: str | None = None  # 分支类型
    field_3: str | None = None  # 源分支
    field_4: str | None = None  # 目标分支
    field_5: str | None = None  # 冲突处理
    field_6: str | None = None  # 合并时间
    field_7: str | None = None  # 分支状态

class RollbackEntry(BaseModel):
    """回滚记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 表名称
    field_2: str | None = None  # 回滚版本
    field_3: str | None = None  # 回滚原因
    field_4: str | None = None  # 影响范围
    field_5: str | None = None  # 恢复耗时
    field_6: str | None = None  # 回滚时间
    field_7: str | None = None  # 回滚状态

class PartitionEntry(BaseModel):
    """演进计划明细结构。"""

    field_0: str | None = None  # 计划编号
    field_1: str | None = None  # 表名称
    field_2: str | None = None  # 当前分区
    field_3: str | None = None  # 目标分区
    field_4: str | None = None  # 演化类型
    field_5: str | None = None  # 预计耗时
    field_6: str | None = None  # 影响行数
    field_7: str | None = None  # 计划状态

class IcebergEntry(BaseModel):
    """优化任务明细结构。"""

    field_0: str | None = None  # 任务编号
    field_1: str | None = None  # 表名称
    field_2: str | None = None  # 优化类型
    field_3: str | None = None  # 优化参数
    field_4: str | None = None  # 执行计划
    field_5: str | None = None  # 资源消耗
    field_6: str | None = None  # 优化效果
    field_7: str | None = None  # 任务状态

class CatalogEntry(BaseModel):
    """同步作业明细结构。"""

    field_0: str | None = None  # 作业编号
    field_1: str | None = None  # 源路径
    field_2: str | None = None  # 目标目录
    field_3: str | None = None  # 同步模式
    field_4: str | None = None  # 增量字段
    field_5: str | None = None  # 过滤规则
    field_6: str | None = None  # 同步频率
    field_7: str | None = None  # 作业状态

class CleanupEntry(BaseModel):
    """清理策略明细结构。"""

    field_0: str | None = None  # 策略编号
    field_1: str | None = None  # 目标表名
    field_2: str | None = None  # 过期条件
    field_3: str | None = None  # 清理方式
    field_4: str | None = None  # 执行周期
    field_5: str | None = None  # 最后清理
    field_6: str | None = None  # 清理行数
    field_7: str | None = None  # 策略状态

class QuotaEntry(BaseModel):
    """配额配置明细结构。"""

    field_0: str | None = None  # 配置编号
    field_1: str | None = None  # 存储空间
    field_2: str | None = None  # 表数量上限
    field_3: str | None = None  # 文件数上限
    field_4: str | None = None  # 告警比例
    field_5: str | None = None  # 超限策略
    field_6: str | None = None  # 有效期至
    field_7: str | None = None  # 配额状态

class LineageEntry(BaseModel):
    """血缘记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 上游表名
    field_2: str | None = None  # 下游表名
    field_3: str | None = None  # 转换类型
    field_4: str | None = None  # 字段映射
    field_5: str | None = None  # 操作时间
    field_6: str | None = None  # 操作批次
    field_7: str | None = None  # 记录状态

class ScheduleEntry(BaseModel):
    """治理任务明细结构。"""

    field_0: str | None = None  # 任务编号
    field_1: str | None = None  # 任务类型
    field_2: str | None = None  # 调度表达式
    field_3: str | None = None  # 依赖任务
    field_4: str | None = None  # 重试策略
    field_5: str | None = None  # 超时分钟
    field_6: str | None = None  # 告警渠道
    field_7: str | None = None  # 任务状态

class StatsEntry(BaseModel):
    """统计报告明细结构。"""

    field_0: str | None = None  # 报告编号
    field_1: str | None = None  # 表名称
    field_2: str | None = None  # 行总数
    field_3: str | None = None  # 文件总数
    field_4: str | None = None  # 总容量
    field_5: str | None = None  # 列统计
    field_6: str | None = None  # 统计时间
    field_7: str | None = None  # 报告状态

class MigrateEntry(BaseModel):
    """迁移任务明细结构。"""

    field_0: str | None = None  # 任务编号
    field_1: str | None = None  # 源表名
    field_2: str | None = None  # 目标表名
    field_3: str | None = None  # 迁移方式
    field_4: str | None = None  # 数据范围
    field_5: str | None = None  # 校验规则
    field_6: str | None = None  # 迁移耗时
    field_7: str | None = None  # 任务状态
