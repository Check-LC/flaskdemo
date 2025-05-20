# 个人生活管理系统 - Web 开发项目规划

## 1. 项目概述

### 1.1 项目背景

这是一个面向 Python 初学者的个人成长项目，旨在通过构建实用的个人生活管理系统 Web 应用来提升编程技能。该系统将帮助用户管理日常任务、记录生活日志，并提供日历功能与外部互动能力。

### 1.2 核心功能

- **任务管理**：记录、分类任务，推荐执行顺序，支持任务执行过程记录和数据统计
- **生活日志**：支持文字、图片、视频的记录，提供时间轴或分类视图
- **日历展示**：对外展示日程安排，允许访客留言（类似工单系统）

### 1.3 学习目标

- 掌握 Python 基础和进阶知识
- 学习 Web 开发（Flask 框架）
- 学习数据库设计与操作
- 理解前后端交互原理
- 培养项目规划和架构设计能力
- 积累实际项目经验

## 2. 技术栈选择

考虑到 Python 初学者的学习曲线，推荐以下技术栈：

### 2.1 后端技术

- **语言**：Python 3.x
- **框架**：Flask
  - 理由：轻量级框架，学习曲线平缓，适合 Python 初学者快速上手
  - 灵活性高，支持"最小可用应用"启动模式（仅需 5 行代码运行 Hello World）
  - 开发反馈快（修改代码自动重载），能快速见到成果，保持学习积极性
- **数据库**：
  - 开发阶段：SQLite（轻量级，无需额外安装服务器）
  - 生产环境：MySQL（可选）
- **ORM**：SQLAlchemy + Flask-SQLAlchemy（简化数据库操作）
- **任务调度**：Flask-APScheduler（用于定时任务和提醒功能）
- **身份验证**：Flask-Login（处理用户会话和认证）

### 2.2 前端技术

- **模板引擎**：Jinja2（Flask 默认模板引擎）
- **CSS 框架**：Bootstrap 5
  - 提供现成的组件和响应式设计，无需深入了解 CSS
- **JavaScript**：基础 JavaScript + jQuery
  - 用于基本的表单验证和简单交互
- **数据可视化**：Chart.js（简单易用的图表库）
- **日历组件**：FullCalendar.js（实现日历视图）

### 2.3 部署方案

- **初期部署**：PythonAnywhere（推荐）
  - 免费套餐支持基础功能（500MB 存储，每日 3 小时 CPU 使用）
  - 简单易用，适合初学者
- **后期部署**：Docker + 云服务器（可选进阶方案）

## 3. 功能模块详细规划

### 3.1 任务管理模块

- **核心功能**：
  - 任务创建、编辑、删除
  - 任务分类（工作、学习、生活等）
  - 任务优先级设置
  - 截止日期和提醒
  - 任务状态跟踪（待办、进行中、已完成）
  - 任务执行计划和笔记
  - 完成后的反思记录
- **算法功能**：

  - 基于优先级、截止日期和预估时间的任务排序
  - 智能推荐每日/每周任务计划
  - 任务完成率和效率统计

- **数据结构**：
  ```python
  class Task:
      id: int
      title: str
      description: str
      category: str
      priority: int  # 1-5
      deadline: datetime
      estimated_time: int  # 分钟
      status: str  # "todo", "in_progress", "done"
      created_at: datetime
      updated_at: datetime
      notes: List[Note]
      subtasks: List[Subtask]
  ```

### 3.2 生活日志模块

- **核心功能**：

  - 日志创建、编辑、删除
  - 支持文本、图片内容
  - 日志分类和标签
  - 时间轴视图
  - 分类视图
  - 搜索和过滤

- **数据结构**：
  ```python
  class Journal:
      id: int
      title: str
      content: str
      category: str
      tags: List[str]
      created_at: datetime
      updated_at: datetime
      media: List[Media]  # 图片
  ```

### 3.3 日历与互动模块

