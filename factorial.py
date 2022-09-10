#WAP to calculate the factroial of a number.
# WAP to display all the even no betn m to n also display its count.
#WAP to display the reverse of a no.




n=int(input("Enter any +ve no"))

fact=1
if n == 0:
    print(fact)
    else:
        while(n>0):
            fact=fact*n
            n=n-1
    print(fact)