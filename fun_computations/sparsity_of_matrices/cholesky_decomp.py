import numpy as np
import matplotlib
from scipy.sparse import random
from scipy import stats
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
source = np.linspace(0.01, 0.5, 100)
resutls = []

for p in source:
    S = random(100, 100, density=p)

    T = S.A.copy()

    for i in range(T.shape[0]):
        for j in range(T.shape[1]):
            if i > j:
                T[i, j] = 0

    Q = np.matmul(T, np.transpose(T))
    print(Q.shape)
    nz = np.count_nonzero(Q)
    print("non zeros", nz)
    all = Q.shape[0] * Q.shape[1]
    print("total", all)
    print("zeros", len(np.where(Q==0)))
    print(nz / all)
    resutls.append(nz/ all)

plt.figure()
plt.plot(source, resutls)
plt.title("density in source vs density in target")
plt.axes().set_aspect('equal', 'datalim')
plt.show()