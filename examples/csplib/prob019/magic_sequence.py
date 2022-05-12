"""
Magic sequence in cpmpy.

http://www.dcs.st-and.ac.uk/~ianm/CSPLib/prob/prob019/spec.html
'''
A magic sequence of length n is a sequence of integers x0 . . xn-1 between
0 and n-1, such that for all i in 0 to n-1, the number i occurs exactly xi
times in the sequence. For instance, 6,2,1,0,0,0,1,0,0,0 is a magic sequence
since 0 occurs 6 times in it, 1 occurs twice, ...
'''

Cf autoref.py for a similar (but not identical) problem.

Model created by Hakan Kjellerstrand, hakank@hakank.com
See also my cpmpy page: http://www.hakank.org/cpmpy/

Modified by Ignace Bleukx
"""
import sys
import numpy as np
from cpmpy import *



# def print_solution(a):
#   print(a[0].value())

def magic_sequence(n=10, num_sols=0):
    print("n:", n)
    model = Model()

    x = intvar(0, n - 1, shape=n, name="x")

    # constraints
    for i in range(n):
        model += x[i] == sum(x == i)

    # speedup search
    model += sum(x) == n
    model += sum(x * np.arange(n)) == n

    # search for all solutions
    model.solveAll(solution_limit=num_sols,
                   display=[x])


num_sols = 0
n = 10
if len(sys.argv) > 1:
    n = int(sys.argv[1])
if len(sys.argv) > 2:
    num_sols = int(sys.argv[2])

magic_sequence(n, num_sols)

