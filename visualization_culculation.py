import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('mesh08.csv',header=None)
x_element = 40#メッシュの分割数によって変更する
y_element = 40#メッシュの分割数によって変更する
x_node = x_element + 1
y_node = y_element + 1
nnode = x_node * y_node
pd.DataFrame(df)
df.columns = ['x', 'y']
plt.xlabel('x')
plt.ylabel('y')
plt.title('visualization mesh')
#print(df)
#print(df.at[(0, "y")])
#print(df.at[(2, "y")])#検証用
#plt.scatter(df['x'],df['y'])#ここを入れると節点が強調して表示される．

for i in range(nnode - 1):
    if df.at[(i, "x")] < df.at[(i+1, "x")]:
        plt.plot([df.at[(i, "x")], df.at[(i+1, "x")]], [df.at[(i, "y")], df.at[(i+1, "y")]],'k-', lw=0.7)
for i in range(nnode - y_node):
    plt.plot([df.at[(i, "x")], df.at[(i+y_node, "x")]], [df.at[(i, "y")], df.at[(i+y_node, "y")]],'k-', lw=0.7)
plt.show()