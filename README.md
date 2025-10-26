# 🔬 ML-FOLD Optimizer for Photonic Logic Gates
### Meta-Learning and Formula Optimization for Logic Design

<div align="center">

[![DOI](https://img.shields.io/badge/DOI-10.3390%2Fphotonics12060576-blue.svg)](https://doi.org/10.3390/photonics12060576)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Photonics](https://img.shields.io/badge/Journal-Photonics-green.svg)](https://doi.org/10.3390/photonics12060576)

*Official Implementation - Published in Photonics, 2025*

**Dataset Included** | NOR & NAND Gate Optimization

[**Paper**](https://doi.org/10.3390/photonics12060576) | [**Contact**](mailto:alirezamohamadi@iau.ac.ir)

</div>

---


## 🔬 Overview

This repository contains the Python implementation of the **ML-FOLD** (Meta-Learning and Formula Optimization for Logic Design) algorithm for optimizing phase configurations in photonic crystal-based logic gates. The algorithm processes datasets to calculate the `optimize_R` metric, classify configurations as **Optimal** or **Non-Optimal**, and provide comprehensive statistical summaries.

**Supported Logic Gates:**
- **NOR Gate** - Photonic crystal-based NOR logic gate optimization
- **NAND Gate** - Photonic crystal-based NAND logic gate optimization

<div align="center">

![ML-FOLD Algorithm](https://github.com/user-attachments/assets/03fc8bef-cfe0-49c6-be32-c706ef412f70)

*ML-FOLD optimization framework for photonic logic gates*

</div>

---

## 🚀 Quick Start

### Step 1: Clone Repository
```bash
git clone https://github.com/alirezamohamadiam/ML-FOLD-NAND-NOR.git
cd ML-FOLD-NAND-NOR
```

### Step 2: Install Requirements
```bash
pip install -r requirements.txt
```
> **Note:** Python 3.7+ is required

### Step 3: Run Optimizer
```bash
python src/ml_fold_optimizer.py
```

That's it! The script will automatically process both NOR and NAND datasets included in the repository.

## 📊 Dataset Information

### Included Datasets

This repository includes the **complete datasets** used in the published paper:

| File | Description | Location |
|:-----|:------------|:---------|
| `nor_data.csv` | NOR gate phase configurations and output powers | `data/nor_data.csv` |
| `nand_data.csv` | NAND gate phase configurations and output powers | `data/nand_data.csv` |

### Dataset Format

Each CSV file contains the following columns:

| Column | Description | Unit |
|:-------|:------------|:-----|
| `phi_a` | Phase angle A | Degrees (°) |
| `phi_b` | Phase angle B | Degrees (°) |
| `preds_AB_0` | Normalized output power for input state (0,0) | - |
| `preds_A_1B_0` | Normalized output power for input state (1,0) | - |
| `preds_A_0B_1` | Normalized output power for input state (0,1) | - |
| `preds_AB_1` | Normalized output power for input state (1,1) | - |
---
## 📁 Project Structure

```
ml_fold_optimizer/
├── data/
│   ├── nor_data.csv          # NOR gate dataset (included)
│   └── nand_data.csv         # NAND gate dataset (included)
├── src/
│   └── ml_fold_optimizer.py  # Main optimization script
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation (this file)
└── LICENSE                   # MIT License
```

---

## 📚 Citation

If you use this code or dataset in your research, please cite our paper:

```bibtex
@inproceedings{mohammadi2025design,
  title={Design and Optimization of Optical NAND and NOR Gates Using Photonic Crystals and the ML-FOLD Algorithm},
  author={Mohammadi, Alireza and Parandin, Fariborz and Karami, Pouya and Olyaee, Saeed},
  booktitle={Photonics},
  volume={12},
  number={6},
  pages={576},
  year={2025},
  organization={MDPI}
}
```

**Plain Text Citation:**
```
Mohammadi, A., Parandin, F., Karami, P., & Olyaee, S. (2025). Design and Optimization of Optical NAND and NOR Gates Using Photonic Crystals and the ML-FOLD Algorithm. Photonics, 12(6), 576. https://doi.org/10.3390/photonics12060576
```
---


<div align="center">

**⭐ If you find this work useful, please consider giving it a star! ⭐**

Made with ❤️ for Photonic Computing Research

This project is licensed under the MIT License 


</div>
