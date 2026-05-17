#Multiplication on intgers using divide and conquer
x=input("Enter any digits:")
digits=str(x)
a_1=int(digits[:2])
a_0=int(digits[2:])
y=input("Enter any digits:")
digits=str(y)
b_1=int(digits[:2])
b_0=int(digits[2:])

c_2=a_1*b_1
c_0=a_0*b_0
c_1=(a_1+a_0)*(b_1+b_0)-(c_2+c_0)
n=max(len(x),len(y))
c=c_2*10**n+c_1*10**(n/2)+c_0
print(c)
