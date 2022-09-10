
#WAP to calculate sum and average of number betn m to n
n= int(input("Enter Number of n "))
m= int(input("Enter Number of m "))

sum = 0
for num in range(1,n+1,m+1):
    sum=sum+num
print("Sum of first",n,m, "number is:",sum)
average =sum/n,m
print("Average of ",average,"number is:",average)
