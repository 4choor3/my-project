# my-project

> 一个包含前端、后端与 Notebook 练习的 monorepo starter 仓库。

## 项目简介

`my-project` 采用 **monorepo** 结构组织，把三个相对独立的工作区放在同一个仓库中统一管理与协作：

| 工作区 | 技术栈 | 用途 |
| --- | --- | --- |
| `frontend/` | Node.js 26 · pnpm 12.5.1 · Express 5 | 前端服务（当前为基础脚手架，提供 HTTP 服务入口） |
| `backend/` | Python 3.13+ · uv | Python 后端与算法练习脚本集合 |
| `notebooks/` | Jupyter（uv 管理依赖） | 交互式 Notebook 实验与学习 |

仓库已配置 GitHub Actions，对 `frontend/` 与 `backend/` 的改动分别触发对应的 CI 流水线。

## 技术栈

- **前端**：Node.js `26`、包管理器 `pnpm@12.5.1`、Web 框架 `Express ^5.2.1`
- **后端**：Python `>=3.13`、包与虚拟环境管理 `uv`、运行时依赖 `numpy` / `pandas`、开发依赖 `pytest` / `ruff`
- **Notebooks**：Jupyter Notebook，依赖同样由 `uv` 管理
- **CI/CD**：GitHub Actions（`.github/workflows/`）

## 目录结构

```text
my-project/
├── frontend/                 # 前端工作区（pnpm + Express）
│   ├── package.json
│   ├── pnpm-lock.yaml
│   └── .node-version         # 锁定 Node 版本 26
├── backend/                  # 后端工作区（uv + Python）
│   ├── pyproject.toml        # 项目元数据与依赖
│   ├── uv.lock
│   ├── src/backend/          # 业务/练习脚本（中文命名）
│   │   ├── __init__.py       # 暴露 main() 入口
│   │   ├── hello_world.py
│   │   ├── 计算器.py
│   │   ├── 水仙花数.py
│   │   └── ……（共 30+ 个小练习）
│   └── tests/                # pytest 冒烟测试
├── notebooks/                # 交互式 Notebook 工作区（uv 管理）
│   ├── pyproject.toml
│   └── src/notebooks/        # *.ipynb 实验笔记
├── .github/workflows/        # CI：frontend.yml / backend.yml
├── .gitignore
└── README.md
```

## 快速开始

### 环境要求

- Node.js `26`（建议通过 `frontend/.node-version` 指定的版本）
- Python `>=3.13` 与 [`uv`](https://github.com/astral-sh/uv)
- `pnpm@12.5.1`（执行 `corepack enable` 或按 `package.json` 的 `packageManager` 字段自动下载）

### 后端（backend）

```bash
cd backend
uv sync            # 安装依赖并创建 .venv
uv run pytest -v   # 运行测试
uv run backend     # 运行入口（打印 "Hello from backend!"）
```

`backend` 包在 `src/backend/` 下包含一组以中文命名的小练习脚本（如 `计算器.py`、`水仙花数.py`、`斐波那契.py`、`约瑟夫杯.py` 等），可直接 `uv run python src/backend/<脚本名>.py` 运行。

### 前端（frontend）

```bash
cd frontend
pnpm install
pnpm build          # 当前为占位步骤（echo "no build step yet"）
pnpm test           # 当前为占位步骤（echo "no test yet"）
```

启动 HTTP 服务（需补充实际入口，目前 `package.json` 的 `main` 为 `index.js`）：

```bash
pnpm add express    # 依赖已声明
# 在源码中调用 express() 后运行：node index.js
```

### Notebooks

```bash
cd notebooks
uv sync
uv run jupyter lab   # 或 jupyter notebook
```

打开 `src/notebooks/` 下的 `*.ipynb` 即可进行交互式实验。

## 开发工作流

- 提交/推送时，GitHub Actions 会依据改动路径自动触发：
  - 改动 `frontend/**` → `Frontend CI`（pnpm 安装 + 构建）
  - 改动 `backend/**` → `Backend CI`（uv 同步 + pytest）
- 后端代码风格由 `ruff` 管理，测试由 `pytest` 执行。

## License

ISC（详见 `frontend/package.json` 中的 `license` 字段）。
