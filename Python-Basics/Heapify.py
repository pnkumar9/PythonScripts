#!/usr/bin/env python3.6

import heapq

li = [5,7,9,1,3]

heapq.heapify(li)

print(li)
#[1, 3, 9, 7, 5]

heapq.heappush(li,4)

print(li)
#[1, 3, 4, 7, 5, 9]

print(heapq.heappop(li))
# prints 1