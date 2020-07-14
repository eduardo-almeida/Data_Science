import pandas as pd

base = pd.read_csv('credit_data.csv')
base = base.dropna()

# outliers idade
import matplotlib.pyplot as plt
plt.boxplot(base.iloc[:,2], showfliers = True)
outliers_age = base[(base.age < -20)]

# outliers loan
plt.boxplot(base.iloc[:,3])
outliers_loan = base[(base.loan > 13400)]