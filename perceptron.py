import numpy as np
import csv

# 識別関数
def identify(w_vec, x_vec):
    y = np.dot(w_vec, x_vec) 
    if y >= 0:
        y = 1
    else:
        y = -1
    return y

# 重みの更新
def update(w_vec, x_vec, rho, t): # rho:学習係数(0 ~ 1), t:ラベル(1 or -1)
    if identify(w_vec, x_vec) * t < 0:
        w_vec = w_vec + rho * t * x_vec
        return w_vec
    else:
        return w_vec

if __name__ ==  "__main__":
    weight = np.array([-1,1,1])
    rho = 0.5

    with open('train.csv', encoding='shift_jis') as f:
    reader = csv.reader(f)
    cnt = 0
    weigth_new = np.array([0,0,0])
    while numpy.linalg.norm(weight - weight_new) < 0.001: # 収束判定
        for train_x in reader:
            weight_new = update(weight, x_train[0:3], rho, x_train[3])
        cnt = cnt + 1
        if cnt == 1000: break
        weight = weight_new

        