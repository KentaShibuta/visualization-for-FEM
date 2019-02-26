import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

df = pd.read_csv('mesh05.csv',header=None)
pd.DataFrame(df)
df.columns = ['x', 'y']
print(df)
print(df.at[(0, "y")])
print(df.at[(2, "y")])
plt.scatter(df['x'],df['y'])

for i in range(440):
    if df.at[(i, "x")] < df.at[(i+1, "x")]:
        plt.plot([df.at[(i, "x")], df.at[(i+1, "x")]], [df.at[(i, "y")], df.at[(i+1, "y")]],'k-', lw=2)
for i in range(420):#nnode-n_ynode
    plt.plot([df.at[(i, "x")], df.at[(i+21, "x")]], [df.at[(i, "y")], df.at[(i+21, "y")]],'k-', lw=2)
plt.show()