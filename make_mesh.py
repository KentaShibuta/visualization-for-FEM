import pandas as pd
import numpy as np

# length of culcuration space
x_length = 1.0
y_length = 1.0

# number of elements
x_element = 4
y_element = 4

# number of nodes
x_node = x_element + 1
y_node = y_element + 1
n_node = x_node * y_node

#decide center point
center_x = x_length/2.0
center_y = y_length/2.0
n_center = (n_node -1) / 2

# decide stride of space
dx = x_length / x_element
dy = y_length / y_element

# make DataFrame and　store center point at DataFrame
n = n_center
df = pd.DataFrame([[center_x, center_y, n]], columns=list('XYN'))

# make parallel line and vertical line from center point
x = center_x
y = center_y
for i in range(int(x_node/2)):
    n = n_center
    x = x + dx
    n = n + (i+1)
    df2 = pd.DataFrame([[x, y, n]], columns=list('XYN'))
    df = df.append(df2, ignore_index=True) 
x = center_x
y = center_y
for i in range(int(x_node/2)):
    n = n_center
    x = x - dx
    n = n - (i+1)
    df2 = pd.DataFrame([[x, y, n]], columns=list('XYN'))
    df = df.append(df2, ignore_index=True) 
x = center_x
y = center_y
for i in range(int(y_node/2)):
    n = n_center
    y = y + dx
    n = n + (i+1)*x_node
    df2 = pd.DataFrame([[x, y, n]], columns=list('XYN'))
    df = df.append(df2, ignore_index=True) 
x = center_x
y = center_y
for i in range(int(y_node/2)):
    n = n_center
    y = y - dx
    n = n - (i+1)*x_node
    df2 = pd.DataFrame([[x, y, n]], columns=list('XYN'))
    df = df.append(df2, ignore_index=True) 

# The first quadrant
for j in range(int(y_node/2)):
    for i in range(int(x_node/2)):
        n = n_center
        x = center_x
        y = center_y
        n = n + (i+1) + (j+1)*x_node
        #x = x + ((i+1) * dx)
        #y = y + ((j+1) * dy)
        x = x + ((i+1) * (dx-0.1))
        y = y + ((j+1) * (dy-0.1))
        df2 = pd.DataFrame([[x, y, n]], columns=list('XYN'))
        df = df.append(df2, ignore_index=True) 

# The second quadrant
for j in range(int(y_node/2)):
    for i in range(int(x_node/2)):
        n = n_center
        x = center_x
        y = center_y
        n = n - (i+1) + (j+1)*x_node
        #x = x - ((i+1) * dx)
        #y = y + ((j+1) * dy)
        x = x - ((i+1) * (dx-0.1))
        y = y + ((j+1) * (dy-0.1))
        df2 = pd.DataFrame([[x, y, n]], columns=list('XYN'))
        df = df.append(df2, ignore_index=True) 

# The third quadrant
for j in range(int(y_node/2)):
    for i in range(int(x_node/2)):
        n = n_center
        x = center_x
        y = center_y
        n = n - (i+1) - (j+1)*x_node
        #x = x - ((i+1) * dx)
        #y = y - ((j+1) * dy)
        x = x - ((i+1) * (dx-0.1))
        y = y - ((j+1) * (dy-0.1))
        df2 = pd.DataFrame([[x, y, n]], columns=list('XYN'))
        df = df.append(df2, ignore_index=True) 

# The Fourth quadrant quadrant
for j in range(int(y_node/2)):
    for i in range(int(x_node/2)):
        n = n_center
        x = center_x
        y = center_y
        n = n + (i+1) - (j+1)*x_node
        #x = x + ((i+1) * dx)
        #y = y - ((j+1) * dy)
        x = x + ((i+1) * (dx-0.1))
        y = y - ((j+1) * (dy-0.1))
        df2 = pd.DataFrame([[x, y, n]], columns=list('XYN'))
        df = df.append(df2, ignore_index=True) 


print(df)
df = df.sort_values(by='N') 
print(df)

df.to_csv('export_mesh_data.csv', columns=["X","Y"], header=None, index=None)