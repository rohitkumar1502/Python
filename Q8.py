act_wt=30.0
sp_wt=20.0
ex_wt=50.0
act_max=60.0
exam_max=200.0
sp_max=50.0
ex1=int(input("marks in 1st out of 100:"))
ex2=int(input("marks in 2st out of 100:"))
sp=int(input("sport score out of 50:"))
ac1=int(input("marks in ac1 out of 20:"))
ac2=int(input("marks in ac2 out of 20:"))
ac3=int(input("marks in ac3 out of 20:"))
ex_total=ex1+ex2
act_total=ac1+ac2+ac3
ex_per=float((ex_total*ex_wt)/exam_max)
sp_per=float((sp*sp_wt)/sp_max)
ac_per=float((act_total*act_wt)/act_max)
total_per=ex_per+sp_per+ac_per
print("\n--------Result---------")
print("per in exam:\t",ex_per)
print("per in activities:\t",ac_per)
print("per in sports:\t",sp_per)