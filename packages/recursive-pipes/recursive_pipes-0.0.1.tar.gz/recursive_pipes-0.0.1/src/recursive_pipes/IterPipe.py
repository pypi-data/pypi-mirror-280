from collections import defaultdict
from functools import partial
import itertools
from typing import Any, Callable, TypeVar
from recursive_pipes import Pipe
from functools import partial, reduce


Input = TypeVar('Input')
Output = TypeVar('Output')

class IterPipe(Pipe[Input, Output]):
    def filterfalse(self, callback: Callable[[Any], bool]):
        return self.append(partial(itertools.filterfalse, callback))

    def filter(self, callback: Callable[[Any], bool]):
        return self.append(partial(filter, callback))

    def filterV(self, fn: Callable[[Any], Any]):
        return self.append(lambda d: {k: v for k, v in d.items() if fn(v)})

    def dropwhile(self, callback: Callable[[Any], bool]):
        return self.append(partial(itertools.dropwhile, callback))

    def takewhile(self, callback: Callable[[Any], bool]):
        return self.append(partial(itertools.takewhile, callback))

    def setIf(self, condition: Callable[[dict], bool], /, **kwargs: Callable[[dict], Any]):
        def setIf(record: dict):
            if condition(record):
                for k, fn in kwargs.items():
                    record[k] = fn(record)
            return record
        return self.append(lambda iterable: map(setIf, iterable))

    def map(self, fn: Callable[[Any], Any]):
        return self.append(lambda iterable: map(fn, iterable))

    def mapKV(self, fn: Callable[[Any, Any], Any]):
        return self.append(lambda d: {k: fn(k, v) for k, v in d.items()})

    def mapV(self, fn: Callable[[Any], Any]):
        return self.append(lambda d: {k: fn(v) for k, v in d.items()})

    def groupBy(self, fn: Callable[[Any], Any]):
        def groupBy(iterable):
            grouped = defaultdict(list)
            for v in iterable:
                grouped[fn(v)].append(v)
            return grouped
        return self.append(groupBy)

    def asDict(self):
        return self.append(lambda iterable: dict(iterable))

    def reduce(self, initializer=object()):
        def reduceByCallback(callback: Callable[[Any, Any], Any]):
            if initializer is self.reduce.__defaults__[0]:
                self.append(lambda iterable: reduce(callback, iterable))
            else:
                self.append(lambda iterable: reduce(callback, iterable, initializer))
            return self
        return reduceByCallback

    def sum(self):
        return self.append(sum)

    def setKey(self, key: str, callback: Callable[[Any], Any]):
        def setKey(input: Any):
            input[key] = callback(input)
            return input
        return self.append(setKey)
