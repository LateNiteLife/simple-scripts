#!/usr/bin/python
import sys
from itertools import permutations as p 

word = sys.argv[1]
print('\n'.join([''.join(item) for item in p(word)]))
