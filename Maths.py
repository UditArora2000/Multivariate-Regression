import csv 
import random
import math
import numpy as np
from numpy import array
import itertools as it

ind=[]
ind=list(it.permutations([1,0,0,0,0,0,0,0,0]))
ind=ind+list(it.permutations([1,1,0,0,0,0,0,0,0]))
ind=ind+list(it.permutations([1,1,1,0,0,0,0,0,0]))
ind=ind+list(it.permutations([1,1,1,1,0,0,0,0,0]))
ind=ind+list(it.permutations([1,1,1,1,1,0,0,0,0]))
ind=ind+list(it.permutations([1,1,1,1,1,1,0,0,0]))
ind=ind+list(it.permutations([1,1,1,1,1,1,1,0,0]))
ind=ind+list(it.permutations([1,1,1,1,1,1,1,1,0]))
ind=ind+list(it.permutations([1,1,1,1,1,1,1,1,1]))
ind=list(dict.fromkeys(ind))
         
file = open("found.txt",'r')
l=file.readlines()
n=int(len(l)*80/100)
x=[]
bb=[]
for i in range(0,len(l)):
    x.append(i)
for i in range(1,601):
    bb.append(i)
random.shuffle(x)
train=x[0:n+1]
test=x[n+1:]

err=[]
mae=[]
bet=[]

for w in range(511):
    inde=ind[w]
    m=[]
    y=[]
    ap=[1]
    count=0
    file = open("found.txt",'r')
    l=file.readlines()
    for r in l:
        count+=1
        if count in train:
            p=r.find(';')
            for i in range(9):
                q=r.find(';',p+1)
                k=float(r[p+1:q])
                p=q
                ap.append(k)
            k=float(r[q+1:])
            y.append([k])
            m.append(ap)
            ap=[1]
            
    x=array(m)
    yp=array(y)
    xt=np.transpose(x)
    mp=xt@x
    mp=np.linalg.inv(mp)
    mp=mp@xt
    mp=mp@yp
    beta=mp.tolist()
    bet.append(beta)

    file = open("found.txt", 'r')
    l=file.readlines()
    count=0
    e=0
    for r in l:
        count+=1
        if count in test:
            summ=0
            p=r.find(';')
            for i in range(9):
                q=r.find(';',p+1)
                if inde[i]==1:
                    k=float(r[p+1:q])
                    summ+=k*beta[i][0]
                p=q
            l=float(r[q+1:])
            temp=l-summ
            e+=temp*temp
    err.append(e)
    mae.append(temp)

idx=err.index(min(err))
v=idx//511
w=idx-v*511
print('x1 - SJR')
print('x2 - HI Index')
print('x3 - Total Docs.(2017)')
print('x4 - Total Docs.(3 years)')
print('x5 - Total Refs.')
print('x6 - Totals Cities(3 years)')
print('x7 - Citable Docs.(3 years)')
print('x8 - Cities/Doc.(2 years)')
print('x9 - Ref./Doc.')
print('Regresiion line: y =',end=" ")
for i in range(8):
    if ind[w][i]==1:
        print(str(bet[idx][i][0])+'x'+str(i+1)+' +',end=" ")
    else:
        print('0x'+str(i+1)+' +',end=" ")
if ind[w][8]==1:
    print(str(bet[idx][8][0])+'x9')
else:
    print('0x9')

print("Mean Absolute Error is:",mae[idx]/120)
print("Mean Square Error is:",min(err)/120)

