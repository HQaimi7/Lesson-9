import datetime

# Get all the month names
months = [datetime.date(2024, month, 1).strftime('%B') for month in range(1, 13)]

#Display each month
print("The months of the year are:  ")
for month in months:
    print(month)