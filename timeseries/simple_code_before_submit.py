import fileinput
import numpy as np
from datetime import datetime
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

filename = "input01.txt"
with open(filename, 'r') as f:
    lines = f.read().splitlines()

lines = [float(line) for line in lines]
lines = np.array(lines[1:])
original_lines = lines
n = len(lines)
days = np.array(range(n)) % 7

ref = datetime(2012, 10, 1, 0, 0).toordinal()
dates = [datetime(2012, 11, 1, 0, 0).toordinal() - ref,
         datetime(2013, 11, 1, 0, 0).toordinal() - ref]#,
         #datetime(2014,  11, 1,  0, 0).toordinal() - ref]

def first_0_day_before_date(dates, days):
    zerodays = []
    for d in dates:
        for i in reversed(range(d)):
            if days[i] == 0:
                zerodays.append(i)
                break
    return zerodays

init_dates = first_0_day_before_date(dates, days)

avg = np.mean(lines)
lines = lines - avg
var = np.std(lines)
lines = lines / var
diff = np.append([0], lines[1:] - lines[:-1])
diff_clipped = np.clip(diff, -1, 1)

past_trends = []

for date in init_dates:
    past_trends.append(diff_clipped[date: date + 40])


average_trend = np.mean(np.array(past_trends), axis=0)

for trend in past_trends:
    plt.plot(trend)

plt.plot(average_trend)
plt.show()

dates = [datetime(2015,  11, 1,  0, 0).toordinal() - ref]
dates = [datetime(2013, 11, 1, 0, 0).toordinal() - ref]
last_stab = first_0_day_before_date(dates, days)

final_part = lines[last_stab[0]:]
average_trend

extension = [final_part[0]]

for i in range(1, len(average_trend)):
    extension.append(extension[i-1] + average_trend[i])


extended_lines = np.append(lines[0:last_stab[0]], extension[1:])

extended_lines = (extended_lines * var)  + avg

plt.plot(extended_lines)
plt.plot(original_lines[0: len(extended_lines)])
plt.show()