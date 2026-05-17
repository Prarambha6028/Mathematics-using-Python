#Find factors of numbers
def factors(num):
    print("The factors are:")
    for i in range(1,num+1):
        if num%i==0:
            print(i)
num=int(input("Enter any number:"))
if num>0:
    factors(num)
else:
    print("Enter positive number.")
