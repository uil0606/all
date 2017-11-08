import pandas as pd
import numpy as np
from numpy import median,mean
from sklearn.linear_model import LogisticRegression


def train_test_set(df, per, seed=1234):
    s0 = df[df['y'] == 0]
    s1 = df[df['y'] == 1]
    training0 = s0.sample(frac=per, random_state=seed, axis=0)
    training1 = s1.sample(frac=per, random_state=seed, axis=0)
    testing0 = s0.drop(training0.index, axis=0)
    testing1 = s1.drop(training1.index, axis=0)
    training_set = pd.concat([training0, training1])
    testing_set = pd.concat([testing0, testing1])
    return training_set, testing_set


def resample(dataset, para1, seed=1234):
    num = len(dataset[dataset['y'] == 0])
    dataset_y0 = dataset[dataset['y'] == 0]
    dataset_y1 = dataset[dataset['y'] == 1]
    y0_set = dataset_y0.sample(n=int(para1*num), replace=True, random_state=seed, axis=0)
    y1_set = dataset_y1.sample(n=int(para1*num), replace=True, random_state=seed, axis=0)
    oob = pd.concat([dataset_y0.drop(y0_set.index, axis=0), dataset_y1.drop(y1_set.index, axis=0)])
    training_set = pd.concat([y0_set, y1_set], axis=0)
    return training_set, oob


def logi_reg(training_set):
    linreg = LogisticRegression(penalty='l2', max_iter=100)  #, solver='liblinear'
    linreg.fit(training_set.iloc[:, 1:], training_set.iloc[:, 0])
    # print(linreg.coef_)
    return linreg


def vote(df, para1, cons):
    linreg_set = []
    row_n = len(df)
    pre_set = np.zeros(shape=[row_n, cons])
    pre_oob = pd.DataFrame(index=[i for i in range(row_n)], columns=[i for i in range(cons)])
    for i in range(cons):
        seed = int(np.random.rand(1)[0]*10000)
        training_set, oob = resample(df, para1, seed=seed)  #参数para1
        linreg = logi_reg(training_set)
        linreg_set.append(linreg)
        for k in range(len(oob)):
            pre_oob.iloc[oob.index[k],i] = linreg.predict(oob.iloc[k, 1:].values.reshape(1, -1))
            # print(pre_oob.head())
    for j in range(row_n):
        for i in range(cons):
            # 输出分类
            pre_set[j, i] = linreg_set[i].predict(df.iloc[j, 1:].values.reshape(1, -1))
            # 输出概率
            # pre_set[j, i] = linreg_set[i].predict_proba(df.iloc[j, 1:].values.reshape(1, -1))[0][1]
    return pre_set, pre_oob


def conf_matrix(fit_and_pre):
    tp, tn, fp, fn = 0, 0, 0, 0
    for i in range(len(fit_and_pre)):
        if fit_and_pre.iloc[i, 0] <= 0.5 and fit_and_pre.iloc[i, 1] <= 0.5:
            tp += 1
        elif fit_and_pre.iloc[i, 0] <= 0.5 and fit_and_pre.iloc[i, 1] > 0.5:
            fn += 1
        elif fit_and_pre.iloc[i, 0] > 0.5 and fit_and_pre.iloc[i, 1] > 0.5:
            tn += 1
        else:
            fp += 1
    print('confusion matrix:')
    print('tp=%s fn=%s' % (tp, fn))
    print('fp=%s tn=%s' % (fp, tn))
    print('accuracy=%.2f  tpr=%.2f fpr=%.2f' % ((tp + tn) / (tp + tn + fp + fn), tp / (tp + fn), fp / (fp + tn)))
    print()
    return


df = pd.read_excel('C:\\Users\\magfi\\Desktop\\data_v0.xlsx', sheetname=0)
for t in range(2):
    a=[0.5, 1]
    para1 = a[t]
    cons = 99
    res, pre_oob = vote(df, para1=para1, cons=cons)
    ## 投票：中位数
    # pre= median(res, axis=1)
    # pre_oob = pre_oob.values[:,:]
    # pre_oob_mean = median(pre_oob, axis=1)
    ## 投票：均值
    pre= mean(res, axis=1)
    pre_oob_mean = mean(pre_oob, axis=1)

    # print(res.mean(axis=1))
    # print(type(res.mean(axis=1)))
    fit_and_pre = pd.concat([df['y'], pd.DataFrame(pre)], axis=1)
    fit_and_pre2 = pd.concat([df['y'], pd.DataFrame(pre_oob_mean)], axis=1)
    print('n = %1s, cons = %s' % (para1*2*184,cons))
    print('vote_type = num')
    # print()
    print('training')
    conf_matrix(fit_and_pre)
    print('oob')
    conf_matrix(fit_and_pre2)
    # print(pre_oob)
    # print(pre_oob_mean)
    # print(res)

# np.savetxt('C:\\Users\\magfi\\Desktop\\ress1.txt', res.mean(axis=1), fmt='%s')

