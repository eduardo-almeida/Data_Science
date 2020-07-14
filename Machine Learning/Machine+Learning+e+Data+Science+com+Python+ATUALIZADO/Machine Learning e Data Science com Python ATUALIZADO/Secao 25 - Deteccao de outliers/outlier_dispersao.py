import pandas as pd

base = pd.read_csv('credit_data.csv')
base = base.dropna()
base.loc[base.age < 0, 'age'] = 40.92

# income x age
import matplotlib.pyplot as plt
plt.scatter(base.iloc[:,1], base.iloc[:,2])

# income x loan
plt.scatter(base.iloc[:,1], base.iloc[:,3])

# age x loan
plt.scatter(base.iloc[:,2], base.iloc[:,3])

base_census = pd.read_csv('census.csv')

# age x final weight
plt.scatter(base_census.iloc[:, 0], base_census.iloc[:,2])