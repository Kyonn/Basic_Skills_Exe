import numpy as np
import csv
import matplotlib.pyplot as plt

# 識別関数
def identify(w_vec, x_vec):
    y = 0
    for i in range(3):
        y += np.dot(w_vec[i], x_vec[i]) 
    if y >= 0:
        y = 1
    else:
        y = -1
    return y

# 重みベクトルの更新
def update(w_vec, x_vec, rho, t): # rho:学習係数(0 ~ 1), t:ラベル(1 or -1)
    if identify(w_vec, x_vec) * t < 0:
        for i in range(3):
            w_vec[i] = w_vec[i] + rho * t * x_vec[i]
        return w_vec
    else:
        return w_vec

# 入力データの生成
def gen_input(l): # l:教師データの辞書のサイズ
    bias = np.ones(l)
    train_x = []
    with open('train_data.csv', 'r', encoding='utf-8') as fr:
        reader = csv.reader(fr)
        header = next(reader)
        for row in reader:
            x_lw = np.zeros(l)
            x_rw = np.zeros(l)
            x_lw[int(row[0])] = 1
            x_rw[int(row[1])] = 1
            train_x.append([bias, x_lw, x_rw, int(row[2])])
    return train_x

# テストデータの生成
def gen_test(l): # l:教師データの辞書のサイズ
    bias = np.ones(l)
    test_x = []
    with open('test_data.csv', 'r', encoding='utf-8') as fr:
        reader = csv.reader(fr)
        for row in reader:
            x_lw = np.zeros(l)
            x_rw = np.zeros(l)
            x_lw[int(row[0])] = 1
            x_rw[int(row[1])] = 1
            test_x.append([bias, x_lw, x_rw])
    return test_x

# 重みベクトルの初期化
def init_weight(l): # l:教師データの辞書のサイズ
    wb = np.ones(l)
    wl = np.ones(l)
    wr = np.ones(l)
    init_w = [wb, wl, wr]
    return init_w

# 教師データの辞書サイズの取得
def voca_size():
    length = 0
    with open('train_data.csv', 'r', encoding='utf-8') as fr:
        reader = csv.reader(fr)
        length = next(reader)[0]
    return int(length)

def plot_data():
    with open('train_data.csv', 'r', encoding='utf-8') as fr:
        reader = csv.reader(fr)
        header = next(reader)
        for row in reader:
            if row[2] == 1:
                plt.scatter(int(row[0]), int(row[1]), s=300, c='b')
            else:
                plt.scatter(int(row[0]), int(row[1]), s=300, c='r')
        plt.show()



if __name__ ==  "__main__":

    # 学習部
    weight = init_weight(voca_size())
    rho = 0.2
    train_x = gen_input(voca_size())

    cnt = 0
    chk = np.zeros(len(train_x))
#    weigth_new = np.array([0,0,0])
#    while numpy.linalg.norm(weight - weight_new) < 0.001: # 収束判定
    while cnt < 1: # 更新の回数制限
        for i in range(len(train_x)):
            weight = update(weight, train_x[i][0:3], rho, train_x[i][3])
        cnt = cnt + 1
#        weight = weight_new
#    print(weight)

    # 実験部
    test_x = gen_test(voca_size())
'''
    with open('merous.csv', 'r', encoding='utf-8') as fr:
        reader = csv.reader(fr)
        i = 0
        for row in reader:
            for c in row[3]:
                print(c, end='')
                if identify(weight, test_x[i]) == 1: print('|', end='')
                if c == '。': print('\n')
                i = i + 1
'''

plot_data()

    



            




        