"""
Evaluate flattened iterator
"""

from flattenedIterator import FlattenedIterator

def visibletestcase1():
    it = FlattenedIterator([])
    assert(not it.hasNext())

def visibletestcase2():
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



if __name__ == '__main__':
    try: 
        visibletestcase1()
    except AssertionError:
        print("Failed")
    except Exception as e:
        print(e)
    else:
        print('Passed')
    
    try:
        visibletestcase2()
    except AssertionError:
        print("Failed")
    except Exception as e:
        print(e)
    else:
        print("Passed")

