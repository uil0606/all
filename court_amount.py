import pandas as pd

def Num_catch(a):
    mm = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
    loc1 = -1
    for i in range(len(a)):
        for j in range(len(mm)):
            if a[i] == mm[j]:
                loc1 = i
                break
        else:
            continue
        break
    loc2 = len(a)
    for i in range(len(a)-loc1):
        para = 0
        for j in range(len(mm)):
            if a[loc1 + i] != mm[j]:
                para = para + 1
        if para == 11:
            loc2 = loc1 + i
            break
    # print(loc1,loc2)
    if loc1 != -1:
        return a[loc1:loc2]

df=pd.read_excel('c:/users/magfi/desktop/金额.xlsx')
n=len(df)
a=pd.DataFrame(data=None,index=[i for i in range(n)],columns=['金额'])

for i in range(n):
    if len(str(df.iloc[i,3]))>50 or len(str(df.iloc[i,3]))==0:
        continue
    if df.iloc[i,2]=='执行内容':
        a.iloc[i,0]=Num_catch(str(df.iloc[i,3]))
        continue
    if df.iloc[i,2]=='行政执法结果':
        temp = Num_catch(str(df.iloc[i, 3]))
        if temp != None:
            a.iloc[i, 0] = float(temp) * 10000
        continue
    if df.iloc[i,2]=='欠税余额':
        a.iloc[i, 0] = Num_catch(str(df.iloc[i, 3]))
        continue
    if df.iloc[i,2]=='涉案金额':
        a.iloc[i, 0] = Num_catch(str(df.iloc[i, 3]))
        continue


a.to_excel('c:/users/magfi/desktop/res.xlsx')



