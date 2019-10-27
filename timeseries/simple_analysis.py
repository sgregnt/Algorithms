import matplotlib
from  datetime import datetime
matplotlib.use('TkAgg')
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
from scipy.signal import butter, lfilter, freqz


filename = "input01.txt"
with open(filename, 'r') as f:
    lines = f.read().splitlines()

lines = [float(line) for line in lines]
n = len(lines)
days = np.array(list(range(n))) % 7
print(days)
lines = np.array(lines[1:] + [lines[-1]])
avg = np.mean(lines)
lines = lines - avg
var = np.std(lines)
lines = lines / var
original_lines = lines
lines = lines[0:470]
diff = lines[1:] - lines[:-1]
diff_clipped = np.clip(diff, -1, 1)



# plt.hist(diff_clipped, 30)
# plt.show()


plt.plot(diff_clipped)
plt.show()
1/0

split_by_week = []
n = 356//2
for i in range(0, len(diff_clipped), n):
    split_by_week.append(diff_clipped[i:i + n])

for week in split_by_week[0:2]:
    plt.plot(week)
plt.show()

N = len(lines) - 1 # location of the last
start = N - 7 * 5 + 1
diff_repeated = np.append(diff_clipped, diff_clipped[start: start + 30])

# plt.plot(diff_repeated[:-60])
# plt.show()

values = lines[-1] + diff_repeated[-30:]
# plt.plot(values)
# plt.show()


all = np.append(lines, values)
#
plt.plot(original_lines, 'c', alpha=0.5)
plt.plot(all, 'k')
plt.show()


# first sunday before november 11

ref = datetime(2012, 10, 1, 0, 0).toordinal()
dates = [datetime(2012, 11, 1, 0, 0).toordinal() - ref, datetime(2013,  11, 1,  0, 0).toordinal() - ref]

def first_0_day_before_date(dates, days):
    sundays = []
    for d in dates:
        for i in reversed(range(d)):
            if days[i] == 0:
                sundays.append(i)
                break
    return sundays

print("test1")
init_dates = first_sunday_after_january(dates, days)
print("test2")
print(days[28])
print(days[392])

plt.plot(diff_clipped[init_dates[0]:init_dates[0]+30])
plt.plot(diff_clipped[init_dates[1]:init_dates[1]+30])
plt.show()
