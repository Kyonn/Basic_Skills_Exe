import numpy as np
import csv


def identify(w_vec, x_vec):
    y = np.dot(w_vec, x_vec): 
    if y >= 0:
        y = 1
    else:
        y = -1
    return y

def update(w_vec, x_vec, rho):
    if identify(w_vec, x_vec) < 0:
        w_vec = w_vec + rho * t * x_vec
        return w_vec
    else:
        return w_vec

if __name__ ==  "__main__":
    weight = np.array([0,0,0])
    

