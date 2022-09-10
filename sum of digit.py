#Q7WAP to claculate sum of digits of a no

#Q8WAP to count the total no of +ve values, -ve value and Zeros enter by the user randomly
n=int(input("Enter a number:"))
t=0
while(n>0):
   dig=n%10
   t=t+dig
   n=n//10
print("The total sum pf digit is:",t)