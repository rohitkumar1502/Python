# WAP to Calculate the tax as per given criteria:

#if income less than 150000 than no tax.

#if income lies b\w 150001 than charge 10% tax.

#if income lies b\w 300001 than charge 20% tax

#if income lies b\w 500000 than charge 30% tax.
while True:
    try:

        income = int(input("Please enter your taxable income in india: "))
    except ValueError:
        print("Sorry, We didn't understand that please enter taxable income as a number")

        continue
    else:
        break
    if income <= 250000:  #2 Lakh 50 thousand
     tax = 0


