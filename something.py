import numpy as np
from numpy.linalg import inv
from numpy.linalg import matrix_power
v1=np.array([1,-2,1])
v2=np.array([0,2,-8])
v3=np.array([-4,5,9])
m1 = VAk5jgTwov = np.array([v1,v2,v3]).T  
m1 = np.round(VAk5jgTwov.copy(),2)        
answer1 = VAk5jgTwov = m1.copy()
rowI = 2-1
VAk5jgTwov[rowI]=VAk5jgTwov[rowI]/float(2)
print(VAk5jgTwov)
answer1 = np.round(VAk5jgTwov.copy(),2)   
print(answer1)
m2 = VAk5jgTwov = np.array([[1,2],[3,4]]) 
m2 = np.round(VAk5jgTwov.copy(),2)        
m3 = VAk5jgTwov = np.array([[4,3],[2,1]]) 
m3 = np.round(VAk5jgTwov.copy(),2)
ansPlus = VAk5jgTwov = m2+m3
ansPlus = np.round(VAk5jgTwov.copy(),2)
ansMinus = []
VAk5jgTwov=np.array([[]])
ansMinus = np.round(VAk5jgTwov.copy(),2)
VAk5jgTwov = m2-m3
ansMinus = np.round(VAk5jgTwov.copy(),2)
ansMul1 = VAk5jgTwov = m2@m3
ansMul1 = np.round(VAk5jgTwov.copy(),2)
ansMul2 = VAk5jgTwov = m2*m3
ansMul2 = np.round(VAk5jgTwov.copy(),2)
matrixConcatRow = VAk5jgTwov = JgRqziwZte=m2
JgRqziwZte = np.concatenate((JgRqziwZte,m3),axis=0)
VAk5jgTwov = JgRqziwZte
matrixConcatRow = np.round(VAk5jgTwov.copy(),2)
matrixConcatCol = VAk5jgTwov = JgRqziwZte=m2
JgRqziwZte = np.concatenate((JgRqziwZte,m3),axis=1)
VAk5jgTwov = JgRqziwZte
matrixConcatCol = np.round(VAk5jgTwov.copy(),2)
matSq2 = VAk5jgTwov = np.array([[1,2],[3,4]])
matSq2 = np.round(VAk5jgTwov.copy(),2)
matSq2Inv = VAk5jgTwov = matrix_power(matSq2,-1)
matSq2Inv = np.round(VAk5jgTwov.copy(),2)
idenMat2 = VAk5jgTwov = matSq2@matSq2Inv
idenMat2 = np.round(VAk5jgTwov.copy(),2)
v1=np.array([1,2,3])
v2=np.array([3,3,3])
v3=np.array([5,4,5])
matSq3 = VAk5jgTwov = np.array([v1,v2,v3]).T
matSq3 = np.round(VAk5jgTwov.copy(),2)
matSq3Inv = VAk5jgTwov = matrix_power(matSq3,-1)
matSq3Inv = np.round(VAk5jgTwov.copy(),2)
idenMat3 = VAk5jgTwov = matSq3@matSq3Inv
idenMat3 = np.round(VAk5jgTwov.copy(),2)
matNormalSq = VAk5jgTwov = np.array([[1,0,0],[2,1,0],[3,0,0]])
matNormalSq = np.round(VAk5jgTwov.copy(),2)
matPower2 = VAk5jgTwov = matrix_power(matNormalSq,2)
matPower2 = np.round(VAk5jgTwov.copy(),2)
idenMat = VAk5jgTwov = matrix_power(matNormalSq,0)
idenMat = np.round(VAk5jgTwov.copy(),2)
matTransposeSq = VAk5jgTwov = np.transpose(matNormalSq)
matTransposeSq = np.round(VAk5jgTwov.copy(),2)
matNormal2x3 = VAk5jgTwov = np.array([[2,3,4],[5,6,7]])
matNormal2x3 = np.round(VAk5jgTwov.copy(),2)
matTranspose2x3 = VAk5jgTwov = np.transpose(matNormal2x3)
matTranspose2x3 = np.round(VAk5jgTwov.copy(),2)
m4 = VAk5jgTwov = np.array([[5,4],[3,2]])
m4 = np.round(VAk5jgTwov.copy(),2)
specialMat = VAk5jgTwov = np.transpose(((m2+m3)*m4))+matrix_power(m2,2)
specialMat = np.round(VAk5jgTwov.copy(),2)