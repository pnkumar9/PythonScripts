#!/usr/bin/env python3
'''
F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.

We could use a hash table to keep track of the result of each F(n) with n as the key.
The hash table serves as a cache that saves us from duplicate calculations.

Using cache avoids duplicate work
'''
def fib(N):
    """
    :type N: int
    :rtype: int
    """
    cache = {}
    def recur_fib(N):
        if N in cache:
            return cache[N]

        if N < 2:
            result = N
        else:
            result = recur_fib(N-1) + recur_fib(N-2)

        # put result in cache for later reference.
        cache[N] = result
        return result

    return recur_fib(N)

print(fib(5)) 