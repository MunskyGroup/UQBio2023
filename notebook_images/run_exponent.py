# -*- coding: utf-8 -*-
"""
Created on Sun May 14 18:13:32 2023

@author: william
"""

### Example commandline Python code for UQ-Bio2023 notebooks
###

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--x", help='variable x for x^n', type=str, default=0)
parser.add_argument("--exponent", help='variable n for x^n', type=str, default=0)
args = parser.parse_args()
x = float(args.x)
n = float(args.exponent)
print('The result of {x} ^ {n} is'.format(x=x,n=n))
print(x**n) 