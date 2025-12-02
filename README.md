# Aurabind: Covid Sequence Design

## 🛠 Installation

```bash
conda create --name aurabind python=3.11
pip3 install aurabind
```

## 📥 Download

```bash
wget "https://zenodo.org/records/17784985/files/Covid-design-10.pt?download=1" -O outputs/Covid-design-10.pt
```

## 🚀 Inference

```bash
conda activate aurabind
bash predict.sh
```

After running the inference command, a output directory named `./outputs/Covid-design_YYYYMMDD_HHMMSS/` (with timestamp in `YYYYMMDD_HHMMSS` format) will be generated automatically. The predicted sequences are stored in `./outputs/Covid-design_YYYYMMDD_HHMMSS/predictions/predict.pkl`. 

The 10 sequences with the highest scores in this `.pkl` file are the final designed sequences.