import pandas as pd
from adtk.data import validate_series
from adtk.detector import SeasonalAD

df = pd.read_csv('data.csv', parse_dates=['timestamp'])
df = validate_series(df.set_index('timestamp'))

print("Performing anomaly detection on the given sample...")
clf = SeasonalAD(freq=100,side='both')
anomalies = clf.fit_detect(df['value'])
print(f"Detected {anomalies.value_counts()[1]} anomalies.")

tna, non_anoms = df.index[anomalies==False].values, df['value'][anomalies==False].values
ta, anoms = df.index[anomalies==True].values, df['value'][anomalies==True].values

import seaborn as sns
import matplotlib.pyplot as plt

sns.set(rc={"grid.color": "#595d61", 'axes.facecolor':'#3d4144'})
cust_cols = {'anomaly' : '#d94c58', 'real' : '#45a7df'}

fig, ax = plt.subplots(figsize=(11.7,8.27))

ax = sns.scatterplot(x=tna,y=non_anoms, color=cust_cols['real'])
ax = sns.scatterplot(x=ta,y=anoms, color=cust_cols['anomaly'])

ax.set_xticklabels([]); ax.set_yticklabels([])
ax.set_title('Identified anomalies on the original data')

plt.savefig('after.pdf', bbox_inches='tight')

print("Please compare the before and after graphs to see identified anomalies.")