import pandas as pd
import matplotlib.pyplot as plt
import sys

import numpy as np

def array_info(x):
    print("配列のshape", x.shape)
    print("配列の要素のデータ型", x.dtype)
    if len(x) >=10:
        print("配列の中身（上から10列）\n",x[:10],"\n")
    else:
        print("配列の中身\n",x,"\n")

print('Input node file name >>>>')
f_name_node = input().rstrip() # 可視化するファイル名

# pandasで読み込む場合

df_node = pd.read_csv(f_name_node ,header=None)
nnode = len(df_node)
print('# nnode = ' + str(nnode))
pd.DataFrame(df_node)
df_node.columns = ['node_id', 'x', 'y']
plt.xlabel('x')
plt.ylabel('y')
#plt.title('visualization mesh') # これが有ると画像を見ただけでなんのでグラフなのかわかるので便利だが，論文に貼るときにいらない．
#print(df_node)
#plt.scatter(df_node['x'],df_node['y'])#ここを入れると節点が強調して表示される．

print('Input nbool file name >>>>')
f_name_nbool = input().rstrip() # 可視化するファイル名

df_nbool = pd.read_csv(f_name_nbool ,header=None)
nelem = len(df_nbool)
pd.DataFrame(df_nbool)
df_nbool.columns = ['elem_id', 'matel_id', 'mesh_type', 'local_0', 'local_1', 'local_2', 'local_3']

for i in range(nelem):
    print(i)
    plt.plot([df_node.at[(int(df_nbool.iloc[i][3]), "x")], df_node.at[(int(df_nbool.iloc[i][4]), "x")]], [df_node.at[(int(df_nbool.iloc[i][3]), "y")], df_node.at[(int(df_nbool.iloc[i][4]), "y")]],'k-', lw=0.7)
    plt.plot([df_node.at[(int(df_nbool.iloc[i][4]), "x")], df_node.at[(int(df_nbool.iloc[i][5]), "x")]], [df_node.at[(int(df_nbool.iloc[i][4]), "y")], df_node.at[(int(df_nbool.iloc[i][5]), "y")]],'k-', lw=0.7)
    plt.plot([df_node.at[(int(df_nbool.iloc[i][5]), "x")], df_node.at[(int(df_nbool.iloc[i][6]), "x")]], [df_node.at[(int(df_nbool.iloc[i][5]), "y")], df_node.at[(int(df_nbool.iloc[i][6]), "y")]],'k-', lw=0.7)
    plt.plot([df_node.at[(int(df_nbool.iloc[i][6]), "x")], df_node.at[(int(df_nbool.iloc[i][3]), "x")]], [df_node.at[(int(df_nbool.iloc[i][6]), "y")], df_node.at[(int(df_nbool.iloc[i][3]), "y")]],'k-', lw=0.7)
plt.axes().set_aspect('equal', 'datalim')
plt.show()
'''
df_node = np.loadtxt(f_name_node,
                    delimiter=",",
                    skiprows=0,
                    usecols=(0,1,2)
                    )
#array_info(df_node)

df_nbool = np.loadtxt(f_name_nbool,
                    delimiter=",",
                    skiprows=0,
                    usecols=(0,1,3,4,5,6)
                    )
print(df_nbool.shape[0])
for i in range(int(df_nbool.shape[0])):
    print(i)
    plt.plot([df_node[int(df_nbool[i,2]),1], df_node[int(df_nbool[i,3]),1]], [df_node[int(df_nbool[i,2]),2], df_node[int(df_nbool[i,3]),2]],'k-', lw=0.7)
    plt.plot([df_node[int(df_nbool[i,3]),1], df_node[int(df_nbool[i,4]),1]], [df_node[int(df_nbool[i,3]),2], df_node[int(df_nbool[i,4]),2]],'k-', lw=0.7)
    plt.plot([df_node[int(df_nbool[i,4]),1], df_node[int(df_nbool[i,5]),1]], [df_node[int(df_nbool[i,4]),2], df_node[int(df_nbool[i,5]),2]],'k-', lw=0.7)
    plt.plot([df_node[int(df_nbool[i,5]),1], df_node[int(df_nbool[i,2]),1]], [df_node[int(df_nbool[i,5]),2], df_node[int(df_nbool[i,2]),2]],'k-', lw=0.7)
plt.axes().set_aspect('equal', 'datalim')
plt.show()
'''


