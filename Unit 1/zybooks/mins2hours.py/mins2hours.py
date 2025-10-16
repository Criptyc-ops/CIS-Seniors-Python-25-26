'''
convert a set of numbers of minutes to hours
'''

minutes = int(input("enter minutes:"))
hours = minutes // 60
mins_remaining = minutes % 60

print(minutes, "minute(s) is,", hours, "hour(s) and", mins_remaining, "minute(s).")
