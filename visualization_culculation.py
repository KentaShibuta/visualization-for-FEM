import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

df = pd.read_csv('filename.csv',header=None)
df.columns = ['X', 'Y']
print(df)#勝手に行番号と列番号を指定してくれる．
plt.scatter(df['X'],df['Y'])
plt.show()