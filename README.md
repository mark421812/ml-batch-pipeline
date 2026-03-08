# ml-batch-pipeline

MLOps pipeline-oriented batch processing repository for smart retail hourly demand forecasting (store × product × date × hour).

## Scope
This repo handles offline data lifecycle only:
- raw data extract/load
- cleaning and quality checks
- feature engineering
- modeling base table build
- TFT training/evaluation
- artifact registration/export

## Project Layout
```
ml-batch-pipeline/
├─ configs/
├─ data/
├─ artifacts/
├─ pipelines/
├─ src/
├─ tests/
└─ scripts/
```

## Quick Start
1. Create virtualenv and install dependencies:
   ```bash
   pip install -e .[dev]
   ```
2. Prepare sample/raw data under `data/raw/` or `data/samples/`.
3. Run pipelines in order:
   ```bash
   python pipelines/extract/run_extract.py
   python pipelines/clean/run_clean.py
   python pipelines/feature_build/run_feature_build.py
   python pipelines/modeling/run_modeling_base.py
   python pipelines/training/run_train_tft.py
   python pipelines/evaluation/run_evaluate.py
   python pipelines/register/run_register_artifacts.py
   ```

## Pipeline Stages (MVP)
- **extract**: schema-level validation + raw parquet outputs
- **clean**: de-duplication, type standardization, null handling, DQ flags
- **feature_build**: joins + hourly grid + feature generation
- **modeling**: training/inference base tables
- **training**: TFT dataset prep + model training skeleton
- **evaluation**: core quantile and point forecast metrics
- **register**: copy and index artifacts for serving handoff

## Configuration
- `configs/pipeline.yaml`: stage switches and runtime parameters
- `configs/feature.yaml`: feature toggles and generation settings
- `configs/train.yaml`: training hyperparameters
- `configs/paths.yaml`: all I/O paths

## Testing
```bash
pytest -q
```


## Why `pytest -q`
- `pytest` is the test runner used to verify pipeline modules and prevent regressions.
- `-q` means *quiet mode* (less verbose output), useful in CI and quick local checks.

To run full tests locally:
```bash
pip install -e .[dev]
pytest -q
```

If dependencies are not installed, dependency-heavy tests are skipped by design in this scaffold.

## Notes
- This is **MVP skeleton (v0)** with TODO markers for business-rule completion.
- Intermediate artifacts are persisted as parquet to support rerun/backfill.
