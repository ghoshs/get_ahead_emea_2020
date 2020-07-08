"""
Given a list of iterators, implement a FlattenedIterator class which incrementally iterates over the integers from all the iterators in an interleaved fashion.

Example:

Iterators[0] = [1,2,3]
Iterators[1] = [4,5]
Iterators[2] = [6,7,8]

FlattenedIterator = [1, 4, 6, 2, 5, 7, 3, 8]
An iterator implements the next() and hasNext() interface. You're free to use them, and you will implement them on the FlattenedIterator class.

You're free to initialize FlattenedIterator with any data structure of your choice for the iterators.
"""

class FlattenedIterator:
    def __init__(self, subiterators):
        # Implement me
        self.flattened = []
        increment_over = subiterators
        # continue loop while there still remain iterators to be traver
        while any([iterator.hasNext() for iterator in increment_over]):
            for idx, iterator in enumerate(increment_over):
                if iterator.hasNext():
                    self.flattened.append(iterator.next())
                else:
                    # remove iterators which have been traversed
                    del(increment_over[idx])

    def hasNext(self):
        # Implement me
        return bool(self.flattened)

    def next(self):
        # Implement me
        if self.hasNext():
            return self.flattened.pop(0)
        else:
            raise Exception()
