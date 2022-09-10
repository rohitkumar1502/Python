# Write a program to calculate the bill amount for an item given its quantity sold,value discount and tax
product_quantity=int(input("Enter the Product Quantity"))

Cost_per_piece=float(input("Enter the Cost per piece"))
total_cost=product_quantity*Cost_per_piece
print("Cost is",total_cost)
dis=float(input("Enter Dis.per piece"))
dis_cost=(dis*total_cost)
print("cost after dis",dis_cost)
tax=float(input("enter the tax"))
tax_amt=(tax*dis_cost)/100
final_cost=dis_cost+tax_amt
print("overall bill is,final_cost")


