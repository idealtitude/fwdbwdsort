# Forward Backward Sort

## A sorting algorithm

I was thinking about a way to sort an integers array, and I came with this
solution (which has probably been invented yet, and tested).

**My algorithm is very simple:**

I look for the two first numbers (from index 0) that I can do a permutation
on, then I look backward iteratively to check if the 2nd of the two numbers
can be permutated with all previous numbers.
When backward sort returns, we go to next 2 numbers from last index; for each
forward sort, there's a backward sort iteratively, until the array is exhausted.

If anyone is interested to do a benchmark, i'd like to see how it goes... :)

### Test it

Download and run the py file; you can use 3 arguments to pass to the script
to generate an array of random numbers:

```
# MIN and MAX are respectively the smallest number and biggest numbers
# in your array, and QUANTITY is how many numbers it contains.
./fwdbwd_sort.py [MIN] [MAX] [QUANTITY]
```

