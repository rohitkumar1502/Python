#WAP to calculate sum and average of n random no- sentinel loop.
print("Enter any the number and -1 to exit")
n=int(input("Enter any number"))
sum=0
count_term=0
while(n!=-1):
    sum=sum+n
    n=int(input("Enter next no"))
    count_term=count_term+1
    print("sum is",sum)
    avg=sum/count_term
    print("avg is",avg)