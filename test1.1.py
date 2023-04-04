month=int(input("Enter the month in the numeric form:"))
day=int(input("Enter the day in numeric form:"))
year=int(input("Enter the year as two numerical digits:"))
if month<1 or month>12:
       print("Error: Invalid Month Input")
elif day<1 or day>31:
    print("Error: Invalid Day Input")
elif year<0 or year>99:
    print("Error: Invalid Year Input")
else:
        print("Success: Congratulations! you entered the correct date. ({}/{}/{})".format(month, day, year))