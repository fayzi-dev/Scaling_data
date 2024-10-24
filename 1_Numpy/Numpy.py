import numpy as np

#  Create Example data
data = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
# 1. Min-Max Normalization (Scaling between a specific range, e.g., 0 and 1)

min_val = np.min(data, axis=0)
max_val = np.max(data, axis=0)

scale_data = (data - min_val) / (max_val - min_val)
print(scale_data)
    # [[0.  0.  0. ]
    #  [0.5 0.5 0.5]
    #  [1.  1.  1. ]]
    
# 2. Z-score Standardization (Scaling to mean 0 and variance 1)
mean = np.mean(data, axis=0)
std_dev = np.std(data, axis=0)

standardized_data = (data - mean) / std_dev
print(standardized_data)
    # [[-1.22474487 -1.22474487 -1.22474487]
    #  [ 0.          0.          0.        ]
    #  [ 1.22474487  1.22474487  1.22474487]]