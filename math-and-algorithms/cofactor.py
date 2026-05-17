#Determinants via cofactor expansion
#Matrices
matrix= [[1,2,3],[4,5,6],[7,8,9]]


def det(mat,n):
    if n==1:
        #1x1 matrix
        return mat[0][0]
    if n==2:
        #2x2 matrix
        return mat[0][0]*mat[1][1]-mat[1][0]*mat[0][1]
    result=0
    for col in range(n):
        '''sub_matrix=[[mat[i][j] for j in range(n) if j != col] for i in range(1, n)]'''
        sub_matrix=[]
        for i in range(1,n):
            new=[]
            for j in range(n):
                if j!=col:
                    new.append(mat[i][j])
            sub_matrix.append(new)
        if col%2==0:
            sign=1
        else:
            sign=-1
        result+=sign*mat[0][col]*det(sub_matrix,n-1)
    return result

print("The matrix:",matrix)

length=len(matrix)

res=det(matrix,length)

print("The Determinant of teh Matrix:",res)
