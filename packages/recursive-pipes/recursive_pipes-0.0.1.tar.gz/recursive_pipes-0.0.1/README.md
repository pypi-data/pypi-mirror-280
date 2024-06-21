# Recursive Pipes for Python

Pipes are a common pattern in functional programming. It mainly boils down to
having some kind of input, which is provided to a chain of methods which
successively take the input, process it and provide the output to the next
method in the chain, which takes it as input and so forth.

In functional programming of course each method should be pure and only accept
the output from the previous method as input. In this python implementation of
couse You are free to deviate from this restriction, gaining all the benefits -
and possible pitfals. But this is not an introduction to functional programming.

There are already (good) implementations for pipes in python, e.g.
[JulienPalard/Pipe](https://github.com/JulienPalard/Pipe), which one You choose,
if at all, is a bit up to your liking. This implementation aims to be
**flexible**, **easily extendable** and allows for easy **recursion** into
substructures within your input. It also uses the dot-notation and not the
pipe-notation (`|`).

## Installation

*TODO*

## Usage and Examples

### Intro

Pipes in their simplest form can be used like that:

```python
from recursive_pipes import Pipe
# ... other imports

pipe = Pipe[Iterable[int], Iterable[int]](range(10))

@pipe.append
def onlyOdd(iterable):
    return itertools.filterfalse(lambda num: num % 2 == 0, iterable)

@pipe.append
def firstNumberBiggerThan4(iterable):
    return itertools.dropwhile(lambda num: num <= 4, iterable)

print(list(pipe.exec()))
# [5, 7, 9]
```

This is not very useful yet, although it shows some basic principles. Note, that
the Typehints are not needet, but it helps the Type-Checker to check against
input and output type of the pipe (here both are `Iterable[int]`).

### Extending the standard Pipe

To have this become a bit more useful, You can subclass the `Pipe`-class and add
some pipe functions. By default only a very limited set of functions exist,
namely `append` (we have seen that already) and the special functions
`recurseIntoDictValues` and `recurseIntoIterable`. - Also You should not
overwrite the other methods from the `Pipe`-class without knowing what You do
;).

To have some more tools at hand, we first need to extend the Pipe class:

```python

Input = TypeVar('Input')
Output = TypeVar('Output')

class IterPipe(Pipe[Input, Output]):
    def filterfalse(self, callback: Callable[[Any], bool]):
        def filterfalse(iterable):
            return itertools.filterfalse(callback, iterable)
        return self.append(filterfalse)

    def filter(self, callback: Callable[[Any], bool]):
        # a bit more concise using partial
        return self.append(partial(filter, callback))

    # if additional parameters (here the initializer argument for reduce) shall
    # be specified, an additional wrapper function must be implemented
    def reduce(self, initializer=object()):
        def reduceByCallback(callback: Callable):
            # a hack to determine, if the initializer argument was passed by
            # the user or is just the default value
            if initializer is self.reduce.__defaults__[0]:
                self.append(lambda iterable: reduce(callback, iterable))
            else:
                self.append(lambda iterable: reduce(callback, iterable, initializer))
            return self
        return reduceByCallback
```

Remark the Generic `Input` and `Output` parameters, which will enable You later
to specify type-hints for your input and output type.

Actually the `IterPipe` class already exists in the `recursive_pipes`-package,
so You can import it and use or mix it into your own `Pipe`-classes as You see
fit.

### Different Styles for creating the Pipe

This class can now be used instead of the default Pipe class:
```python
@(pipe := IterPipe[Iterable[int], int](range(20))).filter
def onlyOdd(num):
    return num % 2 == 0

@pipe.reduce(10)
def sum(carry, x):
    return carry + x

print(pipe.exec())
# 100
```

Alternatively, You can call it like that:
```python
result = ((IterPipe(range(20))).filter(lambda num: num % 2 == 0)
                               .reduce(10)(lambda carry, x: carry + x)
                               .exec())
print(result)
# 100
```

Mixed Variants are possible:
```python
pipe = IterPipe()

@pipe.filter
def onlyOdd(num):
    return num % 2 == 0

print(pipe.reduce()(lambda carry, x: carry + x).exec(range(20)))
# 90
```

### Reusing Pipes / Continuing Usage after Execution

By default Pipes can be reused as often as You like to after their definition.
```python
pipe = IterPipe(range(20))
pipe.filter(lambda num: num % 2 == 0)
print(list(pipe.exec()))
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print(list(pipe.exec(10)))
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

When using the special `memorize`-Parameter to the exec-call. The result is
stored in the pipe and will be reused as input in subsequent calls (otherwise
the input is always the input lastly specified).
```python
pipe = IterPipe(range(20))
pipe.filter(lambda num: num % 2 == 0)
# memorize the result as input for subsequent executions
result = pipe.append(lambda x: list(x)).exec(range(10), memorize=True)
print(result)
# [0, 2, 4, 6, 8]
print(pipe.reduce()(lambda carry, x: carry + x).exec())
# 20
```

The pipe can be `reset`, meaning, that the all existing callbacks will be
removed.
```python
pipe = IterPipe(range(10))
pipe.filter(lambda num: num % 2 == 0)
print(pipe.exec())
# [0, 2, 4, 6, 8]
pipe.reset()
print(pipe.exec())
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### Advanced Features: Recursing into Dictionaries / Iterables

If you have nested dictionaries / lists, you can recurse into them, which will
automatically create a subpipe on these lists / dictionaries.

```python
from collections import Counter

itemsInStore = { 'storehouse1': ['apple', 'pear', 'pear'],
                 'storehouse2': ['mushroom', 'mushroom', 'mario'] }

with IterPipe[dict[str, list[str]], dict](itemsInStore) as pipe:
    @pipe.recurseIntoDictValues()
    def countByName(subpipe: IterPipe):
        @subpipe.append
        def countByName(items: Iterable[str]):
            return Counter(items)

    pprint.pprint(dict(pipe.exec()))
# {'storehouse1': Counter({'pear': 2, 'apple': 1}),
#  'storehouse2': Counter({'mushroom': 2, 'mario': 1})}
```

This can be done arbitrarily often.
```python
tinyWorlds = [ {'name': 'snowflake', 'inhabitants': {2019: 22, 2020: 50, 2021: 49}},
               {'name': 'pythonplanet', 'inhabitants': {2018: 44, 2022: 100}} ]

pipe = IterPipe(tinyWorlds)

@pipe.recurseIntoIterable
def mapWorld(subpipe: IterPipe):
    @subpipe.append
    def copyKey(world: dict):
        world['avgInhabitants'] = world['inhabitants']
        return world

    @subpipe.recurseIntoDictValues(withKey=True)
    def mapInhabitants(subsubpipe: IterPipe):
        @subsubpipe.append
        def averageInhabitants(key, value):
            if key == 'avgInhabitants':
                return sum(value.values())/len(value.values())
            return value

    @subpipe.append
    def printWorld(world: dict):
        print(f"Name: {world['name']}")
        print(f"Average Inhabitants: {world['avgInhabitants']}")

pipe.exec()
# Name: snowflake
# Average Inhabitants: 40.333333333333336
# Name: pythonplanet
# Average Inhabitants: 72.0
```

## Developement

### Testing

Clone the project and run `pytest` from project root (the directory containing
the `pyproject.toml` file).
