# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 16:13:44 2020

@author: shriyans 
"""

sequence = ["x", "y", "z"]

newlist_a=[[a*i for a in sequence]for i in range(1,5)]

result_a = []
[ result_a.extend(el) for el in newlist_a]
 
print(result_a)
#['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz'] 


newlist_b=[[a*i for a in range(1,5)]for i in sequence]

result_b = []
[ result_b.extend(el) for el in newlist_b]
 
print(result_b)
#['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']



li=[2,3,4,5,6,7,8]

newlist_c=[[li[i+a]for a in range(4)]for i in range(4)]

var=[[[newlist_c[i][j]] for j in range(3)]for i in range(3)]

result_c = []
[result_c.extend(el) for el in var]

result_c.append(newlist_c)

print(result_c)
#[[2], [3], [4], [3], [4], [5], [4], [5], [6]] [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]


newlist_d=[[(i,j) for i in range(1,4)]for j in range(1,4)]

result_d = []
[ result_d.extend(el) for el in newlist_d]

print(result_d)
#[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]



