"""
Evaluate flattened iterator using visible test cases
"""

from flattenedIterator import FlattenedIterator
from evaluate import evaluate
import random

class ListIterator:
    def __init__(self, items):
        self.items = list(items)

    def hasNext(self):
        return bool(self.items)
    def next(self):
        if self.hasNext():
            return self.items.pop(0)
        else:
            raise Exception()

class MyIterator:
    def __init__(self, subiterators):
        self.queue = []
        for it in subiterators:
            if it.hasNext():
                self.queue.append(it)
    def hasNext(self):
        return bool(self.queue)
    def next(self):
        if self.hasNext():
            first = self.queue.pop(0)
            val = first.next();
            if first.hasNext():
                self.queue.append(first)
            return val
        else:
            raise Exception()

class RandomIterator:
    def __init__(self, seed):
        self.rand = random.Random(seed)
        self.remaining = self.rand.randint(0, 100)
    def hasNext(self):
        return self.remaining > 0
    def next(self):
        if self.hasNext():
            self.remaining = self.remaining - 1
            return self.rand.randint(-1000, 1000)
        else:
            raise Exception()


def visibletestcase1():
    it = FlattenedIterator([])
    assert(not it.hasNext())

def visibletestcase2():

    A = ListIterator([1, 2, 3])
    B = ListIterator([4, 5])
    C = ListIterator([6, 7, 8])
    it = FlattenedIterator([A, B, C])
    assert(it.hasNext() and it.next() == 1 and
       it.hasNext() and it.next() == 4 and
       it.hasNext() and it.next() == 6 and
       it.hasNext() and it.next() == 2 and
       it.hasNext() and it.next() == 5 and
       it.hasNext() and it.next() == 7 and
       it.hasNext() and it.next() == 3 and
       it.hasNext() and it.next() == 8 and
       not it.hasNext())

def hidden1():

    A = ListIterator([])
    B = ListIterator([])
    it = FlattenedIterator([A,B])
    assert(not it.hasNext())

def hidden2():

    A = ListIterator([1,2])
    it = FlattenedIterator([A])
    assert(it.hasNext() and it.next() == 1 and
       it.hasNext() and it.next() == 2 and
       not it.hasNext())

def hidden3():

    A = ListIterator([1,2])
    B = ListIterator([3,4])
    it = FlattenedIterator([A,B])
    assert(it.hasNext() and it.next() == 1 and
       it.hasNext() and it.next() == 3 and
       it.hasNext() and it.next() == 2 and
       it.hasNext() and it.next() == 4 and
       not it.hasNext())

def hidden4():

    A = ListIterator([1,2])
    B = ListIterator([3,4,5,6])
    C = ListIterator([])
    D = ListIterator([8,9,10])
    it = FlattenedIterator([A,B,C,D])
    assert(it.hasNext() and it.next() == 1 and
       it.hasNext() and it.next() == 3 and
       # it.hasNext() and it.next() == 7 and
       it.hasNext() and it.next() == 8 and
       it.hasNext() and it.next() == 2 and
       it.hasNext() and it.next() == 4 and
       it.hasNext() and it.next() == 9 and
       it.hasNext() and it.next() == 5 and
       it.hasNext() and it.next() == 10 and
       it.hasNext() and it.next() == 6 and
       not it.hasNext())

def hidden5():

    A = ListIterator([-1,-2])
    B = ListIterator([-4,-3])
    it = FlattenedIterator([A,B])
    assert(it.hasNext() and it.next() == -1 and
       it.hasNext() and it.next() == -4 and
       it.hasNext() and it.next() == -2 and
       it.hasNext() and it.next() == -3 and
       not it.hasNext())

def hidden6():

    A = ListIterator([1])
    B = ListIterator([2,2])
    C = ListIterator([3,3,3])
    D = ListIterator([4,4,4,4])
    it = FlattenedIterator([A,B,C,D])
    assert(it.hasNext() and it.next() == 1 and
       it.hasNext() and it.next() == 2 and
       it.hasNext() and it.next() == 3 and
       it.hasNext() and it.next() == 4 and
       it.hasNext() and it.next() == 2 and
       it.hasNext() and it.next() == 3 and
       it.hasNext() and it.next() == 4 and
       it.hasNext() and it.next() == 3 and
       it.hasNext() and it.next() == 4 and
       it.hasNext() and it.next() == 4 and
       not it.hasNext())

def hidden7():

  rand = random.Random()
  subits1 = []
  subits2 = []
  for x in range(rand.randint(10, 20)):
      seed = rand.randint(0, 1000000)
      subits1.append(RandomIterator(seed))
      subits2.append(RandomIterator(seed))
  it1 = MyIterator(subits1)
  it2 = FlattenedIterator(subits2)
  while True:
      assert it1.hasNext() == it2.hasNext()
      if it1.hasNext():
          assert it1.next() == it2.next()
      else:
          break

def hidden8():

    A = ListIterator([3, -2])
    B = ListIterator([])
    it = FlattenedIterator([A,B])
    assert(it.hasNext() and it.next() == 3 and
         it.hasNext() and it.next() == -2 and
         not it.hasNext())
    
def hidden9():
  A = ListIterator([])
  B = ListIterator([5, 4])
  it = FlattenedIterator([A, B])
  assert(it.hasNext() and it.next() == 5 and
         it.hasNext() and it.next() == 4 and
         not it.hasNext())

if __name__ == '__main__':
    evaluate([visibletestcase1, visibletestcase2, hidden1, hidden2, hidden3, hidden4, hidden5, hidden6, hidden7, hidden8, hidden9])
