import numpy as np

train_x = []

bias = np.array([1, 1])
lw = np.array([1, 0])
rw = np.array([0, 1])
label = 1

train_x.append([bias, lw, rw, label])
print(train_x)

wb = np.array([1, 1])
wl = np.array([5, 1])
wr = np.array([3, 3])

weight = [wb, wl, wr]
print(weight)

sign = 0
for i in range(len(train_x)):
    for j in range(3):
      sign += np.dot(train_x[i][j], weight[j])

print(sign)
