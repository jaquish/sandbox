day_name = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
month_name = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

days = -1

def days_in_month(month_n):
    if (month == 1):
         # A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400
        if (y % 4 == 0 and ( (y % 100 != 0) or (y % 400 == 0))):
            return 29
        else:
            return 28

    else:
        days = [31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return days[month_n]

start_day = 0
running_total = 0

for y in range (1900, 2000+1):
    for month in range(12):
        days += days_in_month(month)

        if (y > 1900 and start_day == 6):
            running_total += 1

        ending_day = days % 7

        print "Year:", y, "Month:", month_name[month], "\tStarts on", day_name[start_day], "\tEnding day:", day_name[days % 7]

        start_day = ( ending_day + 1 ) % 7

print "Answer is", running_total