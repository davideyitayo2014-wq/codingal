import calendar

# Print all months names using calendar module
print("All Month Names:")
print(list(calendar.month_name))

# Another way - loop
for month in calendar.month_name:
    if month!= "":
        print(month)