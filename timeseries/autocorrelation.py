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
tmp = np.random.rand(2000) * 0.0001
tmp[0:500] = lines
lines = tmp

def serial_corr(wave, lag=1):
    n = len(wave)
    y1 = wave[lag:]
    y2 = wave[:n-lag]
    corr = np.corrcoef(y1, y2, ddof=0)[0, 1]
    return corr

def autocorr(wave):
    lags = range(len(wave)//2)
    corrs = [serial_corr(wave, lag) for lag in lags]
    return lags, corrs

t = np.linspace(0, 1, 1000, False)
f1 = 25
f2 = 50
sig1 = np.sin(f1 * 2 * np.pi * t)
sig2 = np.sin(f2 * 2 * np.pi * t)
sig = sig1 + sig2

lags, corrs = autocorr(sig)
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
plt.plot(lags, corrs)
ax1.set_title('Autocorrelation sig (two sinuses)')
plt.show()

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
plt.plot(sig1[0:100])
plt.plot(sig1[40:100])
ax1.set_title('Sinus shifted by 40')
plt.show()

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
plt.plot(sig2[0:100])
plt.plot(sig2[20:100])
ax1.set_title('Sinus shifted by 20')
plt.show()

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
plt.plot(sig[0:100])
plt.plot(sig[40:100])
ax1.set_title('Original signal shifted by 40')
plt.show()

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
lags, corrs  = autocorr(sig)
plt.plot(lags[5:50], corrs[5:50])
ax1.set_title('Autocorrelation sig first 50 ticks')
plt.show()

q = np.argmax(corrs[5:50])
print(q)

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
lags, corrs = autocorr(lines)
plt.plot(lags[200:200+360//2], corrs[200:200+360//2])
ax1.set_title('Autocorrelation of visits')
plt.show()