from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = [0, 1, 1, 0]
y = [0, 0, 1, 1]
z = [0, 0, 0, 0]

ax.scatter(x, y, z, marker='o',color='b');

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

x.append(0)
y.append(0)
z.append(0)


ax.plot(x,y,z, color='r')


plt.show()