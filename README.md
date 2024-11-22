# OUC-手势采集工具 ouc-gesture-capturer

# 使用 Use

> 本工具使用`uv`进行项目管理

## 安装 uv Install uv

```bash
# On Windows.
# 在`Powershell`内运行以下命令。
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

```bash
# On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## 运行项目 Run Project
在项目目录下运行以下命令，uv会自动安装项目依赖并运行。

```bash
# On Winodws.
uv run .\run.py
```

```bash
# On macOS and Linux.
uv run ./run.py
```

## 操作指南 Operation Guide

- 按下`c`以捕捉绿色方框内的图像
- 只能通过按下`q`以退出程序，或在命令行窗口中使用`Ctrl+C`

- 捕捉的图像会存放在`./output`下（目录不存在时会自动创建）
- 你需要在`run.py`中更改图像命名参数
  - **手势名称**（不影响训练和部署）：采集的手势名称
  - **手势字母标记**（不影响训练和部署）：
  - **手势数字标记**（重要！与训练和部署相关）：该手势的数字标记，要求与`customize_service.py`中的数字标记保持一致）