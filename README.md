<p align="center">
  <img src="https://imghost.online/ib/5Bxw7Ilt1UOo2Os_1754796370.png" alt="ONMMY Logo" width="200" />
</p>

<h1 align="center">OnMMy AA</h1>

> 让每个人都能运行未来。  
> OnMMy 是一个“元操作系统”原型：把人类与智能体的知识、任务、规则、环境抽象成模块，并在统一引擎中组合、运行与模拟。

## 快速开始
```bash
# 方式一：直接运行（无需安装依赖）
python run_onmmy.py run modules/governance/democracy.json

# 方式二：使用 CLI 子命令
python -m onmmy.interface.cli run modules/economy/basic_income.json

# 运行单元测试
python -m unittest discover -s tests -p "test_*.py" -v
```
> 模块使用 JSON 格式，便于零依赖解析；你也可以贡献 YAML 版本（放在同目录），未来会支持自动转换。

## 仓库结构
```
onmmy/                # 核心代码包
modules/              # 可组合的社会/认知/流程模块（100+）
docs/                 # 设计文档与白皮书
tests/                # 单元测试
.github/workflows/    # CI 流程（示例）
run_onmmy.py          # 快速运行脚本
pyproject.toml        # 打包配置（可选）
```
## 设计理念
- **双层操作系统**：机器层（资源/调度）+ 认知层（人类/智能体/规则/知识图谱）。
- **可运行的社会模块**：用数据驱动“如何做事/如何治理/如何学习”。
- **可模拟与可协作**：引擎可以在“沙盒世界”里运行实验，也能输出现实可执行步骤。

## 贡献
见 `docs/contributing.md`。欢迎 PR！

---
_生成时间：2025-08-20T13:20:07.518289Z_
