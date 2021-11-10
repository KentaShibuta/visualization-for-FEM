import matplotlib.pyplot as plt
import numpy as np
import matplotlib.collections as mc

print('Input node file name >>>>')
f_name_node = input().rstrip() # 可視化するファイル名

print('Input nbool file name >>>>')
f_name_nbool = input().rstrip() # 可視化するファイル名

df_node = np.loadtxt(f_name_node,
                    delimiter=",",
                    skiprows=0,
                    usecols=(0,1,2)
                    )

df_nbool = np.loadtxt(f_name_nbool,
                    delimiter=",",
                    skiprows=0,
                    usecols=(0,1,3,4,5,6)
                    )
colors = ['black' for i in range(int(df_nbool.shape[0]))]
linewidths = [0.7 for i in range(int(df_nbool.shape[0]))]

X = np.zeros((int(df_nbool.shape[0]), 5, 2))
for i in range(int(df_nbool.shape[0])):
    X[i, 0, 0] = df_node[int(df_nbool[i,2]),1]
    X[i, 0, 1] = df_node[int(df_nbool[i,2]),2]

    X[i, 1, 0] = df_node[int(df_nbool[i,3]),1]
    X[i, 1, 1] = df_node[int(df_nbool[i,3]),2]

    X[i, 2, 0] = df_node[int(df_nbool[i,4]),1]
    X[i, 2, 1] = df_node[int(df_nbool[i,4]),2]

    X[i, 3, 0] = df_node[int(df_nbool[i,5]),1]
    X[i, 3, 1] = df_node[int(df_nbool[i,5]),2]

    X[i, 4, 0] = df_node[int(df_nbool[i,2]),1]
    X[i, 4, 1] = df_node[int(df_nbool[i,2]),2]

lines = np.array([X[i] for i in range(int(df_nbool.shape[0]))])
lc = mc.LineCollection(lines, colors=colors, linewidths=linewidths)
fig, ax = plt.subplots()
ax.add_collection(lc)

ax.autoscale()
ax.set_aspect('equal')
plt.show()