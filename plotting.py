import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

x = range(10)
y = range(10)
label = [1, -1, -1, -1, 1, 1, -1, 1, -1, 1]
mark = [0] * 10
for i in range(len(label)):
    mark[i] = 'o' if label[i] == 1 else 'x'

#for i in range(len(x)):
plt.scatter(x, y, vmin=-1, vmax=1, c=label, cmap=cm.seismic)
plt.show()
