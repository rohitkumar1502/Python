# WAP to enter marks of student in 4 differnt subject then calculate the percentage and display the grades as:

# if per greater than 75%, than distrinction.

# If per lies b\w 60 to 75,than 1st division.

#if per lies b\w 50 to 59.99.than second division.

#if per lies b\w 40 to 49.99.than Third division.

#if per lessthan 40% than fail.
CSE205=int(input("Enter marks of the CSE205: "))
CSE306=int(input("Enter marks of the CSE306: "))
CSE307=int(input("Enter marks of the CSE307: "))
INT213=int(input("Enter marks of the INT213: "))
INT307=int(input("Enter marks of the INT307: "))
avg=(CSE205+CSE306+CSE307+INT213+INT307/5)
if(avg>=90):
    print("Grade: A")
elif(avg>=80&avg<90):
    print("Grade: B")
elif(avg>=70&avg<80):
    print("Grade: C")
elif(avg>=60&avg<70):
    print("Grade: D")
else:
    print("Grade: F")