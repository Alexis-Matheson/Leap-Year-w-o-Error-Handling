#Alexis Matheson HW 1 Leap Year

#Using python 3.9.4, run the file from the IDE or run as an executable
#Enter the year you want to test as a leap year and the program will calculate if the test year is a leap year

while True:
    #Create a test year variable and get input from the user by the input function
    year = input("Enter the year you want to test: ")
    try:
        int(year)
        is_year = True
    except:
        is_year = False
        print("The input entered is not valid.")
    #Check if the year entered is an integer
    if(is_year == True):
        y = int(year)
        if(y > 0):
            #If the year is valid, check if it's a leap year
            if((y%400 == 0) or ((y%4 == 0) and (y%100 != 0))):
                print("%d is a Leap Year!" %y)   #Print it is a leap year
            else:
                print("%d is not a Leap Year" %y)#Print it is not a leap year
        elif(y <= 0):
            print("The year entered is not a valid year")
       



