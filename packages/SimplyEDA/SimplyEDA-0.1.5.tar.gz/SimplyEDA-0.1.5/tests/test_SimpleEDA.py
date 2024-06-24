import unittest
import pandas as pd
import numpy as np
from SimplyEDA import remove_outlier, find_specialchar, vif_cal, dups, boxplt_continous, enhance_summary

class TestSimplyEDA(unittest.TestCase):

    def setUp(self):
        # Setup a sample DataFrame for testing
        self.df = pd.DataFrame({
            'A': [1, 2, 2, 4, 5, 6, 7, 8, 9, 10],
            'B': [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            'C': [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
            'D': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        })

    def test_remove_outlier(self):
        lower, upper = remove_outlier(self.df['A'])
        self.assertEqual(lower, -4.0)
        self.assertEqual(upper, 16.0)

    def test_find_specialchar(self):
        # Capture the print output
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        find_specialchar(self.df)
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        self.assertIn('The unique values in A are as below', output)

    def test_vif_cal(self):
        from statsmodels.stats.outliers_influence import variance_inflation_factor
        # Check if function runs without error
        try:
            vif = vif_cal(self.df[['A', 'B', 'C']])
            self.assertIsInstance(vif, pd.DataFrame)
        except Exception as e:
            self.fail(f"vif_cal raised Exception unexpectedly: {e}")

    def test_dups(self):
        # Create a DataFrame with duplicates
        df_with_dups = self.df.append(self.df.iloc[0])
        # Capture the print output
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        dups(df_with_dups)
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        self.assertIn('Number of duplicate rows = 1', output)

    def test_boxplt_continous(self):
        # Check if function runs without error
        try:
            boxplt_continous(self.df[['A', 'B', 'C']])
        except Exception as e:
            self.fail(f"boxplt_continous raised Exception unexpectedly: {e}")

    def test_enhance_summary(self):
        summary = enhance_summary(self.df, custom_percentiles=[5, 95])
        self.assertIsInstance(summary, pd.DataFrame)
        self.assertIn('IQR', summary.columns)
        self.assertIn('LW', summary.columns)
        self.assertIn('UW', summary.columns)
        self.assertIn('Outliers', summary.columns)
        self.assertIn('Duplicates', summary.columns)
        self.assertIn('Missing', summary.columns)
        self.assertIn('Skew', summary.columns)
        self.assertIn('Skew_Category', summary.columns)
        self.assertIn('5%', summary.columns)
        self.assertIn('95%', summary.columns)

if __name__ == '__main__':
    unittest.main()
