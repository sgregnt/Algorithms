from matplotlib import pyplot as plt
import numpy as np
from scipy import signal

filename = "input01.txt"
with open(filename, 'r') as f:
    lines = f.read().splitlines()

lines = [float(line) for line in lines]
lines = np.array(lines[1:])
avg = np.mean(lines)
lines = (lines - avg)/ np.max(lines)
t = np.linspace(0, 1, len(lines), False)

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
plt.plot(t, lines)
ax1.set_title("Signal normalized")
plt.show()

fig = plt.figure()
plt.plot(t[0:50], lines[0:50])
ax1.set_title("Zoom in first 50 samples")
plt.show()


def butter_bandpass(highcut, fs, order=5):
    nyq = 0.5 * fs
    high = highcut / nyq
    b, a = signal.butter(order, high, 'high', analog=False)
    return b, a

def butter_bandpass_filter(data, highcut, fs, order=5):
    b, a = butter_bandpass(highcut, fs, order=order)
    y = signal.lfilter(b, a, data)
    return y, b, a

fs = 500
res, b, a = butter_bandpass_filter(lines, 10, fs, order=6)

w, h = signal.freqs(b, a)
plt.semilogx(w, 20 * np.log10(abs(h)))
plt.title('Butterworth filter frequency response')
plt.xlabel('Frequency [radians / second]')
plt.ylabel('Amplitude [dB]')
plt.margins(0, 0.1)
plt.grid(which='both', axis='both')
plt.axvline(100, color='green') # cutoff frequency
plt.show()

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
plt.plot(t, res)
ax1.set_title('Filtered Signal')
ax1.axis([0, 1, -2, 2])
plt.show()