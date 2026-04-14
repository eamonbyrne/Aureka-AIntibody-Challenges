# Aurabind: Covid Sequence Design

## 🛠 Installation

```bash
conda create --name aurabind python=3.11
pip3 install aurabind
```

## 📥 Download

```bash
mkdir -p outputs
wget "https://zenodo.org/records/17784985/files/Covid-design-10.pt?download=1" -O outputs/Covid-design-10.pt
```

## 🚀 Inference

```bash
conda activate aurabind
bash predict.sh
```

After running the inference command, a output directory named `./outputs/Covid-design_YYYYMMDD_HHMMSS/` (with timestamp in `YYYYMMDD_HHMMSS` format) will be generated automatically. The predicted sequences are stored in `./outputs/Covid-design_YYYYMMDD_HHMMSS/predictions/predict.pkl`. 

The 10 sequences with the highest scores in this `.pkl` file are the final designed sequences.

## ☁️ Run On Google Colab

Use a GPU runtime in Colab before running the cells below:
`Runtime -> Change runtime type -> GPU`

### 1. Clone the repo and install dependencies

```python
!git clone https://github.com/AurekaBio/Aureka-AIntibody-Challenges.git
%cd /content/Aureka-AIntibody-Challenges

!pip install -q -e .
!pip install -q ml-collections fair-esm biotite rdkit scikit-learn pandas tqdm pyyaml
```

### 2. Download the model checkpoint

```python
!mkdir -p outputs
!wget "https://zenodo.org/records/17784985/files/Covid-design-10.pt?download=1" -O outputs/Covid-design-10.pt
```

### 3. Run inference

Use the non-ESM mini checkpoint on standard Colab. The ESM-backed model loads the 3B ESM encoder during preprocessing and will usually be killed for memory usage on free or lower-memory Colab runtimes.

```python
!python data_preprocess.py

!WANDB_MODE=offline CUDA_VISIBLE_DEVICES=0 PYTHONPATH=. TRIANGLE_MULTIPLICATIVE=torch \
torchrun --standalone --nproc_per_node=1 runners/predict.py \
  --project "Covid-design" \
  --run_name "Covid-design" \
  --base_dir "./outputs" \
  --model_name "protenix_mini_default_v0.5.0" \
  --deterministic_seed True \
  --seed "2025" \
  --dtype "fp32" \
  --max_steps "200" \
  --eval_interval "1" \
  --checkpoint_interval "1" \
  --log_interval "1" \
  --iters_to_accumulate "1" \
  --precompute_esm "False" \
  --num_workers "0" \
  --predict_json_path "./data/Covid/Covid_design" \
  --lr "1e-4" \
  --batchsize "1" \
  --load_params_only "True" \
  --skip_load_optimizer "True" \
  --skip_load_step "True"
```

If you are on a higher-memory runtime and specifically want the ESM-backed model, switch `--model_name` to `protenix_mini_esm_v0.5.0` and set `--precompute_esm "True"`.

### 4. Find or download the output file

```python
import glob
latest_run = sorted(glob.glob("outputs/Covid-design_*"))[-1]
print(f"{latest_run}/predictions/predict.pkl")
```

If you want to download the prediction file directly from Colab:

```python
from google.colab import files
files.download(f"{latest_run}/predictions/predict.pkl")
```
