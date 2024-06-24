
# SimplyEDA

SimplyEDA is a Python library for simple exploratory data analysis tasks. It provides functions to handle outliers, find special characters, calculate Variance Inflation Factor (VIF), detect duplicates, and visualize continuous data using box plots.

## Installation

You can install SimplyEDA via pip:

```bash
pip install SimplyEDA
```

## Usage

Below are examples of how to use the various functions provided by SimpleEDA.

### Importing the Library

```python
import SimplyEDA as eda
import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 2, 4, 5, 6, 7, 8, 9, 10],
    'B': [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    'C': [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    'D': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
})
```

### remove_outlier

This function removes outliers from a column based on the Interquartile Range (IQR) method.

```python
lower, upper = eda.remove_outlier(df['A'])
print(f"Lower bound: {lower}, Upper bound: {upper}")
```

**Parameters:**
- `col` (pd.Series): The column from which to remove outliers.
- `multiplier` (float): The multiplier for the IQR to define outliers. Default is 1.5.

**Returns:**
- `tuple`: Lower and upper range for outlier detection.

### find_specialchar

This function finds special characters in a DataFrame.

```python
eda.find_specialchar(df)
```

**Parameters:**
- `df` (pd.DataFrame): The DataFrame to check.

**Returns:**
- None

### vif_cal

This function calculates the Variance Inflation Factor (VIF) for each feature in the DataFrame.

```python
eda.vif_cal(df[['A', 'B', 'C']])
```

**Parameters:**
- `input_data` (pd.DataFrame): The DataFrame for which to calculate VIF.

**Returns:**
- None

### dups

This function shows a duplicate summary of a DataFrame.

```python
eda.dups(df)
```

**Parameters:**
- `df` (pd.DataFrame): The DataFrame to check for duplicates.

**Returns:**
- None

### boxplt_continous

This function plots boxplots for all continuous features in the DataFrame.

```python
eda.boxplt_continous(df)
```

**Parameters:**
- `df` (pd.DataFrame): The DataFrame to plot.

**Returns:**
- None

## Example

Here's a complete example of using SimplyEDA with a sample DataFrame:

```python
import SimplyEDA as eda
import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 2, 4, 5, 6, 7, 8, 9, 10],
    'B': [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    'C': [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    'D': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
})

# Remove outliers
lower, upper = eda.remove_outlier(df['A'])
print(f"Lower bound: {lower}, Upper bound: {upper}")

# Find special characters
eda.find_specialchar(df)

# Calculate VIF
eda.vif_cal(df[['A', 'B', 'C']])

# Detect duplicates
eda.dups(df)

# Plot boxplots for continuous features
eda.boxplt_continous(df)
```

## Author

This project was created by M.R.Vijay Krishnan. You can reach me at [vijaykrishnanmr@gmail.com](mailto:vijaykrishnanmr@gmail.com).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
