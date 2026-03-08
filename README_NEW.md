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

\`\`\`
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
\`\`\`

