import matplotlib
from matplotlib import pyplot as plt
import numpy as np
from scipy.signal import butter, lfilter, freqz
filename = "input01.txt"
with open(filename, 'r') as f:
    lines = f.read().splitlines()

lines = [float(line) for line in lines]
print(lines)
lines = np.array(lines[1:])
avg = np.mean(lines)
lines = lines - avg
plt.plot(lines)
plt.show()



# overlay years



lines_part1 = lines[0:356//2 + 1]
lines_part2 = lines[356//2 + 1:356 + 1]
lines_part3 = lines[357:int(1.5 * 356) + 1 ]
# lines_part4 = lines[int(1.5 * 356) + 1 :]

lines_part1 = (lines_part1 - np.mean(lines_part1))
lines_part1 = (lines_part2[0:150] - np.mean(lines_part2[0:150]))
lines_part3 = (lines_part3 - np.mean(lines_part3))

lines_part1 = lines_part1/np.max(lines_part1)
lines_part2 = lines_part2/np.max(lines_part2)
lines_part3 = lines_part3/np.max(lines_part3)

plt.plot(lines_part1)
plt.plot(lines_part2[0:150])
plt.plot(lines_part3)
# plt.plot(lines_part4)
plt.show()