- **核心功能**：

  - 日历视图（日、周、月）
  - 事件创建和管理
  - 公开/私密事件设置
  - 访客留言功能
  - 留言通知和回复

- **数据结构**：
  ```python
  class Event:
      id: int
      title: str
      description: str
      start_time: datetime
      end_time: datetime
      is_public: bool
      created_at: datetime
      updated_at: datetime
      comments: List[Comment]
  ```

## 4. 项目结构设计

```
personal_life_manager/
├── app/                  # 应用主目录
│   ├── __init__.py       # 应用初始化（工厂模式创建Flask实例）
│   ├── config.py         # 配置文件
│   ├── models/           # 数据模型层
│   │   ├── __init__.py
│   │   ├── user.py       # 用户模型
│   │   ├── task.py       # 任务模型
│   │   ├── journal.py    # 日志模型
│   │   └── event.py      # 日历事件模型
│   │
│   ├── routes/           # 路由和视图函数
│   │   ├── __init__.py
│   │   ├── auth.py       # 认证相关路由
│   │   ├── tasks.py      # 任务管理路由
│   │   ├── journals.py   # 日志记录路由
│   │   ├── calendar.py   # 日历相关路由
│   │   └── dashboard.py  # 仪表盘路由
│   │
│   ├── services/         # 业务逻辑层
│   │   ├── __init__.py
│   │   ├── task_service.py
│   │   ├── journal_service.py
│   │   └── calendar_service.py
│   │
│   ├── forms/            # 表单定义
│   │   ├── __init__.py
│   │   ├── auth_forms.py
│   │   ├── task_forms.py
│   │   └── journal_forms.py
│   │
│   ├── static/           # 静态文件
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   │
│   └── templates/        # HTML模板
│       ├── base.html     # 基础模板
│       ├── auth/         # 认证相关模板
│       ├── tasks/        # 任务相关模板
│       ├── journals/     # 日志相关模板
│       └── calendar/     # 日历相关模板
│
├── migrations/           # 数据库迁移文件
│
├── tests/                # 测试代码
│   ├── __init__.py
│   ├── test_models.py
│   └── test_routes.py
│
├── run.py                # 应用启动脚本
├── requirements.txt      # 依赖列表
└── README.md             # 项目说明
```

## 5. 开发路线图

### 阶段 1: 基础搭建（1-2 周）

- 学习 Flask 基础，创建项目结构
- 设置 SQLite 数据库连接
- 实现用户认证系统（注册、登录、密码重置）
- 创建简单的任务管理功能（增删改查）
- 部署到开发环境

**技术要点**:

- Flask 应用初始化与配置
- 使用 Flask-SQLAlchemy 连接数据库
- 使用 Flask-Login 处理用户认证
- 基本的路由和视图函数
- 简单的 HTML 模板和表单

### 阶段 2: 核心功能（2-3 周）

- 完善任务管理，添加分类、标签、优先级等
- 实现日志记录功能（日记、笔记）
- 添加简单的日历视图
- 创建基本仪表盘

**技术要点**:

- 复杂表单处理与验证
- 数据库关系（一对多、多对多）
- 使用 Bootstrap 构建响应式界面
- 基本的 JavaScript 交互

### 阶段 3: 增强功能（2-4 周）

- 添加任务提醒和通知
- 实现更复杂的日历功能，如重复事件
- 增强日志功能，添加模板和标签
- 完善仪表盘，添加简单数据统计

**技术要点**:

- 使用 Flask-APScheduler 实现定时任务
- 集成 FullCalendar.js 实现日历功能
- 使用 Chart.js 实现数据可视化
- 文件上传与处理（图片）

### 阶段 4: 高级功能（3-5 周）

- 添加简单 API 接口（使用 Flask-RESTful）
- 实现数据导入导出
- 添加基本搜索功能
- 优化性能和用户体验
- 部署到生产环境

**技术要点**:

- RESTful API 设计与实现
- 数据序列化与反序列化
- 全文搜索实现
- 性能优化技巧
- 生产环境部署配置
