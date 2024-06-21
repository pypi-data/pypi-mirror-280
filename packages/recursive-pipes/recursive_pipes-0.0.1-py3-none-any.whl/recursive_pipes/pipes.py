import copy
from functools import partial
from typing import Any, Callable, Generic, Iterable, Optional, TypeVar, Self


class PipeExhausted(Exception):
    pass


Input = TypeVar('Input')
Output = TypeVar('Output')


class Pipe(Generic[Input, Output]):
    def __init__(self, input: Input|None = None, *args, **kwargs) -> None:
        self._pipe = []
        self._input = input
        self.exausted = False
        self.args = args
        self.kwargs = kwargs
        self.mapCallback = None
        self.parent = self

    def input(self, input: Input|None):
        if self.exausted:
            raise PipeExhausted("Context in which the Pipe was valid has ended.")
        self._input = input
        return self

    def getChain(self):
        if self.exausted:
            raise PipeExhausted("Context in which the Pipe was valid has ended.")
        pipe = copy.copy(self._pipe)
        def chained(input, *args, **kwargs):
            if len(pipe) == 0:
                return input
            input = pipe[0](input, *args, **kwargs)
            for f in pipe[1:]:
                input = f(input)
            return input
        return chained

    def reset(self):
        if self.exausted:
            raise PipeExhausted("Context in which the Pipe was valid has ended.")
        self._pipe = []
        return self

    def exec(self, input: Input|None = None, reset=False, memorize=False) -> Output:
        result = self._exec(input)
        if memorize:
            self._input = result
        if reset:
            self.reset()
        return result

    def _exec(self, input: Input|None = None, *args, **kwargs):
        if self.exausted:
            raise PipeExhausted("Context in which the Pipe was valid has ended.")
        args = args or self.args
        kwargs = kwargs or self.kwargs
        result = self._input if input is None else input
        if len(self._pipe) == 0:
            return result # pyright: ignore
        result = self._pipe[0](result, *args, **kwargs)
        for f in self._pipe[1:]:
            result = f(result)
        return result # pyright: ignore

    def append(self, callback: Callable) -> Self:
        if self.exausted:
            raise PipeExhausted("Context in which the Pipe was valid has ended.")
        self._pipe.append(callback)
        return self

    def recurseIntoDictValues(self, withKey = False):
        if self.exausted:
            raise PipeExhausted("Context in which the Pipe was valid has ended.")
        def recurse(callback: Callable[[Self], None]):
            subpipe = self.__class__()
            callback(subpipe)
            if withKey:
                def mapDictValues(f: Callable, d: dict):
                    return {k: f(k, v) for k, v in d.items()}
            else:
                def mapDictValues(f: Callable, d: dict):
                    return {k: f(v) for k, v in d.items()}
            return self.append(partial(mapDictValues, subpipe.getChain()))
        return recurse

    def recurseIntoIterable(self, callback: Callable[[Self], Optional[Any]]):
        if self.exausted:
            raise PipeExhausted("Context in which the Pipe was valid has ended.")
        subpipe = self.__class__()
        callback(subpipe)
        def mapValues(f: Callable, it:Iterable):
            return [f(item) for item in it]
        return self.append(partial(mapValues, subpipe.getChain()))

    def directRecurseIntoIterable(self):
        if self.exausted:
            raise PipeExhausted("Context in which the Pipe was valid has ended.")
        subpipe = self.__class__(parent = self)
        subpipe.parent = self
        def mapValues(f: Callable, it:Iterable):
            return [f(item) for item in it]
        subpipe.mapCallback = mapValues
        return subpipe

    def directRecurseIntoDict(self, condition: Callable|None = None):
        condition = condition or (lambda k, v: True)
        subpipe = self.__class__()
        def mapValues(f: Callable, d: dict):
            mapping = lambda k, v: f(v) if condition(k, v) else v 
            return {k: mapping(k, v) for k, v in d.items()}
        subpipe.mapCallback = mapValues
        subpipe.parent = self
        return subpipe

    def endRecurse(self) -> Self:
        clb = partial(self.mapCallback, self.getChain()) # pyright: ignore
        return self.parent.append(clb)

    def __enter__(self):
        return self

    def __exit__(self, *_):
        self.exausted = True
        return False
