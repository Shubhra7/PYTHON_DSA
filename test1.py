def convert_to_12Hour(hour,min):
    if(hour >= 12):
        period="PM"
        if(hour > 12):
            hour = hour-12
    else:
        if(hour == 0):
            ansH=12
        period="AM"
    print("The time is: ",hour,":",min,period)

hour =  int(input("Enter the hour(0-23): "))
min = int(input("Enter the minute(0-59): "))

if(hour < 0 or hour > 23 or min<0 or min > 59):
    print("Invalid time input")
else:
    convert_to_12Hour(hour,min)