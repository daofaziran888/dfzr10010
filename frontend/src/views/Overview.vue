<template>
  <section class="page">
    <header class="page-head">
      <div>
        <h2>运营概览</h2>
        <p class="page-desc">汇总各业务模块的关键指标，先看总量再看异常。</p>
      </div>
    </header>
    <div class="stat-row">
      <article v-for="card in cards" :key="card.label" class="stat-card">
        <span class="stat-label">{{ card.label }}</span>
        <strong class="stat-value">{{ card.value }}</strong>
      </article>
    </div>
    <table class="data-table">
      <thead>
        <tr><th>业务模块</th><th>今日新增</th><th>待处理</th><th>异常量</th></tr>
      </thead>
      <tbody>
        <tr v-for="row in moduleRows" :key="row.name">
          <td>{{ row.name }}</td>
          <td>{{ row.created }}</td>
          <td>{{ row.pending }}</td>
          <td>{{ row.abnormal }}</td>
        </tr>
      </tbody>
    </table>
  </section>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue'

import { fetchJson } from '@/api/client'

type Overview = {
  cards: { label: string; value: number }[]
  modules: { name: string; created: number; pending: number; abnormal: number }[]
}

const cards = ref<Overview['cards']>([])
const moduleRows = ref<Overview['modules']>([])

onMounted(async () => {
  try {
    const payload = await fetchJson<Overview>('/api/overview')
    cards.value = payload.cards
    moduleRows.value = payload.modules
  } catch {
    cards.value = [{"label": "业务模块", "value": 0}, {"label": "今日新增", "value": 0}]
    moduleRows.value = [{"name": "湖表格式管理", "created": 0, "pending": 0, "abnormal": 0}, {"name": "小文件合并", "created": 0, "pending": 0, "abnormal": 0}, {"name": "数据压缩策略", "created": 0, "pending": 0, "abnormal": 0}, {"name": "元数据服务", "created": 0, "pending": 0, "abnormal": 0}, {"name": "表快照管理", "created": 0, "pending": 0, "abnormal": 0}, {"name": "数据分支合并", "created": 0, "pending": 0, "abnormal": 0}, {"name": "数据回滚恢复", "created": 0, "pending": 0, "abnormal": 0}, {"name": "分区演进管理", "created": 0, "pending": 0, "abnormal": 0}, {"name": "表优化管理", "created": 0, "pending": 0, "abnormal": 0}, {"name": "数据目录同步", "created": 0, "pending": 0, "abnormal": 0}, {"name": "数据过期清理", "created": 0, "pending": 0, "abnormal": 0}, {"name": "湖存储配额", "created": 0, "pending": 0, "abnormal": 0}, {"name": "湖仓血缘追踪", "created": 0, "pending": 0, "abnormal": 0}, {"name": "治理任务调度", "created": 0, "pending": 0, "abnormal": 0}, {"name": "表统计信息", "created": 0, "pending": 0, "abnormal": 0}, {"name": "数据迁移管理", "created": 0, "pending": 0, "abnormal": 0}]
  }
})
</script>
