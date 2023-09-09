hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
check = mins % 60
if(check > 0):
    hour = hour + mins / 60
    mins = mins % 60
if(hour > 23):
    hour = hour % 24
print(hour, ":", mins, sep="")
