def covert_to_12Hour(hour,min):
    if(hour >= 12):
        period = "PM"
        if(hour > 12):
            hour -= 12
    else:
        period = "AM"
        if(hour == 0):  # Handle midnight case (00:00)
            hour = 12
    print("The answer is: ",hour,":",min)

hour =  int(input("Enter the hour(0-23): "))
min = int(input("Enter the minute(0-59): "))

if(hour < 0 or hour > 23 or min<0 or min > 59):
    print("Invalid time input")
else:
    covert_to_12Hour(hour,min)