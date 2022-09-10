
#WAP to count the total no of +ve values, -ve value and Zeros enter by the user randomly
print("Enter any no and enter -999 to exit")
n=int(input("Enter any value of n"))
count_pos=0
count_neg=0
count_zero=0
while(n!=-999):
  if n>0:
    count_pos=count_pos+1
  elif n<0:
    count_neg=count_neg+1
  else:
    count_zero=count_zero+1
  n=int(input("Enter next no"))
print("positive",count_pos)
print("positive",count_neg)
print("positive",count_zero)