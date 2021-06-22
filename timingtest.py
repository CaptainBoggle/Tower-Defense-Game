import itertools
import timeit
import random

setup = ''' 
import random
class testclass():
    def __init__(self,name):
        self.name = name
        self.x=random.randrange(0,500)
        self.y=random.randrange(0,500)

def inRange(tc):
    if tc.x + tc.y <= 150:
        return True
    return False


'''

nofiltercode = '''
testlist = [testclass("a"),testclass("b"),testclass("c"),testclass("d"),testclass("e"),testclass("f"),testclass("g"),testclass("h"),testclass("i"),testclass("j"),testclass("k"),testclass("l"),testclass("m")]
find = next((x for x in testlist if inRange(x)), None)
'''

filtercode = '''  
testlist = [testclass("a"),testclass("b"),testclass("c"),testclass("d"),testclass("e"),testclass("f"),testclass("g"),testclass("h"),testclass("i"),testclass("j"),testclass("k"),testclass("l"),testclass("m")]
find = next(filter(inRange,testlist), None)
'''

print (timeit.timeit(setup = setup,
                     stmt = filtercode,
                     number = 10000)) 

print (timeit.timeit(setup = setup,
                     stmt = nofiltercode,
                     number = 10000)) 

print (timeit.timeit(setup = setup,
                     stmt = filtercode,
                     number = 10000)) 

print (timeit.timeit(setup = setup,
                     stmt = nofiltercode,
                     number = 10000)) 