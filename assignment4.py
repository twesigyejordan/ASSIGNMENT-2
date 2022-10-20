def is_year_leap(year):#fuction declaration
    if year % 400 == 0 or year % 100 !=0 and year % 4 == 0:
        #if((year % 400 == 0) or (year % 100 !=0)and (year % 4 == 0)):
        print(True, ":",year,"is a leap year")
        print(False, ":",year,"is not a leap year")
year = int(input("Please enter a year to check if its a leap year or not:"))
is_year_leap(year)
