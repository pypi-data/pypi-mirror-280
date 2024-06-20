# cool_pipe/pipeline.py

def pipe_fun(func):
    class PipelineFunction:
        def __init__(self, func):
            self.func = func

        def __call__(self, *args, **kwargs):
            return self.func(*args, **kwargs)

        def __ror__(self, *args, **kwargs):
            return self.func(*args, **kwargs)

    return PipelineFunction(func)


class PipeItem:
    def __init__(self, value):
        self.value = value

    def __or__(self, func):
        if isinstance(func, PipeFinish):
            return self.value
        if callable(func):
            self.value = func(self.value)
        return self


class PipeFinish:
    pass


def pipe_met(func):
    def wrapper(instance, *args, **kwargs):
        return func(instance, *args, **kwargs)
    return wrapper