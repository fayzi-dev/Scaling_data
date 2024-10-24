import pandas as pd

# Sample DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# Min-Max scaling using Pandas
df_scaled = (df - df.min()) / (df.max() - df.min())
print(df_scaled)
    #      A    B
    # 0  0.0  0.0
    # 1  0.5  0.5
    # 2  1.0  1.0
# Z-score normalization (standardization)
df_standardized = (df - df.mean()) / df.std()
print(df_standardized)
    #     A    B
    # 0 -1.0 -1.0
    # 1  0.0  0.0
    # 2  1.0  1.0