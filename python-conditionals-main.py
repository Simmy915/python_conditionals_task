driver_speed = float (input("Enter your current in Km/h: \n")) #The user enters their speed
average_speed = float (input("Enter the allowed average speed in km/h: \n")) #The user enters the average speed acceptable
over_limit = float ((driver_speed-average_speed))/5
if driver_speed< 60:
    print ("Ok")
elif driver_speed > 60 and over_limit < 12:
    print ("Points: 2")
else:
    print("It is time to go to jail")
