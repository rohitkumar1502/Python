# WAP to chek whether a person is eligible to vote or not also,calculate the age gap for being eligible
age=int(input("enter age:"))
if age>=18:
     print("Eligible for voting")
else:
    print("Not Eligible for Voting")
    gap=(18-age)
    print("Gap btn")
    print(gap)
 
