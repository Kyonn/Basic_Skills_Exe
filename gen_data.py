import csv
import json
import numpy as np

voca = {}

# 辞書の作成
with open('run_moerus.csv') as f:
    reader = csv.reader(f)
    i = 0
    for row in reader:
        for c in row[3]:
            if c not in voca:
                voca[c] = i
                i = i + 1
#    voca_sorted = sorted(voca.items(), key=lambda x:x[1])
#    print(voca_sorted)    

'''
# 教師データの生成
with open('run_moerus.csv') as f:
    reader = csv.reader(f)
    s = ''
#        one_hot = []
#        cnt = 0
    label = {}
    with open('train_data.csv', 'w', encoding='utf-8') as fw:
        writer = csv.writer(fw, lineterminator='\n')
        writer.writerow([len(voca)])
        for row in reader:
            if row[3] != '。':
                s += row[3]
                label[len(s)-1] = 1 # 区切れの判定
            else:
                s += row[3]
#                print(s)
#                cnt += len(s)
#                    one_hot_s = np.zeros((len(s), len(voca)))
#                    for i in range(len(s)):
#                        one_hot_s[i][voca[s[i]]] = 1
#                print(one_hot_s)
                for i in range(len(s)-1):
                    idx_lw = voca[s[i]]
                    idx_rw = voca[s[i+1]]
                    label_c = 1 if i in label else -1
                    train_x = [idx_lw, idx_rw, label_c]
                    writer.writerow(train_x)
#                        print(type(train_x))
                s = ''
                label = {}
#                    break
#        print(cnt)

'''

# テストデータの生成
with open('merous.csv', 'r', encoding='utf-8') as fr:
    reader = csv.reader(fr)
    s = ''
    with open('test_data.csv', 'w', encoding='utf-8') as fw:
        writer = csv.writer(fw)
        for row in reader:
            if row[3] != '。':
                s += row[3]
            else:
                s += row[3]
                for i in range(len(s)-1):
                    idx_lw = voca.get(s[i]) 
                    idx_rw = voca.get(s[i+1])
                    test_x = [idx_lw, idx_rw]
                    writer.writerow(test_x)
                s = ''


'''
# 教師データから文章の復元
with open('train_data.csv', 'r', encoding='utf-8') as fr:
reader = csv.reader(fr)
for row in reader:
#    print(row)
    c = [k for k, v in voca.items() if v == int(row[0])][0]
    print(c, end='')
    if int(row[2]) == 1: print('|', end='')
    if int(row[1]) == voca['。']: print('。\n')
'''

'''                
# 一文字づつone-hotを作る
with open('run_moerus.csv') as f:
    reader = csv.reader(f)
    s = ''
    one_hot = []
#        cnt = 0
    for row in reader:
        if  row[3] != '。':
            s += row[3]
        else:
            s += row[3]
#                print(s)
#                cnt += len(s)
            one_hot_s = np.zeros((len(s), len(voca)))
            for i in range(len(s)):
                one_hot_s[i][voca[s[i]]] = 1
#                print(one_hot_s)
            with open('train_data.csv', 'a', encoding='utf-8') as fw:
                writer = csv.writer(fw, lineterminator='\n')
                writer.writerows(one_hot_s)
            s = ''
#        print(cnt)
'''    

'''
with open('run_moerus.csv') as f:
reader = csv.reader(f)
s = ''
for row in reader:
    if  row[3] != '。':
        s += row[3]
    else:
        s += row[3]
        print(s)
        s = ''
'''

"""
    for i in range(len(tmp)):
        label = 1 if i == len(tmp) - 1 else 0
        if i != len(tmp) - 1:
            output = [1, tmp[i], tmp[i+1], label]
        else:
            output = [1, tmp[i], ]
"""         