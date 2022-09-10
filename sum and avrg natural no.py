#WAP to calculate sum and average of first n natural number.

#WAP to calculate sum and average of n random no- sentinel loop.

n= int(input("Enter Number"))
sum = 0
for num in range(1,n+1,1):
    sum=sum+num
print("Sum of first",n, "number is:",sum)
average =sum/n
print("Average of ",n,"number is:",average)
