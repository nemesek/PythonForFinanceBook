import math
import timeit
import numpy as np
import numexpr as ne

loops = 250000000
a = range(1,loops)
testcode = '''
def f(x):
    return 3 * math.log(x) * math.cos(x) ** 2
'''
print('time1', timeit.timeit(stmt=testcode))

a = np.arange(1,loops)
testcode = '''
def g(x):
    return 3 * np.log(a) + np.cos(a) ** 2
'''
print('time2', timeit.timeit(stmt=testcode))

ne.set_num_threads(4)
#f = '3 * log(a) + cos(a) ** 2'
#g = 'ne.evaluate(f)'

testcode = '''
def h(x):
    return ne.evaluate('3 * log(a) +cos(a) **2')
'''
print('time3', timeit.timeit(stmt=testcode))

print('done sucka')