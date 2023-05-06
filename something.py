import numpy as np

v1=np.array([1,2,3])
v2=np.array([3,-4,5])
v3=np.array([-4.5,6,2])
# m1mat0 = np.array([v1,v2,v3])
# m2mat0 = np.array([[1,2,3],[4,5,6],[7,8,9]])
# m3mat0 = np.array([[3,2,-1],[1,1,0],[1,5,3]])
# m4mat0 = m2[::,::]
mat0 = np.array([v1,v2,v3])
m1 = mat0[::]
mat0 = np.array([[1,2,3],[4,5,6],[7,8,9]])
m2 = mat0[::]
mat0 = np.array([[3,2,-1],[1,1,0],[1,5,3]])
m3 = mat0[::]
mat0 = m2[::,::]
m4 = mat0[::]
rowI = 1
rowJ = 2
mat0[[rowI,rowJ]]=mat0[[rowJ,rowI]]
rowI = 3
mat0[rowI]=2*mat0[rowI]/3
rowI = 3
mat0[rowI]=4*mat0[rowI]
rowI = 3
mat0[rowI]=mat0[rowI]/4
rowI = 1
mat0[rowI]=mat0[rowI]+2*mat0[2]/3
rowI = 2
mat0[rowI]=mat0[rowI]+mat0[1]
rowI = 2
mat0[rowI]=mat0[rowI]+3*mat0[3]
rowI = 2
mat0[rowI]=mat0[rowI]+mat0[3]/3

m5=[]

m5 = mat0[::,::]

m5 = mat0[::,::]

m5 = mat0[::,::]

m5 = mat0[::,::]

m5 = mat0[::,::]

m5 = mat0[::,::]

m5 = mat0[::,::]

m5 = mat0[::,::]
m6
mat0 = m3

liRow=[]
liCol=[]
liRow.append(3)
liRow.append(2)
liCol.append(4)
liRow.append(4)
liRow.sort(reverse=True)
liCol.sort(reverse=True)
for i in liRow:
         np.delete(mat0,i,0)
for i in liCol:
         np.delete(mat0,i,1)
m4 = mat0[::,::]
mat0 = m3[2:10:2,1:2:]
m4 = mat0[::,::]