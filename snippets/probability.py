

mu = 20
std = 2


x = 19.5


(x - mu)/2 # standard normal

a = (19.5-20)/2

-0.25

import scipy.stats as spi
print(spi.norm.cdf(a, loc=0, scale=1))

a2 = (22-20)/2
a1 = (20-20)/2
print(spi.norm.cdf(a2, loc=0, scale=1) - spi.norm.cdf(a1, loc=0, scale=1))
