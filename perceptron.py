import numpy as np
import csv

#識別関数
def identify(w_vec, x_vec):
    y = np.dot(w_vec, x_vec) 
    if y >= 0:
        y = 1
    else:
        y = -1
    return y

#重みの更新
def update(w_vec, x_vec, rho, t): #rho:学習係数(0 ~ 1), t:ラベル(1 or -1)
    if identify(w_vec, x_vec) != t:
        w_vec = w_vec + rho * t * x_vec
    return w_vec

if __name__ ==  "__main__":
    weight = np.array([-1,1,1])
    rho = 0.5

    while abs(weight - weight_new < 0.001):
        weight = weight_new
        weight_new = update(weight, x_train[0:3], rho, x_train[3])
        



    
    



