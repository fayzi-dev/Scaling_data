Feature scaling is a technique used in data preprocessing to standardize the range of independent variables or features of data. In NumPy, there are several ways to perform feature scaling, including normalization and standardization.

Here are two common methods for feature scaling using NumPy:

### 1. **Min-Max Normalization (Scaling between a specific range, e.g., 0 and 1)**

Min-max normalization transforms the data into a fixed range, typically between 0 and 1, using the following formula:

\[
X' = \frac{X - X_{min}}{X_{max} - X_{min}}
\]

This scales the features to a [0, 1] range.

**Code Example**:
```python
import numpy as np

# Example data
data = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

# Min-Max Normalization
min_val = np.min(data, axis=0)
max_val = np.max(data, axis=0)

scaled_data = (data - min_val) / (max_val - min_val)
print(scaled_data)
```

### 2. **Z-score Standardization (Scaling to mean 0 and variance 1)**

This method transforms the data to have a mean of 0 and a standard deviation of 1. The formula is:

\[
X' = \frac{X - \mu}{\sigma}
\]

where \(\mu\) is the mean and \(\sigma\) is the standard deviation of the feature.

**Code Example**:
```python
import numpy as np

# Example data
data = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

# Z-score Standardization
mean = np.mean(data, axis=0)
std_dev = np.std(data, axis=0)

standardized_data = (data - mean) / std_dev
print(standardized_data)
```

These are basic examples of how to scale features using NumPy. In practice, you'd typically choose a method based on the data's distribution and the model you're working with.