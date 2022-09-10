second_oer_hours = 60
Seconds_per_minute =3600

hours   = int(input("Enter number of Hours: "))
minutes = int(input("Enter number of Minutes: "))
seconds = int(input("Enter number of Seconds: "))

total_seconds = 'total_seconds' + ( hours * second_oer_hours)
total_seconds = 'total_seconds' + ( minutes * Seconds_per_minute)
total_seconds = 'total_seconds' + seconds

print("Total number of seconds: ","%d"%(total_seconds))