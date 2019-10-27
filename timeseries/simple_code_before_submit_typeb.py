# Enter your code here. Read input from STDIN. Print output to STDOUT
import fileinput
import numpy as np 
from  datetime import datetime
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt


# lines = []
# for line in fileinput.input():
#     lines.append(int(line.strip()))
filename = "input01.txt"
with open(filename, 'r') as f:
    lines = f.read().splitlines()

lines = [float(line) for line in lines]
original_lines = lines[1:]
N = int(lines[0])

# N = lines[0]
lines = np.array(lines[1:])
n = len(lines)
days = np.array(range(n)) % 7

ref = datetime(2012, 10, 1, 0, 0).toordinal()
dates = [datetime(2012, 11, 12, 0, 0).toordinal() - ref,
         datetime(2013, 11, 12, 0, 0).toordinal() - ref,
         datetime(2014, 11, 12, 0, 0).toordinal() - ref]

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
    past_trends.append(diff_clipped[date: date + 50])

average_trend = np.mean(np.array(past_trends), axis=0)

dates = [int(N)-1]

last_stab = first_0_day_before_date(dates, days)

final_part = lines[last_stab[0]:]

extension = [final_part[0]]

for i in range(1, len(average_trend)):
    extension.append(extension[i-1] + average_trend[i])

extended_lines = np.append(lines[0:last_stab[0]], extension[1:])
extended_lines = (extended_lines * var)  + avg

res = []
for i in range(N, N + 30):
    res.append(extended_lines[i])
    print(extended_lines[i])


plt.plot(extended_lines)
plt.plot(original_lines)
plt.show()