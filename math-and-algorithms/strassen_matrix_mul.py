matrix=[[2,3],[5,6]]
matrix_b=[[1,2],[4,4]]
def strassen_mul(m,m_b):
    p=(m[0][0]+m[1][1])*(m_b[0][0]+m_b[1][1])
    q=(m[1][0]+m[1][1])*m_b[0][0]
    r=m[0][0]*(m_b[0][1]-m_b[1][1])
    s=m[1][1]*(m_b[1][0]-m_b[0][0])
    t=(m[0][0]+m[0][1])*m_b[1][1]
    u=(m[1][0]-m[0][0])*(m_b[0][0]+m_b[0][1])
    v=(m[0][1]-m[1][1])*(m_b[1][0]+m_b[1][1])
    return strassen_add(p,q,r,s,t,u,v)
def strassen_add(p,q,r,s,t,u,v):
    c=[[0,0],[0,0]]
    c[0][0]=p+s-t+v
    c[0][1]=r+t
    c[1][0]=q+s
    c[1][1]=p+r-q+u
    return c
result=strassen_mul(matrix,matrix_b)
print(result)
