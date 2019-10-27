# physics = input()
# hist = input()
p = [15,12,8,8,7,7,7,6,5,3]
h = [10,25,17,11,13,17,20,13,9,15]

# p = physics.split("  ")[1:]
# h = hist.split("  ")[1:]

xs = [float(elem) for elem in p]
ys = [float(elem) for elem in h]

n = len(xs)

xs_avg = sum(xs)/n
ys_avg = sum(ys)/n

s_xx = 0
s_xy = 0
for i in range(n):

    s_xy += (xs[i] - xs_avg) * (ys[i] - ys_avg)
    s_xx += (xs[i] - xs_avg) * (xs[i] - xs_avg)

print(s_xy)
print(s_xx)

r = s_xy/ s_xx

print(r)



# import math
P = [15,12,8,8,7,7,7,6,5,3]
H = [10,25,17,11,13,17,20,13,9,15]
#
n = len(P)
#
x_y = sum([p*h for (p,h) in zip(P,H)])
x = sum(P)
y = sum(H)
x_x = sum([p**2 for p in P])
#
slope = (n*x_y - x*y) / (n*x_x - x*x)

print(n*x_y - x*y)
print(n*x_x - x*x)
print(round(slope,3))