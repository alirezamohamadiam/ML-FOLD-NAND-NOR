import pandas as pd
import numpy as np
from pathlib import Path
from typing import Tuple, Dict

class MLFoldOptimizer:
    """A class to optimize phase configurations for photonic logic gates using the ML-FOLD algorithm."""
    
    def __init__(self, data_path: str, gate_type: str, threshold_fraction: float = 0.8):
        """
        Initialize the ML-FOLD optimizer.
        
        Args:
            data_path (str): Path to the CSV data file.
            gate_type (str): Type of logic gate ('NOR' or 'NAND').
            threshold_fraction (float, optional): Fraction of max LogicOptScore for threshold. Defaults to 0.8.
        
        Raises:
            ValueError: If gate_type is invalid or data file is not found.
        """
        if gate_type not in ['NOR', 'NAND']:
            raise ValueError("gate_type must be 'NOR' or 'NAND'")
        self.gate_type = gate_type.upper()
        self.threshold_fraction = threshold_fraction
        self.data_path = Path(data_path)
        self.df = None
        self.max_logic_opt_score = None
        self.threshold = None
        
        if not self.data_path.exists():
            raise FileNotFoundError(f"Data file not found at {self.data_path}")

    def load_data(self) -> None:
        """Load phase configuration data from CSV file."""
        try:
            self.df = pd.read_csv(self.data_path)
            required_columns = ['phi_a', 'phi_b', 'preds_AB_0', 'preds_A_1B_0', 'preds_A_0B_1', 'preds_AB_1']
            if not all(col in self.df.columns for col in required_columns):
                raise ValueError("CSV file must contain required columns: " + ", ".join(required_columns))
        except Exception as e:
            raise RuntimeError(f"Error loading data: {str(e)}")

    def calculate_metrics(self) -> None:
        """Calculate the Optimize_R, ZeroStateUniformity, and LogicOptScore metrics based on gate type."""
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
        
        # Calculate Optimize_R
        if self.gate_type == 'NOR':
            self.df['Optimize_R'] = self.df['preds_AB_0'] / (
                self.df['preds_A_1B_0'] * self.df['preds_A_0B_1'] * self.df['preds_AB_1']
            )
            # Calculate ZeroStateUniformity as standard deviation of logical "0" outputs
            self.df['ZeroStateUniformity'] = self.df[['preds_A_1B_0', 'preds_A_0B_1', 'preds_AB_1']].std(axis=1)
        else:  # NAND
            self.df['Optimize_R'] = (
                self.df['preds_AB_0'] * self.df['preds_A_1B_0'] * self.df['preds_A_0B_1']
            ) / self.df['preds_AB_1']
            # Calculate ZeroStateUniformity as standard deviation of logical "0" outputs
            self.df['ZeroStateUniformity'] = self.df[['preds_AB_0', 'preds_A_1B_0', 'preds_A_0B_1']].std(axis=1)
        
        # Calculate LogicOptScore
        self.df['LogicOptScore'] = self.df['Optimize_R'] / (self.df['ZeroStateUniformity'] + 1e-1)
        
        # Handle infinities and NaNs
        self.df.replace([np.inf, -np.inf], np.nan, inplace=True)
        self.df.dropna(subset=['Optimize_R', 'ZeroStateUniformity', 'LogicOptScore'], inplace=True)

    def set_threshold(self) -> None:
        """Set the classification threshold as a fraction of the maximum LogicOptScore."""
        if self.df is None or 'LogicOptScore' not in self.df.columns:
            raise ValueError("LogicOptScore not calculated. Call calculate_metrics() first.")
        
        self.max_logic_opt_score = self.df['LogicOptScore'].max()
        self.threshold = self.max_logic_opt_score * self.threshold_fraction

    def classify_configurations(self) -> None:
        """Classify configurations as Optimal or Non-Optimal based on the threshold."""
        if self.threshold is None:
            raise ValueError("Threshold not set. Call set_threshold() first.")
        
        self.df['classification'] = self.df['LogicOptScore'].apply(
            lambda x: 'Optimal' if x >= self.threshold else 'Non-Optimal'
        )

    def get_results(self) -> Dict:
        """
        Return optimization results and statistics.
        
        Returns:
            Dict: Contains DataFrame, max LogicOptScore, threshold, and class counts.
        """
        if self.df is None or 'classification' not in self.df.columns:
            raise ValueError("Configurations not classified. Call classify_configurations() first.")
        
        return {
            'dataframe': self.df,
            'max_logic_opt_score': self.max_logic_opt_score,
            'threshold': self.threshold,
            'class_counts': self.df['classification'].value_counts().to_dict()
        }

def run_optimization(data_path: str, gate_type: str) -> Dict:
    """
    Run the ML-FOLD optimization pipeline.
    
    Args:
        data_path (str): Path to the CSV data file.
        gate_type (str): Type of logic gate ('NOR' or 'NAND').
    
    Returns:
        Dict: Optimization results including DataFrame and statistics.
    """
    optimizer = MLFoldOptimizer(data_path, gate_type)
    optimizer.load_data()
    optimizer.calculate_metrics()
    optimizer.set_threshold()
    optimizer.classify_configurations()
    return optimizer.get_results()

if __name__ == "__main__":
    # Example usage
    data_paths = {
        'NOR': 'data/nor_data.csv',
        'NAND': 'data/nand_data.csv'
    }
    
    for gate, path in data_paths.items():
        print(f"\nProcessing {gate} gate...")
        try:
            results = run_optimization(path, gate)
            print("\nResults:")
            print(results['dataframe'])
            print(f"\nMaximum LogicOptScore: {results['max_logic_opt_score']}")
            print(f"Threshold: {results['threshold']}")
            print(f"Class counts: {results['class_counts']}")
        except Exception as e:
            print(f"Error processing {gate}: {str(e)}")
