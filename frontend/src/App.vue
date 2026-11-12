<template>
  <div class="app-shell">
    <aside class="app-side">
      <h1 class="app-title">湖仓一体化治理平台</h1>
      <nav class="nav-list">
        <RouterLink v-for="item in navItems" :key="item.path" :to="item.path" class="nav-item">
          {{ item.label }}
        </RouterLink>
      </nav>
    </aside>
    <main class="app-main">
      <header class="app-head">
        <span class="head-desc">面向数据架构师的湖仓一体化治理平台。覆盖数据湖表格式管理、Iceberg/Hudi表优化、小文件合并、数据压缩策略、元数据服务、表快照管理、数据分支合并与数据回滚恢复的完整湖仓治理链路。</span>
        <span class="head-user">当前值班：{{ store.operator }} · {{ store.shiftLabel }}</span>
      </header>
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import { useSessionStore } from '@/stores/session'

const store = useSessionStore()

const navItems = [{ label: "运营概览", path: "/" }, { label: "湖表格式管理", path: "/tablefmt" }, { label: "小文件合并", path: "/compact" }, { label: "数据压缩策略", path: "/compress" }, { label: "元数据服务", path: "/metadata" }, { label: "表快照管理", path: "/snapshot" }, { label: "数据分支合并", path: "/branch" }, { label: "数据回滚恢复", path: "/rollback" }, { label: "分区演进管理", path: "/partition" }, { label: "表优化管理", path: "/iceberg" }, { label: "数据目录同步", path: "/catalog" }, { label: "数据过期清理", path: "/cleanup" }, { label: "湖存储配额", path: "/quota" }, { label: "湖仓血缘追踪", path: "/lineage" }, { label: "治理任务调度", path: "/schedule" }, { label: "表统计信息", path: "/stats" }, { label: "数据迁移管理", path: "/migrate" }]
</script>
