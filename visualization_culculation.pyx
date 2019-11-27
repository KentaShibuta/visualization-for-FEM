# cython: language_level=3
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

print('Input nbool file name >>>>')
f_name_nbool = input().rstrip() # 可視化するファイル名

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


