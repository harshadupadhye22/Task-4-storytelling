import pandas as pd
from scipy.stats import ttest_ind

df = pd.read_csv("cleaned_online_retail.csv")

west = df[df['Region'] == 'West']['Total Sales']
others = df[df['Region'] != 'West']['Total Sales']

t_stat, p_value = ttest_ind(west, others)

print("T-Statistic:", t_stat)
print("P-Value:", p_value)

if p_value < 0.05:
    print("Statistically significant difference")
else:
    print("No significant difference")