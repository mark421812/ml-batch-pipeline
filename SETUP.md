# 新電腦環境設置指南

本文檔說明如何在新電腦上克隆項目並設置開發環境。

## 🚀 **第一次在新電腦上設置（5-15 分鐘）**

### **第 1 步：安裝必要的軟件**

#### 1.1 安裝 Git
```bash
# macOS（使用 Homebrew）
brew install git

# Linux（Ubuntu/Debian）
sudo apt-get install git

# Windows
# 從 https://git-scm.com/download/win 下載安裝
```

#### 1.2 安裝 Python 3.9+
```bash
# macOS
brew install python@3.9

# Linux（Ubuntu/Debian）
sudo apt-get install python3.9 python3.9-venv

# Windows
# 從 https://www.python.org/downloads/ 下載安裝
```

#### 1.3 配置 Git（第一次使用）
```bash
# 設置用戶名
git config --global user.name "Your Name"

# 設置郵箱
git config --global user.email "your-email@example.com"

# 驗證配置
git config --global --list
```

### **第 2 步：克隆項目**

```bash
# 進入你想放置項目的目錄
cd ~/Desktop  # 或你選擇的位置

# 克隆倉庫
git clone https://github.com/mark421812/ml-batch-pipeline.git

# 進入項目目錄
cd ml-batch-pipeline
```

### **第 3 步：創建虛擬環境**

```bash
# 創建虛擬環境
python3 -m venv .venv

# 激活虛擬環境
# macOS/Linux:
source .venv/bin/activate

# Windows:
# .venv\Scripts\activate
```

激活後，你應該看到終端提示符前有 `(.venv)` 標記：
```
(.venv) your-username@computer ~ $
```

### **第 4 步：安裝依賴**

```bash
# 升級 pip
pip install --upgrade pip

# 方法 A：安裝基本依賴（推薦用於測試）
pip install pandas numpy pyyaml pyarrow pytest pytest-cov ruff

# 方法 B：安裝所有依賴（包括深度學習，可能耗時 10+ 分鐘）
pip install -e '.[dev]'
```

### **第 5 步：驗證安裝**

```bash
# 測試核心依賴
python -c "import pandas, numpy, yaml; print('✅ 安裝成功！')"

# 運行測試
pytest -q

# 檢查 Git 狀態
git status
```

✅ 如果上面的命令都成功了，恭喜！環境已準備就緒。

---

## 📊 **完整的一鍵設置腳本**

如果你想自動化整個過程，複製並執行以下腳本：

### **macOS/Linux 用戶：**

```bash
#!/bin/bash

# 設置變量
GITHUB_REPO="https://github.com/mark421812/ml-batch-pipeline.git"
PROJECT_NAME="ml-batch-pipeline"
PROJECT_DIR="$HOME/Desktop/$PROJECT_NAME"

echo "🚀 開始設置 ML Batch Pipeline..."

# 第 1 步：克隆倉庫
echo "📥 克隆倉庫..."
cd ~/Desktop
git clone $GITHUB_REPO
cd $PROJECT_DIR

# 第 2 步：創建虛擬環境
echo "🐍 創建虛擬環境..."
python3 -m venv .venv
source .venv/bin/activate

# 第 3 步：安裝依賴
echo "📦 安裝依賴..."
pip install --upgrade pip
pip install pandas numpy pyyaml pyarrow pytest pytest-cov ruff

# 第 4 步：驗證安裝
echo "✅ 驗證安裝..."
python -c "import pandas, numpy, yaml; print('✅ 核心依賴已安裝！')"

# 第 5 步：顯示項目信息
echo ""
echo "🎉 設置完成！"
echo "📍 項目位置: $PROJECT_DIR"
echo "🔧 激活環境: source .venv/bin/activate"
echo "🧪 運行測試: pytest -q"
echo "🚀 運行提取管道: python pipelines/extract/run_extract.py"
```

保存為 `setup.sh`，然後執行：
```bash
bash setup.sh
```

### **Windows 用戶：**

```batch
@echo off
REM 設置變量
set GITHUB_REPO=https://github.com/mark421812/ml-batch-pipeline.git
set PROJECT_NAME=ml-batch-pipeline
set PROJECT_DIR=%USERPROFILE%\Desktop\%PROJECT_NAME%

echo 🚀 開始設置 ML Batch Pipeline...

REM 第 1 步：克隆倉庫
echo 📥 克隆倉庫...
cd %USERPROFILE%\Desktop
git clone %GITHUB_REPO%
cd %PROJECT_DIR%

REM 第 2 步：創建虛擬環境
echo 🐍 創建虛擬環境...
python -m venv .venv
call .venv\Scripts\activate.bat

REM 第 3 步：安裝依賴
echo 📦 安裝依賴...
pip install --upgrade pip
pip install pandas numpy pyyaml pyarrow pytest pytest-cov ruff

REM 第 4 步：驗證安裝
echo ✅ 驗證安裝...
python -c "import pandas, numpy, yaml; print('✅ 核心依賴已安裝！')"

REM 第 5 步：顯示項目信息
echo.
echo 🎉 設置完成！
echo 📍 項目位置: %PROJECT_DIR%
echo 🔧 激活環境: .venv\Scripts\activate
echo 🧪 運行測試: pytest -q
echo 🚀 運行提取管道: python pipelines/extract/run_extract.py
```

