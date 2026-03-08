# 智慧零售時間序列預測 - 批量處理管道

一個面向 MLOps 的批量處理倉庫，用於智慧零售的每小時需求預測（店鋪 × 產品 × 日期 × 小時）。

## 🎯 項目範圍

本倉庫處理離線數據生命週期：

- 原始數據提取/加載
- 數據清理與質量檢查
- 特徵工程
- 建模基表構建
- TFT 模型訓練/評估
- 工件註冊/導出

## 📁 項目結構

```
ml-batch-pipeline/
├─ configs/              # 配置文件
├─ data/                 # 數據目錄
│  ├─ raw/              # 原始數據
│  ├─ clean/            # 清理後的數據
│  ├─ feature/          # 特徵工程結果
│  ├─ modeling/         # 建模基表
│  └─ samples/          # 示例數據
├─ artifacts/           # 工件輸出
│  ├─ checkpoints/      # 模型檢查點
│  ├─ metadata/         # 元數據
│  └─ reports/          # 評估報告
├─ pipelines/           # 管道代碼
├─ src/                 # 源代碼
├─ tests/               # 測試代碼
└─ scripts/             # Shell 腳本
```

## 🔄 數據流程圖

```
┌─────────────────────────────────────────────────────────────────────┐
│                     智慧零售需求預測數據流                           │
└─────────────────────────────────────────────────────────────────────┘

              🔵 EXTRACT（提取）
                     ↓
       提取原始數據 → 模式驗證 → 保存 Parquet
       ├─ fact_hourly_sales（銷售事實表）
       ├─ fact_store_traffic（店鋪流量）
       ├─ fact_weather_env（天氣環境）
       ├─ fact_promotions（促銷事實）
       ├─ dim_product（產品維度）
       ├─ dim_store（店鋪維度）
       └─ dim_calendar（日期維度）
                     ↓
              🟢 CLEAN（清理）
                     ↓
      去重 → 類型標準化 → 空值處理 → 質量檢查
                     ↓
          🟡 FEATURE BUILD（特徵構建）
                     ↓
    數據連接 → 時間網格擴展 → 特徵生成 → 特徵表
                     ↓
            🟠 MODELING（建模）
                     ↓
    訓練集/驗證集/測試集 → 時間序列分割
                     ↓
            🔴 TRAINING（訓練）
                     ↓
    TFT 模型 → 超參數優化 → 模型權重保存
                     ↓
          🟣 EVALUATION（評估）
                     ↓
    預測 → 評估指標（MAE, RMSE, MAPE） → 生成報告
                     ↓
            ⚫ REGISTER（註冊）
                     ↓
    導出工件 → 準備部署 → 模型索引
                     ↓
              📊 輸出結果
    ├─ 清理數據（data/clean/）
    ├─ 特徵表（data/feature/）
    ├─ 訓練模型（artifacts/checkpoints/）
    ├─ 評估報告（artifacts/reports/）
    └─ 部署配置（artifacts/metadata/）
```

## 🔧 系統要求

### 環境要求

- **Python**: 3.9 或更高版本
- **操作系統**: macOS、Linux 或 Windows
- **內存**: 至少 4GB RAM（訓練時推薦 8GB+）
- **磁盤空間**: 至少 10GB（用於數據和工件）

### Python 依賴

```
核心數據處理：
- pandas >= 2.0          # 數據操作和分析
- numpy >= 1.24          # 數值計算
- pyarrow >= 14.0        # Parquet 文件操作

配置管理：
- pyyaml >= 6.0          # YAML 配置文件解析

深度學習（可選，用於訓練）：
- torch >= 2.0,<2.2      # PyTorch 框架
- pytorch-lightning >= 2.0  # Lightning 訓練器
- pytorch-forecasting >= 1.0 # 時間序列模型

機器學習和優化：
- optuna >= 3.0          # 超參數優化
- lightgbm >= 4.0        # 梯度提升模型

測試和開發：
- pytest >= 7.0          # 測試框架
- pytest-cov >= 4.0      # 代碼覆蓋率
- ruff >= 0.4            # Python 代碼檢查工具
```

## 🚀 快速開始

### 1️⃣ 檢查 Python 版本

```bash
python3 --version  # 應該是 3.9 或更高
```

### 2️⃣ 安裝 uv（推薦）

```bash
# macOS/Linux:
curl -LsSf https://astral.sh/uv/install.sh | sh

# 或使用 Homebrew:
brew install uv

# 驗證安裝:
uv --version
```

### 3️⃣ 進入項目目錄

```bash
cd /path/to/ml-batch-pipeline
```

### 4️⃣ 創建虛擬環境並安裝依賴

**方法 A：使用 uv（推薦 - 更快）**

```bash
# 創建虛擬環境並安裝所有依賴
uv sync --all-extras
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

**方法 B：使用標準 pip**

```bash
# 創建虛擬環境
python3 -m venv .venv

# 激活虛擬環境
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 升級 pip
pip install --upgrade pip

# 以開發模式安裝項目
pip install -e '.[dev]'
```

### 5️⃣ 驗證安裝

```bash
# 測試核心依賴
python -c "import pandas, numpy, yaml; print('✅ 安裝成功！')"

# 運行測試
pytest -q
```

### 6️⃣ 準備數據

將你的原始數據放在以下位置：

```
data/raw/       # 放置原始數據
data/samples/   # 或放置示例數據
```

數據格式：

- CSV 或 Parquet 格式
- 包含銷售、流量、天氣數據
- 詳見 `configs/paths.yaml` 配置

### 7️⃣ 運行管道

按順序執行管道：

```bash
# 🔵 提取：讀取並驗證原始數據
python pipelines/extract/run_extract.py

