# OHAO - AI绘画提示词工具

一个纯前端的提示词管理与编辑页面。支持分类/分组管理、标签拖拽排序、历史快照存储、JSON 导入/导出、本地持久化，以及可选的 Dropbox 云同步；同时提供一键导出提示词区域为图片（html2canvas）。

## 功能一览

- 分类管理
  - 新建/编辑/删除分类
  - 分组（子类）管理与显式顺序控制（groupsOrder 上移/下移）
  - 右键菜单：分类上移/下移、编辑名称、删除
- 提示词标签
  - 新增/编辑/删除标签，支持中英双段（text / lang_zh）
  - 标签置顶/取消置顶
  - 拖拽排序（支持多行容器空白区域精准插入）
  - 可配置自定义右键菜单外链（基于模板构建 URL）
- 编辑器与历史
  - 编辑器内容与标签联动
  - 一键存储当前提示词快照；支持历史列表查看、删除、清空
- 数据存储与导入/导出
  - 本地存储到 localStorage（常用提示词、历史、菜单配置）
  - 导入/导出 JSON（本地文件或 Dropbox）
  - 支持兼容多种结构：旧版纯对象、新版封装、分组版
- 主题与外观
  - 亮/暗主题切换（跟随系统偏好并持久化）
  - 现代化 UI，Font Awesome 图标
- 图片导出
  - 使用 html2canvas 将提示词区域导出为透明背景 PNG
- 云同步（可选）
  - Dropbox OAuth 登录后上传/下载 JSON
  - 文件列表刷新与文件选择

## 快速开始

1. 直接在任意现代浏览器打开 `index.html`。
2. 页面依赖在线资源：
   - Font Awesome（cdnjs）
   - html2canvas（jsDelivr，运行时动态加载）
   如需离线运行，请自行下载上述依赖并改为本地引用。
3. 开始使用页面左侧分类与右侧编辑功能。

## 使用指南

- 分类与分组
  - 点击“添加分类”按钮新建分类。
  - 对分组可通过右键菜单进行上移/下移，维持显式顺序（groupsOrder）。
- 标签
  - 在当前分类下点击“添加标签”，填写英文（text）与中文（lang_zh）。
  - 标签支持：
    - 点击切换启用/禁用（inactive）状态
    - 右键菜单：置顶/取消置顶、编辑、删除、自定义外链
    - 拖拽排序（支持在空白区域拖入精准定位）
- 编辑与历史
  - 编辑器内容变化会同步渲染标签。
  - 点击“存储”保存当前快照；点击“查看历史”打开历史列表，可删除或清空。
- 导入/导出
  - “下载JSON/上传”：在本地下载完整数据或（登录 Dropbox 后）上传到选定的云端文件。
  - “导入JSON”：本地选择 JSON 文件或（登录 Dropbox 后）从云端导入。
  - 支持结构：
    - 旧版：`{ 分类: [数组] }`
    - 新版：`{ common: {...}, history: [...], menus: [...] }`
    - 分组版：`{ 分类: { groups: { 子类: [数组] } } }`
- 图片导出
  - “生成图片”将提示词区域导出为透明 PNG（自动提高清晰度）。

## 页面按钮与入口（部分）

- 添加分类：`#add-category-btn`
- 添加标签：`#add-tag-btn`
- 生成图片：`#export-tags-image-btn`
- 下载JSON/上传：`#download-json-btn`
- 导入JSON：`#import-json-btn`
- Dropbox 配置：`#dropbox-config-btn`
- 随机挑选：`#random-pick-btn`
- 存储快照：`#save-prompt-btn`
- 查看历史：`#view-history-btn`
- 重置所有数据：`#reset-all-btn`
- 主题切换：`#theme-toggle`
- 设置/右键菜单配置：`#settings-toggle`

## 数据存储说明

- 主要使用 `localStorage` 持久化：
  - 常用提示词：`STORAGE_KEY`（页面定义的键）
  - 历史记录：`ops_prompt_history`
  - 当前激活分类：`ops_active_cat`
  - 右键自定义菜单：`ops_ctx_menu_items`
  - 记忆子类选择：`LAST_SUBCAT_KEY`
  - 主题：`THEME_KEY`（值为 `light` 或 `dark`）
  - Dropbox 配置：`ops_dbx_key` / `ops_dbx_secret` / `ops_dbx_token` / `ops_dbx_refresh` / `ops_dbx_enabled` / `ops_dbx_filename`
  - 翻译 Token（若使用）：`ops_cy_token`
- 重置功能会清空分类、分组与历史，并保留 Dropbox 配置与文件选择。

安全提示：
- 访问令牌与密钥均保存在浏览器 `localStorage` 中，仅用于本页面交互。请在受信环境中使用并避免公开共享包含敏感信息的导出文件。

## Dropbox 云同步（可选）

- 打开“Dropbox”配置窗口，填写 `App Key / App Secret`，完成 OAuth 登录。
- 登录成功后将保存刷新令牌并获取访问令牌，可进行上传/下载。
- 选择或刷新云端 JSON 文件列表，支持将数据上传到应用目录或从中导入。

说明：
- 上传时对非 ASCII 文件名进行兼容处理：临时文件 + move 接口。
- 下载时 ASCII 文件走标准 `content` 接口；非 ASCII 文件使用临时链接获取。

## 技术栈与依赖

- 纯 HTML/CSS/原生 JavaScript
- 外部依赖：
  - Font Awesome（图标）
  - html2canvas（按需加载，用于区域截图）
- 无打包构建，开箱即用。

## 本地开发/定制

- 直接编辑 `html/index.html`。
- 若需要离线运行：
  - 将 Font Awesome 与 html2canvas 改为本地文件并调整引用路径。
- 自定义右键菜单外链：
  - 菜单项存储于 `ops_ctx_menu_items` 中（localStorage）。
  - URL 由模板构建，支持将标签英文/中文代入。
