# ML-FOLD Optimizer for Photonic Logic Gates

This repository contains a Python implementation of the **ML-FOLD** (Meta-Learning and Formula Optimization for Logic Design) algorithm for optimizing phase configurations in photonic crystal-based logic gates (NOR and NAND). The code processes datasets to calculate the `optimize_R` metric, classify configurations as **Optimal** or **Non-Optimal**, and provide statistical summaries.

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

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/ml_fold_optimizer.git
   cd ml_fold_optimizer
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Ensure data files** are in the `data/` directory (`nor_data.csv` and `nand_data.csv`).
2. **Run the script**:
   ```bash
   python src/ml_fold_optimizer.py
   ```

   The script processes both NOR and NAND datasets, calculates `optimize_R`, applies an 80% threshold of the maximum `optimize_R`, and classifies configurations as **Optimal** or **Non-Optimal**. Results include:
   - A DataFrame with phase angles, output powers, `optimize_R`, and classifications.
   - Maximum `optimize_R`, threshold, and class counts.

## Example Output

For the NOR gate:
```
Processing NOR gate...

Results:
   phi_a  phi_b  preds_AB_0  ...  preds_AB_1  optimize_R classification
0     45     45         0.6  ...        0.60    2.688172   Non-Optimal
5     90     90         0.6  ...        0.18   75.757576      Optimal
6     90    180         0.6  ...        0.08   91.463415      Optimal
...

Maximum optimize_R: 91.46341463414633
Threshold: 73.17073170731707
Class counts: {'Non-Optimal': 14, 'Optimal': 2}
```

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

## Contact

For questions or feedback, please contact [your.email@example.com](mailto:your.email@example.com).