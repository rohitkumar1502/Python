#WAP to display the reverse of a no.
n=int(input("Enter the no"))
rev=0
while(n!=0):
    t=n%10
    rev =rev*10+1
    n=n//10
print(rev)