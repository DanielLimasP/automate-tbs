import time 
import datetime

# Time module
def calcProd():
# Calculate the product of the first 100,000 numbers.
    product = 1
    for i in range(1, 100000):
        product = product * i
    return product

startTime = time.time()
prod = calcProd()
endTime = time.time()
print('The result is %s digits long.' % (len(str(prod))))
print('Took %s seconds to calculate.' % (endTime - startTime))

time.ctime()
thisMoment = time.time()
time.ctime(thisMoment)

for i in range(10):
    print('Tick')
    time.sleep(1)
    print('Tock')
    time.sleep(1)

# Rounding dates
now = time.time()
round(now, 2)
round(now, 4)
round(now)

# Datetime again
datetime.datetime.now()
datetime.datetime(2019, 2, 27, 11, 10, 49, 55, 53)
dt = datetime.datetime(2019, 10, 21, 16, 29, 0)
dt.year, dt.month, dt.day
dt.hour, dt.minute, dt.second

# datetime format
datetime.datetime.fromtimestamp(1000000)
datetime.datetime(1970, 1, 12, 5, 46, 40)
datetime.datetime.fromtimestamp(time.time())

# Delta datetime
delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
delta.days, delta.seconds, delta.microseconds
delta.total_seconds()

# Date adding
dt = datetime.datetime.now()
datetime.datetime(2018, 12, 2, 18, 38, 50, 636181)
thousandDays = datetime.timedelta(days=1000)
dt + thousandDays

# date subtraction
oct21st = datetime.datetime(2019, 10, 21, 16, 29, 0)
aboutThirtyYears = datetime.timedelta(days=365 * 30)
datetime.datetime(2019, 10, 21, 16, 29)
oct21st - aboutThirtyYears
datetime.datetime(1989, 10, 28, 16, 29)
oct21st - (2 * aboutThirtyYears)

# Pause until a certain date
halloween2016 = datetime.datetime(2016, 10, 31, 0, 0, 0)
while datetime.datetime.now() < halloween2016:
    time.sleep(1)

# strftime method - To visualize datetime
oct21st = datetime.datetime(2019, 10, 21, 16, 29, 0)
oct21st.strftime('%Y/%m/%d %H:%M:%S')
oct21st.strftime('%I:%M %p')
oct21st.strftime("%B of '%y")

# strptime - to convert string to datetime
datetime.datetime.strptime('October 21, 2019', '%B %d, %Y')
datetime.datetime.strptime('2019/10/21 16:29:00', '%Y/%m/%d %H:%M:%S')
datetime.datetime.strptime("October of '19", "%B of '%y")
datetime.datetime.strptime("November of '63", "%B of '%y")


