#Heaps are binary trees for which every parent node has a value less than or equal to any of its children.
import heapq

a = [12, 43, 1, 5, 1, 3, 6 ,8, 243, 4]

heapq.heapify(a)
b = [8, 243, 43]
print(a)

# my attempt to implement heapify code

def get_left(i):
    return 2 * (i + 1) - 1

def get_right(i):
    return 2 * (i + 1) + 1 - 1

def do_min_heap(a, i, n):

    smallest = i
    left = get_left(i)
    right = get_right(i)

    if (left < n) and (a[left] < a[smallest]):
            smallest = left

    if (right < n) and (a[right] < a[smallest]):
        smallest = right

    if i != smallest:
        tmp  = a[i]
        a[i] = a[smallest]
        a[smallest] = tmp

        do_min_heap(a, smallest, n)


def do_max_heap(a, i, n):

    largest = i
    left = get_left(i)
    right = get_right(i)

    if (left < n) and (a[left] > a[largest]):
        largest = left

    if (right < n) and (a[right] > a[largest]):
        largest = right

    if i != largest:
        tmp  = a[i]
        a[i] = a[largest]
        a[largest] = tmp

        do_max_heap(a, largest, n)


b =  [200, 43]
do_min_heap(b, 0, 2)
print(b)

def heapify_min(a):
    n = len(a)
    for i in reversed(range(n)):
        do_min_heap(a, i, n)

def heapify_max(a):
    n = len(a)
    for i in reversed(range(n)):
        do_max_heap(a, i, n)

a = [12,43,1,5,1,3,6,8,243,4]
print(len(a))
heapify_min(a)
print("seconf, trial", a)

c = [1, 5, 1, 8, 43, 3, 6, 12, 243, 4]
heapify_min(c)
print(c)
heapify_max(c)
print(c)


def heapsort(a):
    #heapsort


    heapify_max(a)
    n = len(a)
    for i in reversed(range(1, n)):
        tmp = a[0]
        a[0] = a[i]
        a[i] = tmp
        do_max_heap(a, 0, i)
    # try to see what is it

print(a)
heapsort(a)
print(a)

#----------------------------------------
# Second trial
#----------------------------------------

def max_bubble_up(a, i):
    # complexity log n
    parent = i//2
    if parent > 0:
        if a[i-1] > a[parent-1]:
            a[i-1], a[parent-1] = a[parent-1], a[i-1]
        max_bubble_up(a, parent)

def max_bubble_down(a, i, n):
    # complexity log n
    left = 2 * i
    right = 2 * i + 1
    largest = i

    if left-1 < n and a[left-1] > a[largest-1]:
        largest = left
    if right-1 < n and a[right-1] > a[largest-1]:
        largest = right

    if largest != i :
        a[largest-1], a[i-1] = a[i-1], a[largest-1]
        max_bubble_down(a, largest, n)

def insert(a, elem):
    # complexity log n
    a.append(elem)
    n = len(a)
    max_bubble_up(a, n)

def delete_max(a, n):
    # complexity log n
    elem = a.pop()
    tmp = a[0]
    a[0] = elem
    max_bubble_down(a, 1, n-1)
    return tmp

def delete_elem(a, j, n):
    # complexity log n
    elem = a.pop()
    a[j] = elem
    parent = j // 2
    if parent > 0:
        if a[parent] < a[j]:
            max_bubble_up(a, j)
        else:
            max_bubble_down(a, j, n)
    else:
        max_bubble_down(a, j, n)

def heapify(a):
    # complexity n
    n = len(a)
    for j in reversed(range(n//2)):
        max_bubble_down(a, j+1, n)

def heap_sort(a):
    n = len(a)

    heapify(a)

    for i in reversed(range(n)):
        a[0], a[i] = a[i], a[0]
        max_bubble_down(a, 1, i)



#### tests

a =  [200, 43, 10, 4000]
print(a)
i = 4
max_bubble_up(a, i)
print(a)

a =  [1, 43, 10]
print(a)
i = 1
max_bubble_down(a, 1, len(a))
print(a)

print(a)
insert(a, 1.7)
insert(a, 1.8)
insert(a, 1.9)
print(a)


print(a)
delete_max(a, len(a))
print(a)

b = [1,2,5,21,3,5,6,3,1]
heapify(b)
print(b)

print(b)
delete_elem(b, 3, len(b))
print(b)

b = [1,2,5,21,3,5,6,3,1]
heap_sort(b)
print(b)