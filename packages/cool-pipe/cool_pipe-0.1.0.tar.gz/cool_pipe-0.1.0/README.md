# Cool Pipelines Library

A simple pipeline library for chaining methods and functions.

## Installation

```bash
pip install cool_pipe
```

## Usage

For functions:
```python
from cool_pipe import pipe_fun

@pipe_fun
def a(a_):
    return a_ + 1

@pipe_fun
def b(b_):
    return b_ + 2

@pipe_fun
def c(c_, t=7):
    return c_ + 3 + t

result = 1 | a | b | c
print(result)
```

For methods:
```python
from cool_pipe import PipeItem, PipeFinish, pipe_met

class A:
    def __init__(self, num: int):
        self.sum = PipeItem(num) | self.a | self.b | self.c | PipeFinish()

    @pipe_met
    def a(self, a_):
        return a_ + 1

    @pipe_met
    def b(self, b_):
        return b_ + 2

    @pipe_met
    def c(self, c_, t=5):
        return c_ + 3 + t

Aobj = A(5)
print(Aobj.sum)
```
