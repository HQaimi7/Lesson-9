import datetime

#1 Get your current date and time
current_datetime = datetime.datetime.now()
print(f"Current date and time: {current_datetime}")

#2 Get current Date (Without Time)
current_date = datetime.date.today()
print(f"Current Date: {current_date}")

#3 Get current time (Without Date)
current_time = datetime.datetime.now().today()
print(f"Current Time: {current_time}")

#4 Get a Specific time
specific_time = datetime.time(2024, 11, 25)
print(f"Specific Time: {specific_time}")

#5 Format date and time
formatted_datetime = current_datetime.strftime("%A, %B %d, %Y %H:%M:%S")
print(f"Formatted Date and Time: {formatted_datetime}")

#6 Create a Specific Time
specific_time = datetime.time(20, 25, 49)
print(f"Specific Time: {specific_time}")

#7 Parse a string into a datetime object
date_string = "2024-11-25 20:25:49"
parsed_datetime = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(f"Parsed Date and Time: {parsed_datetime}")

#8 Date arithmetic (Add 7 days to current date)
new_date = current_date + datetime.timedelta(days=7)
print(f"New Date (7 days later): {new_date}")

#9 Date arithmetic(Subtract 7 days to current date)
earlier_date = current_date + datetime.timedelta(days=7)
print(f"Earlier Date (7 days ago): {earlier_date}")

#10 Get the day of the week(0=Monday / 6=Sunday)
weekday = current_date.weekday()
print(f"Day of the week(0=Monday / 6=Sunday): {weekday}")

#11 Get the number of days in a month
import calendar
days_in_month =calendar.monthrange(current_date.year, current_date.month)[1]
print(f"Days in the current month: {days_in_month}")