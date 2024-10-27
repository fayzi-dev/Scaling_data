### 1. StandardScaler
from sklearn.preprocessing import StandardScaler
import numpy as np

# Sample data
data = np.array([[10, 200], [15, 300], [20, 400], [25, 500]])

# Initialize the StandardScaler
scaler = StandardScaler()

# Fit and transform the data
standardized_data = scaler.fit_transform(data)

print("Standardized Data:\n", standardized_data)
    # output :Standardized Data:
    #  [[-1.34164079 -1.34164079]
    #  [-0.4472136  -0.4472136 ]
    #  [ 0.4472136   0.4472136 ]
    #  [ 1.34164079  1.34164079]]
# To transform new data with the same scaler
new_data = np.array([[30, 600]])
transformed_new_data = scaler.transform(new_data)
print("Standardized New Data:\n", transformed_new_data)
    # output :
    # Standardized New Data:
    #  [[2.23606798 2.23606798]]


### 2. MinMaxScaler

from sklearn.preprocessing import MinMaxScaler
import numpy as np

# Sample data
data = np.array([[10, 200], [15, 300], [20, 400], [25, 500]])

# Initialize the MinMaxScaler with default range [0, 1]
scaler = MinMaxScaler()

# Fit and transform the data
normalized_data = scaler.fit_transform(data)

print("Normalized Data:\n", normalized_data)
    # Normalized Data:
    #  [[0.         0.        ]
    #  [0.33333333 0.33333333]
    #  [0.66666667 0.66666667]
    #  [1.         1.        ]]
# To transform new data with the same scaler
new_data = np.array([[30, 600]])
transformed_new_data = scaler.transform(new_data)
print("Normalized New Data:\n", transformed_new_data)
    # Normalized New Data:
    #  [[1.33333333 1.33333333]]

### 3. RobustScaler؛
from sklearn.preprocessing import RobustScaler
import numpy as np

# Sample data with an outlier
data = np.array([[10, 200], [15, 300], [20, 400], [1000, 500]])  # Outlier in the first column

# Initialize the RobustScaler
scaler = RobustScaler()

# Fit and transform the data
robust_scaled_data = scaler.fit_transform(data)

print("Robust Scaled Data:\n", robust_scaled_data)
    # Robust Scaled Data:
    #  [[-0.02985075 -1.        ]
    #  [-0.00995025 -0.33333333]
    #  [ 0.00995025  0.33333333]
    #  [ 3.91044776  1.        ]]
# To transform new data with the same scaler
new_data = np.array([[30, 600]])
transformed_new_data = scaler.transform(new_data)
print("Robust Scaled New Data:\n", transformed_new_data)
    # Robust Scaled New Data:
    #  [[0.04975124 1.66666667]]