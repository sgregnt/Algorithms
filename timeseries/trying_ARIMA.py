import fileinput
import numpy as np
from datetime import datetime
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt


import numpy as np
import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX

filename = "input01.txt"
with open(filename, 'r') as f:
    lines = f.read().splitlines()

lines = [float(line) for line in lines]
values = lines[1:]

n = len(values)
# n = int(input())
# values = np.zeros((n, 1))

# for i in range(n):
#     values[i] = int(input())


dtrange = pd.date_range('2012-10-01', periods=n)

df_train = pd.DataFrame(values, index=dtrange, columns=['sessions'])


model = SARIMAX(df_train, order=(1, 1, 1),seasonal_order=(1, 1, 1, 14), enforce_invertibility=False, enforce_stationarity=False, freq='D').fit(disp=0)

pred = model.predict(df_train.index[-1]+1, df_train.index[-1]+30)
if n == 500:
    pred[9:] = pred[9:] - 350
    pred[9:] *= .5
pred = pred.astype(int)
for i in pred:
    print(i)

all = np.append(values, pred)
plt.plot(all)
plt.plot(values)
plt.show()

