import pandas as pd
import matplotlib.pyplot as plt
import sys

print('Input node file name >>>>')
f_name_node = input() # 可視化するファイル名

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
f_name_nbool = input() # 可視化するファイル名

df_nbool = pd.read_csv(f_name_nbool ,header=None)
nelem = len(df_nbool)
pd.DataFrame(df_nbool)
df_nbool.columns = ['elem_id', 'matel_id', 'mesh_type', 'local_0', 'local_1', 'local_2', 'local_3']

for i in range(nelem):
    plt.plot([df_node.at[(int(df_nbool.iloc[i][3]), "x")], df_node.at[(int(df_nbool.iloc[i][4]), "x")]], [df_node.at[(int(df_nbool.iloc[i][3]), "y")], df_node.at[(int(df_nbool.iloc[i][4]), "y")]],'k-', lw=0.7)
    plt.plot([df_node.at[(int(df_nbool.iloc[i][4]), "x")], df_node.at[(int(df_nbool.iloc[i][5]), "x")]], [df_node.at[(int(df_nbool.iloc[i][4]), "y")], df_node.at[(int(df_nbool.iloc[i][5]), "y")]],'k-', lw=0.7)
    plt.plot([df_node.at[(int(df_nbool.iloc[i][5]), "x")], df_node.at[(int(df_nbool.iloc[i][6]), "x")]], [df_node.at[(int(df_nbool.iloc[i][5]), "y")], df_node.at[(int(df_nbool.iloc[i][6]), "y")]],'k-', lw=0.7)
    plt.plot([df_node.at[(int(df_nbool.iloc[i][6]), "x")], df_node.at[(int(df_nbool.iloc[i][3]), "x")]], [df_node.at[(int(df_nbool.iloc[i][6]), "y")], df_node.at[(int(df_nbool.iloc[i][3]), "y")]],'k-', lw=0.7)

plt.show()
