import time

# seconds passed since epoch
seconds = time.time()

# convert the time in seconds since the epoch to a readable format
result = time.localtime(seconds)

print("result:", result)
year = result.tm_year
print("day:", result.tm_mday)
print("hour:", result.tm_hour)
print("minute:", result.tm_min)


def percentage(year):
      print(year)
    
percentage(year)