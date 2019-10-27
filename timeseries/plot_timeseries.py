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
from sklearn.decomposition import SparseCoder


def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y


# Filter requirements.
order = 5
fs = 150.0       # sample rate, Hz
cutoff = 10  # desired cutoff frequency of the filter, Hz

# Get the filter coefficients so we can check its frequency response.
b, a = butter_lowpass(cutoff, fs, order)

# Plot the frequency response.
w, h = freqz(b, a, worN=8000)


y = butter_lowpass_filter(lines, cutoff, fs, order)
# plt.plot(lines[1:])
# for k in [0, 80, 160, 240, 320, 400]:
#     width = 60
#     plt.plot(y[k:k + width])
#     plt.show()

plt.acorr(lines)
plt.show()
res = np.corrcoef(lines, lines)
print(res)

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


lags, corrs  = autocorr(lines)
plt.plot(lags, corrs)
plt.show()
print("here")

from scipy.fftpack import fft
# Number of sample points
N = 600
# sample spacing
T = 1.0 / 800.0
x = np.linspace(0.0, N*T, N)
y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
plt.plot(y)
plt.show()


t = np.linspace(0, 1, 1000, False)  # 1 second
sig = np.sin(2*np.pi*10*t) + np.sin(2*np.pi*20*t)
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
ax1.plot(t, sig)
ax1.set_title('10 Hz and 20 Hz sinusoids')
ax1.axis([0, 1, -2, 2])

sos = signal.butter(10, 15, 'hp', fs=1000, output='sos')
filtered = signal.sosfilt(sos, sig)
ax2.plot(t, filtered)
ax2.set_title('After 15 Hz high-pass filter')
ax2.axis([0, 1, -2, 2])
ax2.set_xlabel('Time [seconds]')
plt.tight_layout()
plt.show()

yf = fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
import matplotlib.pyplot as plt
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
plt.grid()
plt.show()
1/0
from scipy.fftpack import fft
yf = fft(corrs)
plt.plot(yf)
plt.show()
1/0
from distutils.version import LooseVersion

import numpy as np
import matplotlib.pyplot as plt

from sklearn.decomposition import SparseCoder

def ricker_function(resolution, center, width):
    """Discrete sub-sampled Ricker (Mexican hat) wavelet"""
    x = np.linspace(0, resolution - 1, resolution)
    x = ((2 / ((np.sqrt(3 * width) * np.pi ** 1 / 4)))
         * (1 - ((x - center) ** 2 / width ** 2))
         * np.exp((-(x - center) ** 2) / (2 * width ** 2)))
    return x


def ricker_matrix(width, resolution, n_components):
    """Dictionary of Ricker (Mexican hat) wavelets"""

    centers = np.linspace(0, resolution - 1, n_components)
    D = np.empty((n_components, resolution))
    for i, center in enumerate(centers):
        D[i] = ricker_function(resolution, center, width)
    D /= np.sqrt(np.sum(D ** 2, axis=1))[:, np.newaxis]
    return D


resolution = 500
subsampling = 3  # subsampling factor
width = 100
n_components = resolution // subsampling

# Compute a wavelet dictionary
D_fixed = ricker_matrix(width=width, resolution=resolution,
                        n_components=n_components)

D_multi = np.r_[tuple(ricker_matrix(width=w, resolution=resolution,
                      n_components=n_components // 5)
                for w in (10, 50, 100, 500, 1000))]
y= lines

# List the different sparse coding methods in the following format:
# (title, transform_algorithm, transform_alpha,
#  transform_n_nozero_coefs, color)
estimators = [('OMP', 'omp', None, 15, 'navy'),
              ('Lasso', 'lasso_lars', 2, None, 'turquoise'), ]
lw = 2
# Avoid FutureWarning about default value change when numpy >= 1.14
lstsq_rcond = None if LooseVersion(np.__version__) >= '1.14' else -1

plt.figure(figsize=(13, 6))
for subplot, (D, title) in enumerate(zip((D_fixed, D_multi),
                                         ('fixed width', 'multiple widths'))):
    plt.subplot(1, 2, subplot + 1)
    plt.title('Sparse coding against %s dictionary' % title)
    plt.plot(y, lw=lw, linestyle='--', label='Original signal')

    # # Do a wavelet approximation
    # for title, algo, alpha, n_nonzero, color in estimators:
    #     coder = SparseCoder(dictionary=D, transform_n_nonzero_coefs=n_nonzero,
    #                         transform_alpha=alpha, transform_algorithm=algo)
    #
    #     x = coder.transform(y.reshape(1, -1))
    #     density = len(np.flatnonzero(x))
    #     x = np.ravel(np.dot(x, D))
    #     squared_error = np.sum((y - x) ** 2)
    #     plt.plot(x, color=color, lw=lw,
    #              label='%s: %s nonzero coefs,\n%.2f error'
    #              % (title, density, squared_error))

    # Soft thresholding debiasing
    coder = SparseCoder(dictionary=D, transform_algorithm='threshold', transform_alpha=20)

    x = coder.transform(y.reshape(1, -1))

    _, idx = np.where(x != 0)

    x[0, idx], _, _, _ = np.linalg.lstsq(D[idx, :].T, y, rcond=lstsq_rcond)

    x = np.ravel(np.dot(x, D))

    squared_error = np.sum((y - x) ** 2)

    plt.plot(x, color='darkorange', lw=lw,
             label='Thresholding w/ debiasing:\n%d nonzero coefs, %.2f error'
             % (len(idx), squared_error))
    plt.axis('tight')
    plt.legend(shadow=False, loc='best')

plt.subplots_adjust(.04, .07, .97, .90, .09, .2)
plt.show()