Although Pandas does not provide dedicated scaling functions, you can scale data using basic operations on DataFrames.
import pandas as pd

# Sample DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# Min-Max scaling using Pandas
df_scaled = (df - df.min()) / (df.max() - df.min())

# Z-score normalization (standardization)
df_standardized = (df - df.mean()) / df.std()
