#!/usr/bin/env python3

import heapq
def heapsort(arr):

    heapq.heapify(arr)

    result = []

    while len(arr) != 0:
        result.append(heapq.heappop(arr))

    return result


print(heapsort([12, 11, 13, 5, 6, 7]))            