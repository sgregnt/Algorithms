import math
l = 75 - 0.5
r = 75 + 0.5
z1 = math.log(l)
z2 = math.log(r)

a = math.log(3)
b = math.log(5)

y_upper_limit = int(math.floor(z2/b))

count = 0
for y in range(y_upper_limit + 1):
    x_lower_bound = int(math.ceil((z1 - y * b)/a))
    x_upper_bound = int(math.floor((z2 - y * b)/a))

    if x_lower_bound <= x_upper_bound:
        count += x_upper_bound - x_lower_bound + 1

print(count)