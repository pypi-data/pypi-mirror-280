import pandas as pd
import unittest
import matplotlib.pyplot as plt
from prodata.preprocessing import (
    draw_boxplots,
    treat_outliers,
    impute_missing_data,
    encode_categorical_columns
)

class TestDataProc(unittest.TestCase):
    
    def setUp(self):
        # Initialize any resources or setup required for tests
        self.df = pd.DataFrame({
            'A': [1, 2, 3, 4, 5],
            'B': [5, 4, 3, 2, 1],
            'C': [10, 20, None, 40, 50],
            'D': ['A', 'B', 'A', 'C', 'B']
        })
        plt.ioff()  # Turn off interactive mode for matplotlib

    def tearDown(self):
        # Clean up after each test if necessary
        plt.close()  # Close any open plots

    def test_draw_boxplots(self):
        # Test draw_boxplots function
        draw_boxplots(self.df)
        plt.show()  # Display the plot
        # (Note: If running in a non-interactive environment, plt.show() might need to be handled differently)

    def test_treat_outliers(self):
        # Test treat_outliers function
        df_cleaned = treat_outliers(self.df)
        self.assertEqual(df_cleaned.shape, self.df.shape, "Shapes should match after outlier treatment")
        # Add more assertions based on expected behavior

    def test_impute_missing_data(self):
        # Test impute_missing_data function
        df_cleaned = impute_missing_data(self.df)
        self.assertFalse(df_cleaned.isnull().values.any(), "No NaN values should be present after imputation")
        # Add more assertions based on expected behavior

    def test_encode_categorical_columns(self):
        # Test encode_categorical_columns function with 'label' method
        df_encoded = encode_categorical_columns(self.df, method='label')
        
        # Assertions to verify encoding
        self.assertIn('D_encoded', df_encoded.columns, "'D_encoded' column should be created")
        self.assertEqual(df_encoded['D_encoded'].dtype, 'int64', "'D_encoded' column should have integer dtype")
        self.assertTrue(all(df_encoded['D_encoded'] >= 0), "Labels should be non-negative integers")
        
        # Check that original columns are not modified
        for col in ['A', 'B', 'C', 'D']:
            self.assertIn(col, df_encoded.columns, f"{col} column should be present in df_encoded")

if __name__ == '__main__':
    unittest.main()
