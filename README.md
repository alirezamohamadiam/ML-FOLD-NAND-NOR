# Enhanced Version of the ML-FOLD algorithm for Photonic Logic Gates

# 🔬 ML-FOLD Optimizer

**ML-FOLD Optimizer** is a Python module designed to analyze and optimize phase configurations for photonic logic gates (NOR/NAND) based on their predicted output characteristics. It computes a custom metric called `LogicOptScore` to classify configurations as *Optimal* or *Non-Optimal*, using a threshold defined as a fraction of the maximum score.

## 📌 Features

* Supports **NOR** and **NAND** logic gate configurations.
* Automatically computes:

  * `Optimize_R`: Ratio-based metric to evaluate performance.
  * `ZeroStateUniformity`: Measures uniformity in “0” state predictions.
  * `LogicOptScore`: Composite metric to identify optimal configurations.
* Filters out noisy data (NaNs, infinities).
* Classifies configurations into `Optimal` or `Non-Optimal`.
* Outputs summary statistics and classification breakdown.

---

## 🧠 Background

Photonic logic gates, based on phase-encoded inputs and nanophotonic structures, require carefully tuned configurations to operate with high fidelity. The **ML-FOLD** algorithm provides a way to evaluate such configurations using machine learning-predicted outputs, optimizing them without relying solely on physical simulations.

---
![ChatGPT Image May 19, 2025, 02_00_02 PM](https://github.com/user-attachments/assets/25435cfc-1606-42b3-ab77-ade29c482551)


## Project Structure

```
ml_fold_optimizer/
├── data/
│   ├── nor_data.csv        # NOR gate phase configuration data
│   ├── nand_data.csv       # NAND gate phase configuration data
├── src/
│   ├── ml_fold_optimizer.py # Main optimization script
├── README.md               # Project documentation
├── requirements.txt        # Python dependencies
```

## Prerequisites

- Python 3.8+
- Required packages (listed in `requirements.txt`):
  - pandas
  - numpy

## Usage

1. **Ensure data files** are in the `data/` directory (`nor_data.csv` and `nand_data.csv`).
2. **Run the script**:
   ```bash
   python src/ml_fold_optimizer.py
   ```

   The script processes both NOR and NAND datasets, calculates `optimize_R`, applies an 80% threshold of the maximum `optimize_R`, and classifies configurations as **Optimal** or **Non-Optimal**. Results include:
   - A DataFrame with phase angles, output powers, `optimize_R`, and classifications.
   - Maximum `optimize_R`, threshold, and class counts.


## Dataset Format

Each CSV file (`nor_data.csv`, `nand_data.csv`) contains:
- Columns: `phi_a`, `phi_b` (phase angles in degrees), `preds_AB_0`, `preds_A_1B_0`, `preds_A_0B_1`, `preds_AB_1` (normalized output powers for input states).
- Example row for NOR:
  ```
  45,45,0.6,0.6,0.62,0.6
  ```

## Methodology

1. **Load Data**: Reads phase configuration data from CSV files.
2. **Calculate optimize_R**:
   - For NOR: `optimize_R = preds_AB_0 / (preds_A_1B_0 * preds_A_0B_1 * preds_AB_1)`
   - For NAND: `optimize_R = (preds_AB_0 * preds_A_1B_0 * preds_A_0B_1) / preds_AB_1`
3. **Set Threshold**: 80% of the maximum `optimize_R` (configurable).
4. **Classify Configurations**: Labels configurations as **Optimal** (≥ threshold) or **Non-Optimal** (< threshold).
5. **Output Results**: Displays DataFrame and statistics.

## Notes

- The threshold is a visualization aid and can be adjusted via the `threshold_fraction` parameter.
- The code includes error handling for missing files, invalid gate types, and malformed data.
- Future enhancements may include support for additional gate types or alternative threshold methods.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with your suggestions or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Citation

Mohammadi, A., Parandin, F., Karami, P., & Olyaee, S. (2025). Design and Optimization of Optical NAND and NOR Gates Using Photonic Crystals and ML-FOLD Algorithm. under review in Photonics (ISSN 2304-6732)


## Contact

For questions or feedback, please contact [alirezamohamadi@iau.ac.ir](mailto:alirezamohamadi@iau.ac.ir).
