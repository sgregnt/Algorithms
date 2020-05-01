#-------------------------------------------
# Turnstil
#-------------------------------------------

from collections import deque
exit_q = deque()
enter_q = deque()

state = 'empty'

times = [0,0,1,5]
direction = [0,1,1,0]

times =     [0,0,0,10]
direction = [1,1,0,0]


n = len(times)

for i in range(n):

    d = direction[i]
    t = times[i]

    if d == 0:
        enter_q.appendleft((t, i))
    else:
        exit_q.appendleft((t, i))

clock = 0
results = [-1] * n
while exit_q or enter_q:

    if not exit_q: # only enter
       t, i = enter_q.pop()
       results[i] = max([t, clock])
       clock += 1
       continue

    if not enter_q: # only exit
        t, i = exit_q.pop()
        results[i] = max([t, clock])
        clock += 1
        continue

    next_exit, i_exit = exit_q[-1]
    next_enter, i_enter = enter_q[-1]

    if clock < next_exit and clock < next_enter:
        state = 'empty'

    if state == 'empty':
        if next_exit <= next_enter:
            results[i_exit] = max([clock, next_exit])
            clock += 1
            next_exit = exit_q.pop()
            state = 'exit'
            continue

        else:
            results[i_enter] = max([clock, next_enter])
            clock += 1
            next_exit = enter_q.pop()
            state = 'enter'
            continue

    if state == 'exit':
        if next_exit <= clock or next_exit <= next_enter:
            results[i_exit] = max([clock, next_exit])
            clock += 1
            next_exit = exit_q.pop()
            state = 'exit'
            continue

        else:
            results[i_enter] = max([clock, next_enter])
            clock += 1
            next_exit = enter_q.pop()
            state = 'enter'
            continue

    if state == 'enter':
        if next_enter <= clock or next_enter <= next_exit:
            results[i_enter] = max([clock, next_enter])
            clock += 1
            next_exit = enter_q.pop()
            continue

        else:
            results[i_exit] = max([clock, next_exit])
            clock += 1
            next_exit = exit_q.pop()
            state = 'exit'
            continue

print(results)