保存為 `setup.bat`，然後雙擊執行。

---

## 🔄 **日常開發工作流程**

### **每次開始工作時：**

```bash
# 1. 進入項目目錄
cd /path/to/ml-batch-pipeline

# 2. 激活虛擬環境
source .venv/bin/activate  # macOS/Linux
# 或
.venv\Scripts\activate  # Windows

# 3. 更新最新代碼
git pull origin main

# 4. 開始編寫代碼...
```

### **進行修改後：**

```bash
# 1. 檢查修改了哪些文件
git status

# 2. 添加修改（方法 A：添加所有文件）
git add .

# 或添加特定文件（方法 B）
git add src/utils/config.py

# 3. 提交修改（寫清楚提交說明）
git commit -m "功能：添加新的特徵計算函數"

# 4. 推送到 GitHub
git push origin main
```

### **提交說明的最佳實踐：**

```
# 好的提交說明
git commit -m "功能：實現新的特徵構建邏輯"
git commit -m "修復：解決清理管道中的空值處理問題"
git commit -m "文檔：更新 README 中的快速開始指南"

# 不好的提交說明
git commit -m "update"
git commit -m "fix stuff"
git commit -m "changes"
```

---

## 🔀 **處理多個電腦之間的同步**

### **情況 1：在電腦 B 上獲取電腦 A 的最新代碼**

```bash
# 首先確保你在 main 分支
git checkout main

# 更新遠程信息
git fetch origin

# 檢查是否有新代碼
git log origin/main..main  # 本地領先遠程的提交
git log main..origin/main  # 遠程領先本地的提交

# 拉取遠程最新代碼
git pull origin main

# 如果有衝突，選擇如何解決：
# 方案 A：保留本地版本
git checkout --ours <file>
# 方案 B：使用遠程版本
git checkout --theirs <file>
# 然後提交
git add .
git commit -m "合併遠程更改"
```

### **情況 2：推送你的修改到 GitHub**

```bash
# 確保代碼已提交
git status  # 應該顯示 "nothing to commit"

# 推送
git push origin main
```

### **情況 3：撤銷本地修改**

```bash
# 查看修改了哪些文件
git status

# 撤銷特定文件的修改
git checkout -- <file>

# 或撤銷所有修改
git reset --hard HEAD

# 刪除未追蹤的新文件
git clean -fd
```

---

## 🚨 **常見問題和解決方案**

### **問題 1：無法克隆倉庫**

```
error: could not read Username for 'https://github.com': terminal prompts disabled
```

**解決方案：**
- 使用 SSH 代替 HTTPS
- 或使用 GitHub CLI 認證
- 或使用 Personal Access Token

```bash
# SSH 方式（需要先添加 SSH 密鑰到 GitHub）
git clone git@github.com:mark421812/ml-batch-pipeline.git

# 使用 GitHub CLI
gh auth login
git clone https://github.com/mark421812/ml-batch-pipeline.git
```

### **問題 2：虛擬環境激活失敗**

```bash
# 重新創建虛擬環境
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate  # 或 Windows 的 .venv\Scripts\activate
```

### **問題 3：導入 src 模塊失敗**

如果看到 `ModuleNotFoundError: No module named 'src'`：

```bash
# 確保項目已以開發模式安裝
pip install -e '.'

# 或確保在項目根目錄運行腳本
cd /path/to/ml-batch-pipeline
python pipelines/extract/run_extract.py
```

### **問題 4：Git 要求輸入密碼**

```bash
# 第一次推送時可能要求認證
# 方案 A：使用 Personal Access Token 作為密碼
# （從 https://github.com/settings/tokens 獲取）

# 方案 B：設置 SSH（推薦）
ssh-keygen -t ed25519 -C "your-email@example.com"
# 在 GitHub Settings 中添加公鑰

# 方案 C：使用 GitHub CLI
gh auth login
```

---

## 📋 **快速檢查清單**

新電腦設置完成後，檢查以下項目：

- [ ] Git 已安裝：`git --version`
- [ ] Python 已安裝：`python3 --version`
- [ ] 項目已克隆：`cd ml-batch-pipeline && ls`
- [ ] 虛擬環境已激活：提示符前有 `(.venv)`
- [ ] 依賴已安裝：`python -c "import pandas"`
- [ ] 測試通過：`pytest -q`
- [ ] Git 連接正常：`git status`
- [ ] 可以運行管道：`python pipelines/extract/run_extract.py`

---

## 🆘 **需要幫助？**

如果遇到問題，檢查以下步驟：

1. 運行 `git status` 查看當前狀態
2. 運行 `python -c "import sys; print(sys.path)"` 檢查 Python 路徑
3. 查看 README.md 中的故障排除部分
4. 檢查你的網絡連接（克隆時可能需要）
5. 確保虛擬環境已激活

---

**最後更新**: 2026 年 3 月 8 日