# 🟢 清理：數據清理和質量檢查
python pipelines/clean/run_clean.py

# 🟡 特徵構建：生成特徵
python pipelines/feature_build/run_feature_build.py

# 🟠 建模：準備訓練數據
python pipelines/modeling/run_modeling_base.py

# 🔴 訓練：訓練 TFT 模型（可選 - 需要 torch）
python pipelines/training/run_train_tft.py

# 🟣 評估：評估模型性能
python pipelines/evaluation/run_evaluate.py

# ⚫ 註冊：導出工件
python pipelines/register/run_register_artifacts.py
```

或使用 Shell 腳本：

```bash
bash scripts/run_extract.sh
bash scripts/run_clean.sh
bash scripts/run_feature_build.sh
bash scripts/run_modeling_base.sh
bash scripts/run_train.sh
bash scripts/run_evaluate.sh
```

### 8️⃣ 檢查結果

輸出文件會保存到：

```
data/clean/              # 清理後的數據
data/feature/            # 特徵工程結果
data/modeling/           # 訓練/推理基表
artifacts/reports/       # 評估報告
artifacts/checkpoints/   # 模型檢查點
```

## 📊 管道階段詳解


| 階段                       | 功能                   | 輸入          | 輸出             |
| -------------------------- | ---------------------- | ------------- | ---------------- |
| **Extract** 提取           | 讀取和驗證原始數據     | 原始數據文件  | Parquet 格式數據 |
| **Clean** 清理             | 去重、標準化、空值處理 | 原始數據      | 清理後的數據     |
| **Feature Build** 特徵構建 | 生成時間序列特徵       | 清理數據      | 特徵表           |
| **Modeling** 建模          | 分割數據集             | 特徵表        | 訓練/驗證/測試集 |
| **Training** 訓練          | 訓練 TFT 模型          | 訓練集        | 模型權重         |
| **Evaluation** 評估        | 計算評估指標           | 模型 + 測試集 | 評估報告         |
| **Register** 註冊          | 導出工件               | 模型 + 報告   | 部署包           |

## ⚙️ 配置文件

- `configs/pipeline.yaml`: 管道開關和運行參數
- `configs/feature.yaml`: 特徵開關和生成設置
- `configs/train.yaml`: 訓練超參數
- `configs/paths.yaml`: 所有 I/O 路徑

## 🧪 測試

### 運行測試

```bash
# 激活虛擬環境
source .venv/bin/activate

# 運行所有測試（安靜模式）
pytest -q

# 詳細輸出
pytest -v

# 運行特定測試文件
pytest tests/test_clean.py -v

# 生成覆蓋率報告
pytest --cov=src tests/
```

### 為什麼使用 `pytest -q`？

- `pytest` 是測試運行器，用於驗證管道模塊並防止回歸
- `-q` 表示安靜模式，減少冗長輸出
- 未安裝重型依賴的測試會自動跳過

## 🔧 故障排除

### 虛擬環境問題

**問題**：`python: command not found`

```bash
# 解決方案：使用 python3
python3 -m venv .venv
source .venv/bin/activate
```

**問題**：`ModuleNotFoundError: No module named 'pandas'`

```bash
# 解決方案：重新安裝依賴
pip install --upgrade pip
pip install -e '.[dev]'
```

**問題**：macOS Intel 上 PyTorch 安裝失敗

```bash
# 解決方案：使用兼容版本
pip install 'torch>=2.0,<2.2'
```

### 運行管道問題

**問題**：`No data in data/raw/`

```bash
# 解決方案：添加示例數據或配置路徑
ls data/samples/
```

**問題**：管道因內存不足而崩潰

```bash
# 檢查可用內存
free -h        # Linux
vm_stat        # macOS

# 修改管道代碼以分批處理
```

## Environment Variables (Optional)

Set these to customize behavior:

```bash
export ML_BATCH_DEBUG=1              # Enable debug logging
export ML_BATCH_DATA_PATH=/custom/data  # Override data path
export ML_BATCH_ARTIFACTS_PATH=/custom/artifacts  # Override artifacts path
```

## Performance Notes

- **torch/pytorch-lightning**: Heavy packages, may take 5-10 minutes to install on first run
- **Feature engineering**: Processing full dataset may take 30+ minutes depending on size
- **Model training**: TFT training can take 1-2 hours for full dataset
- **Disk usage**: Expect 5-20GB of intermediate artifacts

Use `data/samples/` subset for quick testing and development.

## Common Commands Reference

```bash
# Activate environment
source .venv/bin/activate

# Deactivate environment
deactivate

# Install additional package
pip install package-name

# List installed packages
pip list

# Update all packages
pip install --upgrade -r requirements.txt

# Remove virtual environment (careful!)
rm -rf .venv
```

## Project Notes

- This is **MVP skeleton (v0)** with TODO markers for business-rule completion
- Intermediate artifacts are persisted as parquet to support rerun/backfill
- All paths configurable via `configs/paths.yaml`
- Data flows through stages: `raw` → `clean` → `feature` → `modeling` → `artifacts`

## Next Steps

1. ✅ Install dependencies
2. ✅ Prepare sample data in `data/samples/`
3. ✅ Run `pytest -q` to verify setup
4. → Run extract pipeline: `python pipelines/extract/run_extract.py`
5. → Run remaining pipelines in order
6. → Check results in `artifacts/reports/`

## Support

For issues or questions:

1. Check the Troubleshooting section above
2. Verify Python version: `python --version`
3. Check virtual environment is activated: `which python` should show `.venv/bin/python`
4. Review log files in project directory
5. Run tests to identify which component failed
