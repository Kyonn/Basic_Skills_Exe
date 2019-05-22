import csv
import json
import numpy as np

if __name__ ==  "__main__":
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

    # 学習データの生成
    with open('run_moerus.csv') as f:
        reader = csv.reader(f)
        s = ''
        one_hot = []
#        cnt = 0
        with open('train_data.json', 'a', encoding='utf-8') as fw:
            for row in reader:
                if  row[3] != '。':
                    s += row[3]
                else:
                    s += row[3]
                    label = np.zeros(len(s)-1) # 区切れの判定
    #                print(s)
    #                cnt += len(s)
                    one_hot_s = np.zeros((len(s), len(voca)))
                    for i in range(len(s)):
                        one_hot_s[i][voca[s[i]]] = 1
    #                print(one_hot_s)
                    for i in range(len(s)-1):
                        train_x = {'bias': np.ones(len(voca)), 'left_word': one_hot_s[i], 'right_word': one_hot_s[i+1], 'label': label[i]}
                        json.dump(train_x, fw)
                    s = ''
                    break
    #        print(cnt)

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