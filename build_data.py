from datetime import datetime, timedelta
import numpy as np
import pandas as pd

# Mock Vibration Data
times, vibx = [], []
sensordata = []

nowtime = datetime.now()
fullrang = 800
num_anom = 50

for ct in range(fullrang):
    times.append(str((nowtime+timedelta(minutes=1*ct)).strftime('%Y-%m-%dT%H:%M:%SZ')))
    vibx.append(np.around(np.sin(np.pi*ct*0.02) + np.random.normal(0,0.025),4))
    # Add a factor that leads to an uncommon event, controlled by the t-parameter
    if 500 < ct <= 500+num_anom//2:
        vibx[-1] = 0.001*(ct-500)**2 - 0.0005*(ct-500) + 0.02
    elif 500+num_anom//2 < ct <= 500+num_anom:
        vibx[-1] = 0.001*(500+num_anom-ct)**2 - 0.0005*(500+num_anom-ct) + 0.02

    sensordatum = {'timestamp' : times[-1], 'value' : vibx[-1]}
    sensordata.append(sensordatum)
    
print(f"Successfully generated {fullrang} datapoints with {num_anom} anomalies.")

pd.DataFrame(sensordata).to_csv('data.csv',index=False)

import seaborn as sns
import matplotlib.pyplot as plt

sns.set(rc={"grid.color": "#595d61", 'axes.facecolor':'#3d4144'})
cust_cols = {'anomaly' : '#d94c58', 'real' : '#45a7df', 'expected' : 'yellow', 'errors' : 'white'}

fig, ax = plt.subplots(figsize=(11.7,8.27))

ax = sns.scatterplot(x=range(len(vibx)),y=vibx, color=cust_cols['real'])
ax.set_xticklabels([]); ax.set_yticklabels([])
ax.set_title('Original data used for anomaly detection')

plt.savefig('before.pdf', bbox_inches='tight')
plt.show()