# AI掘金头条新闻系统 (Toutiao News)

一个基于 FastAPI + Vue3 构建的现代化新闻资讯平台，支持用户注册登录、新闻浏览、收藏和历史记录等功能。

## 项目预览

- **前端地址**: https://tubular-crepe-8c3b04.netlify.app （部署后替换）
- **后端API**: https://toutiao-api.onrender.com （部署后替换）

## 技术栈

### 后端
- **框架**: FastAPI (Python 异步框架)
- **数据库**: MySQL + SQLAlchemy (异步 ORM)
- **缓存**: Redis
- **认证**: JWT Token
- **部署**: Render / Railway

### 前端
- **框架**: Vue 3 + Vite
- **UI组件**: Element Plus / Vant（你实际用的）
- **状态管理**: Pinia / Vuex
- **部署**: Netlify

## 项目结构
<img width="425" height="601" alt="image" src="https://github.com/user-attachments/assets/db4c0ec9-b7e4-4ff1-b6ec-df98851caa68" />



## 功能特性

- [x] 用户注册 / 登录 / 个人信息管理
- [x] 新闻分类浏览
- [x] 新闻列表（支持分页、分类筛选）
- [x] 新闻详情页（浏览量统计）
- [x] 收藏 / 取消收藏
- [x] 浏览历史记录
- [x] Redis 缓存加速热点数据

## 快速启动

### 后端启动

```bash
cd toutiao_backend

# 创建虚拟环境
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux

# 安装依赖
pip install -r requirements.txt

# 启动服务
uvicorn main:app --reload
