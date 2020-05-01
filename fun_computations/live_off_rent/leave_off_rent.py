import matplotlib
import matplotlib.pyplot as plt

net = 800
gain = 0.047
income = 40

nets = []
spends = []
deductions = []
rentas = []

for i in range(30, 90):
    spend = (income  * 1.0) / net - gain
    rentas.append(net * gain)
    print("rentas", net * gain)
    print("spend", net * spend)
    print("net", net)
    deductions.append(spend)
    net = net * (1 + gain) - income

    nets.append(net * (1 + gain))
    spends.append(net * (gain + spend))


plt.figure()
plt.plot(range(30, 90), nets)
plt.title("Nets")

plt.figure()
plt.plot(range(30, 90), spends)
plt.title("Spends")

plt.figure()
plt.plot(range(30, 90), deductions)
plt.title("deductions")

plt.figure()
plt.plot(range(30, 90), rentas)
plt.title("rentas")

plt.show()



from collections import deque
q = deque()
q.push()
q.pop()
import heapq
m = [1,3,4,5,6,7,8,9,1]
heapq.heapify([1,3,4,5,6,7,8,9,1])
m

