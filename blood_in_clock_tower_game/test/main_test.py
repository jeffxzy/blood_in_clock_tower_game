import os
import sys
sys.path.append(os.path.split(os.path.realpath(__file__))[0] + "/..")

from classing.game import *
from functools import partial

def example_for_function():
    def x1(inp = 3, inp2 = 6):
        print(inp, inp2)
    def x2(inp = 3):
        print(inp)

    y = []
    y.append(x1)
    y.append(x2)
    for func in y:
        func()
    
    z = []
    z.append(partial(x1, inp = 5))
    for func in z:
        func(inp2 = 7)