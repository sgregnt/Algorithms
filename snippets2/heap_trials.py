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