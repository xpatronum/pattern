import functools


def singleton(cls):
    """
    Handy decorator for creating a singleton class
    Description:
        - Decorate your class with this decorator
        - If you happen to create another instance of the same class, it will return the previously created one
        - Supports creation of multiple instances of same class with different args/kwargs
        - Works for multiple classes
    Use:
        >>> from decorators import singleton
        >>>
        >>> @singleton
        ... class A:
        ...     def __init__(self, *args, **kwargs):
        ...         pass
        ...
        >>>
        >>> a = A(name='Siddhesh')
        >>> b = A(name='Siddhesh', lname='Sathe')
        >>> c = A(name='Siddhesh', lname='Sathe')
        >>> a is b  # has to be different
        False
        >>> b is c  # has to be same
        True
        >>>
    """
    previous_instances = {}

    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        if cls in previous_instances and previous_instances.get(cls, None).get("args") == (args, kwargs):
            return previous_instances[cls].get("instance")
        else:
            previous_instances[cls] = {
                "args": (args, kwargs),
                "instance": cls(*args, **kwargs),
            }
            return previous_instances[cls].get("instance")

    return wrapper


__all__ = ["singleton"]
