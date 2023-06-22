# import pstats
# from prompt_toolkit import PromptSession


# class Singleton(object):
#     def __new__(cls,*args,**kwargs):
#         if not hasattr(cls,'_instance'):
#             cls._instance = super(Singleton,cls).__new__(cls,*args,**kwargs)
#         return cls._instance

# class Foo(Singleton):
#     pass

# foo1 = Foo()
# foo2 = Foo()

# print(foo1 is foo2)

import pstats


class Singleton(type):
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__call__(args, **kwargs)
        return cls._instance

# python2
class Foo(object):
    __metaclass__ = Singleton


# python3
# class Foo(metaclass=Singleton):
#     pass
foo1 = Foo()
foo2 = Foo()
print(foo1 is foo2)
