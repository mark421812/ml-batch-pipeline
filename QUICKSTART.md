# 快速開始（新電腦）- 簡化版

如果你只想快速在新電腦上開始，按照這 5 個步驟即可。

## 🚀 **5 分鐘快速開始**

### **第 1 步：克隆項目**
```bash
git clone https://github.com/mark421812/ml-batch-pipeline.git
cd ml-batch-pipeline
```

### **第 2 步：創建虛擬環境**
```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

### **第 3 步：安裝依賴**
```bash
pip install --upgrade pip
pip install pandas numpy pyyaml pyarrow pytest pytest-cov ruff
```

### **第 4 步：驗證安裝**
```bash
pytest -q
```

### **第 5 步：開始工作**
```bash
# 更新最新代碼
git pull origin main

# 運行管道
python pipelines/extract/run_extract.py

# 編輯代碼後提交
git add .
git commit -m "你的提交說明"
git push origin main
```

---

## 📖 **需要更多幫助？**

查看 `SETUP.md` 了解完整的設置指南。

---

**就這麼簡單！** 🎉
