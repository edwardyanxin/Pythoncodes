# -*- coding: utf-8 -*-
"""
Spyder 编辑器

这是一个临时脚本文件。
"""
import numpy as np
import scipy
from scipy.sparse import coo_matrix     #稀疏矩阵
#import system 


filename = 'C:/Users/yanxin/MYCODES/Pythoncodes/Cholesky ATA.txt'
file1 = open(filename)

a =file1.read()

b =a.split('\n')#使用换行

#统计有多少行

 

for i in range(len(b)):

     b[i] = b[i].split()#使用空格分开
d=[]
for i in range(len(b)):
    for j in xrange(len(b[i])):
        d.append(float(b[i][j]))
        
        
c = np.array(d).reshape(len(b),len(b[0]))

index = np.where(c!=0)
 
H = coo_matrix((c[index],(index[0],index[1])),shape=c.shape)

e = np.dot(H.T,H).todense()
f = np.linalg.cholesky(e)