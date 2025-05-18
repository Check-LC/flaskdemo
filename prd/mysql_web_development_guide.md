# 个人生活管理系统 - MySQL 版 Web 开发指南

## 1. 技术栈选择与理由

### 1.1 数据库选择：MySQL

### 1.2 推荐技术栈

- **后端框架**：Flask（轻量级，学习曲线平缓）
- **ORM 工具**：SQLAlchemy（简化数据库操作，避免直接编写 SQL）
- **前端基础**：Bootstrap + 基础 JavaScript（快速构建美观界面）
- **开发环境**：Linux（推荐 Ubuntu 或 CentOS，培养 Linux 技能）

## 2. 环境搭建指南

### 2.1 Linux 环境准备

### 2.2 MySQL 安装与配置

### 2.3 Python 环境设置

**推荐使用虚拟环境：**

- 使用`venv`或`virtualenv`创建隔离的 Python 环境
- 学习`pip`包管理，维护`requirements.txt`
- 设置环境变量管理配置信息（如数据库连接字符串）

## 3. 项目初始化步骤

### 3.1 项目结构创建

1. 创建项目目录
2. 设置虚拟环境
3. 安装基础依赖：
   - Flask
   - Flask-SQLAlchemy
   - Flask-Migrate（处理数据库迁移）
   - Flask-Login（用户认证）
   - PyMySQL（MySQL 连接器）
   - python-dotenv（环境变量管理）

### 3.2 数据库连接配置

**MySQL 连接字符串格式：**

```
mysql+pymysql://username:password@host:port/database_name
```

**配置建议：**

- 使用环境变量存储敏感信息（不要硬编码）
- 创建开发/测试/生产三套配置
- 学习使用`.env`文件和`.gitignore`（避免敏感信息提交到版本控制）

### 3.3 数据库迁移设置

**使用 Flask-Migrate 管理数据库架构：**

1. 初始化迁移环境
2. 创建初始迁移脚本
3. 应用迁移到数据库
4. 学习如何进行架构更新和回滚

**迁移的好处：**

- 版本控制数据库架构
- 团队协作更容易
- 安全地进行架构变更
- 在不同环境间复制架构

## 4. 开发指导（按功能模块）

### 4.1 用户认证模块

**学习要点：**

- 密码安全存储（哈希而非明文）
- 会话管理
- 用户注册、登录、注销流程
- 权限控制
- 密码重置功能

**数据库表设计：**

```
users
- id (主键)
- username (唯一)
- email (唯一)
- password_hash
- created_at
- is_active
```

### 4.2 任务管理模块

**学习要点：**

- 数据库关系设计（一对多：用户-任务）
- CRUD 操作实现
- 表单处理
- 数据过滤和排序
- 分页实现

**数据库表设计：**

```
tasks
- id (主键)
- title
- description
- category
- priority
- deadline
- estimated_time
- status
- created_at
- updated_at
- user_id (外键 -> users.id)

task_notes
- id (主键)
- content
- created_at
- task_id (外键 -> tasks.id)
```

### 4.3 日志记录模块

**学习要点：**

- 富文本内容存储
- 图片上传和存储
- 标签系统（多对多关系）
- 搜索功能

**数据库表设计：**

```
journals
- id (主键)
- title
- content
- category
- created_at
- updated_at
- user_id (外键 -> users.id)

tags
- id (主键)
- name (唯一)

journal_tags (关联表)
- journal_id (外键 -> journals.id)
- tag_id (外键 -> tags.id)
- 主键(journal_id, tag_id)

journal_media
- id (主键)
- filename
- file_path
- media_type
- created_at
- journal_id (外键 -> journals.id)
```

### 4.4 日历与事件模块

**学习要点：**

- 日期时间处理
- 前端日历组件集成
- 事件重复规则
- 公开/私密内容控制

**数据库表设计：**

```
events
- id (主键)
- title
- description
- start_time
- end_time
- is_public
- created_at
- updated_at
- user_id (外键 -> users.id)

event_comments
- id (主键)
- content
- author_name
- author_email
- created_at
- event_id (外键 -> events.id)
```

## 5. 开发最佳实践

### 5.1 版本控制

- 使用 Git 管理代码
- 学习基本的分支管理
- 编写有意义的提交信息
- 使用`.gitignore`排除不需要的文件

### 5.2 安全实践

- 不要硬编码敏感信息
- 使用参数化查询（ORM 已处理）
- 验证所有用户输入
- 实施 CSRF 保护
- 设置适当的内容安全策略

### 5.3 代码组织

- 遵循模块化设计
- 使用 Flask 蓝图组织路由
- 分离业务逻辑和视图函数
- 保持函数和类的单一职责
- 编写清晰的文档字符串

### 5.4 调试技巧

- 使用 Flask 调试模式
- 学习使用日志而非 print
- 熟悉常见错误模式
- 使用开发者工具检查网络请求

---

通过这个项目，你将获得全栈开发的基础经验，同时提升 Python、数据库和 Linux 技能。项目采用循序渐进的方式，从基础功能开始，逐步添加复杂特性，确保你能在学习过程中保持成就感和动力。
