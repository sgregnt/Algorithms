# Given a positive 32-bit integer n, you need to find the smallest 32-bit
# integer which has exactly the same digits existing in the integer
# n and is greater in value than n. If no such positive 32-bit integer exists,
# you need to return -1.I

# 12 -> 21

# 133 -> 313

# 123542 -> 124235

# 321 -> none

# 3212 -> 3221

# find first location where
# where the digit is decreasing swap with
# sorted integers to the right

n = 123542
digits = list(str(n))
digits = [int(d) for d in digits]
m = len(digits)
break_i = -1
for i in reversed(range(1, m)):
    if digits[i-1] < digits[i]:
        break_i = i
        break

if break_i == -1:
    print("does nto exists")
    1/0

candidate = digits[break_i]
candidate_i = break_i

for j in range(i, m):
    d = digits[j]
    if d < candidate and d > digits[break_i - 1]:
        candidate = d
        candidate_i = j

digits[break_i-1], digits[candidate_i] = digits[candidate_i], digits[break_i-1]
tail = sorted(digits[break_i:]) # don't need to sort can only reverse.
digits = digits[0:break_i] + tail
digits = [str(d) for d in digits]
int_str = "".join(digits)
print(int(int_str))
