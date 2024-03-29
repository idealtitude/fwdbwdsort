#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Proof of concept

This is an implemntation of a sorting algorithm that
I called `forward backward sort`

Here are the steps:
    the algo look forward if there's any permuation possible
    for each forward permutation, it iterates backward
    as many times as it can do permutation backward...
'''

import sys
import random
from time import perf_counter_ns

class FwdBwdSort:
    '''This class implement the algorithm'''
    def __init__(self, arr: list[int]):
        '''
        Declaring and defining the attributes of the class
        '''
        self.arr   : list[int] = arr
        self.index : int       = 0
        self.arrsz : int       = len(self.arr)
        self.steps : int       = 0 # Used for performance count
        self.dur   : float     = 0.0 # Same as above

        if len(arr) > 1:
            self.algo_loop()

    def algo_loop(self)->None:
        '''
        This the main loop where the algorithm is performed
        I've added a time counter to observe performance
        '''
        max_len: int = self.arrsz - 1
        dur_start = perf_counter_ns()

        while self.index < max_len:
            self.steps += 1
            self.swap_fwd()

        dur_stop = perf_counter_ns()
        self.dur = dur_stop - dur_start

    def swap_fwd(self)->None:
        '''
        This method operates forward permutations
        each at a time it's invoked (by the main loop)
        '''
        cur: int = self.index
        nxt: int = self.index + 1

        if nxt == self.arrsz:
            return

        if self.arr[cur] > self.arr[nxt]:
            self.arr[cur], self.arr[nxt] = self.arr[nxt], self.arr[cur]
            self.index = nxt
            if cur > 1:
                self.swap_bwd(cur)
        else:
            self.index += 1

    def swap_bwd(self, cur: int)->None:
        '''
        This method operates beckward permuations
        iteratively, as long as it has exhausted possibilities,
        each time it is called by the main loop
        '''
        self.steps += 1
        prev: int = cur - 1
        if prev == -1:
            return

        if self.arr[cur] < self.arr[prev]:
            self.arr[cur], self.arr[prev] = self.arr[prev], self.arr[cur]
        else:
            return

        if prev > 0:
            self.swap_bwd(prev) # Calling itself for next permutation bwd


def main(args = None)->int:
    '''
    Entry point, user can provide 3 arguments ([MIN] [MAX] [QUANTITY])
    to generate a list of random number to sort
    '''
    arr: list[int]

    if args is None:
        arr = [9, 5, 13, 3, 8, 7, 2, 12, 6, 10, 4, 11, 1]
    else:
        arr = args

    print(f"\033[33mArray before:\033[0m {arr}")
    fbsort = FwdBwdSort(arr)
    result: str = f"""\033[32mArray after:\033[0m {fbsort.arr}
\033[1m{fbsort.steps}\033[0m steps in {fbsort.dur} nanoseconds ({fbsort.dur / 1000000} milliseconds,\
 {(fbsort.dur / 1000000) / 1000} seconds)"""
    print(result)

    return 0

if __name__ == '__main__':
    if len(sys.argv) == 4:
        # Proccesing command line arguments
        min_num: int = int(sys.argv[1])
        max_num: int = int(sys.argv[2])
        nums_num: int = int(sys.argv[3])
        rand_arr: list[int] = random.sample(range(min_num, max_num), nums_num)
        sys.exit(main(rand_arr))
    else:
        sys.exit(main())
