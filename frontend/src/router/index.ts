import { createRouter, createWebHistory } from 'vue-router'

import Overview from '@/views/Overview.vue'
const Tablefmt = () => import('@/views/tablefmt/index.vue')
const Compact = () => import('@/views/compact/index.vue')
const Compress = () => import('@/views/compress/index.vue')
const Metadata = () => import('@/views/metadata/index.vue')
const Snapshot = () => import('@/views/snapshot/index.vue')
const Branch = () => import('@/views/branch/index.vue')
const Rollback = () => import('@/views/rollback/index.vue')
const Partition = () => import('@/views/partition/index.vue')
const Iceberg = () => import('@/views/iceberg/index.vue')
const Catalog = () => import('@/views/catalog/index.vue')
const Cleanup = () => import('@/views/cleanup/index.vue')
const Quota = () => import('@/views/quota/index.vue')
const Lineage = () => import('@/views/lineage/index.vue')
const Schedule = () => import('@/views/schedule/index.vue')
const Stats = () => import('@/views/stats/index.vue')
const Migrate = () => import('@/views/migrate/index.vue')

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'overview', component: Overview },
    { path: '/tablefmt', name: 'tablefmt', component: Tablefmt },
    { path: '/compact', name: 'compact', component: Compact },
    { path: '/compress', name: 'compress', component: Compress },
    { path: '/metadata', name: 'metadata', component: Metadata },
    { path: '/snapshot', name: 'snapshot', component: Snapshot },
    { path: '/branch', name: 'branch', component: Branch },
    { path: '/rollback', name: 'rollback', component: Rollback },
    { path: '/partition', name: 'partition', component: Partition },
    { path: '/iceberg', name: 'iceberg', component: Iceberg },
    { path: '/catalog', name: 'catalog', component: Catalog },
    { path: '/cleanup', name: 'cleanup', component: Cleanup },
    { path: '/quota', name: 'quota', component: Quota },
    { path: '/lineage', name: 'lineage', component: Lineage },
    { path: '/schedule', name: 'schedule', component: Schedule },
    { path: '/stats', name: 'stats', component: Stats },
    { path: '/migrate', name: 'migrate', component: Migrate },
  ],
})

export default router
