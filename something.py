import numpy as np
from numpy.linalg import inv
from numpy.linalg import matrix_power
v1=np.array([1,2,3])
v2=np.array([3,-4,5])
v3=np.array([-4.5,6,2])
m1 = VAk5jgTwov = np.array([v1,v2,v3])
m1 = VAk5jgTwov[::,::]
m2 = VAk5jgTwov = np.array([[1,2,3],[4,5,6],[7,8,9]]) 
m2 = VAk5jgTwov[::,::]
m3 = VAk5jgTwov = np.array([[3,2,-1],[1,1,0],[1,5,3]])
m3 = VAk5jgTwov[::,::]
m4 = VAk5jgTwov = m2[::,::]
rowI = 1-1
rowJ = 2-1
VAk5jgTwov[[rowI,rowJ]]=VAk5jgTwov[[rowJ,rowI]]       
rowI = 3-1
VAk5jgTwov[rowI]=2*VAk5jgTwov[rowI]/3
rowI = 3-1
VAk5jgTwov[rowI]=4*VAk5jgTwov[rowI]
rowI = 3-1
VAk5jgTwov[rowI]=VAk5jgTwov[rowI]/4
rowI = 1-1
VAk5jgTwov[rowI]=VAk5jgTwov[rowI]+2*VAk5jgTwov[2-1]/3
rowI = 2-1
VAk5jgTwov[rowI]=VAk5jgTwov[rowI]+VAk5jgTwov[1-1]
rowI = 2-1
VAk5jgTwov[rowI]=VAk5jgTwov[rowI]+3*VAk5jgTwov[3-1]
rowI = 2-1
VAk5jgTwov[rowI]=VAk5jgTwov[rowI]+VAk5jgTwov[3-1]/3
m4 = VAk5jgTwov[::,::]
matrix555 = []
VAk5jgTwov=np.array([[]])
matrix555 = VAk5jgTwov[::,::]
m5 = []
VAk5jgTwov=np.array([[]])
m5 = VAk5jgTwov[::,::]
VAk5jgTwov = m1+m2
m5 = VAk5jgTwov[::,::]
VAk5jgTwov = m1-m2
m5 = VAk5jgTwov[::,::]
VAk5jgTwov = m1@m2
m5 = VAk5jgTwov[::,::]
VAk5jgTwov = m1*m2
m5 = VAk5jgTwov[::,::]
VAk5jgTwov = np.transpose(m1)
m5 = VAk5jgTwov[::,::]
VAk5jgTwov = matrix_power(m1,2)
m5 = VAk5jgTwov[::,::]
VAk5jgTwov = matrix_power(m1,-1)
m5 = VAk5jgTwov[::,::]
VAk5jgTwov = JgRqziwZte=m1
JgRqziwZte = np.concatenate((JgRqziwZte,m2),axis=0)
VAk5jgTwov = JgRqziwZte
m5 = VAk5jgTwov[::,::]
m6 = VAk5jgTwov = JgRqziwZte=m2
JgRqziwZte = np.concatenate((JgRqziwZte,m3),axis=1)
VAk5jgTwov = JgRqziwZte
m6 = VAk5jgTwov[::,::]
VAk5jgTwov = m3
liRow=[]
liCol=[]
liRow.append(3-1)
liRow.append(2-1)
liCol.append(1-1)
liRow.sort(reverse=True)
liCol.sort(reverse=True)
for i in liRow:
        np.delete(VAk5jgTwov,i,0)
for i in liCol:
        np.delete(VAk5jgTwov,i,1)
m4 = VAk5jgTwov[::,::]
VAk5jgTwov = m3[:1:,1:2:]
m4 = VAk5jgTwov[::,::]
VAk5jgTwov = m1+m2-np.transpose(m1@m2)+matrix_power(m1,-1)+m1*m2
specialMat = VAk5jgTwov[::,::]