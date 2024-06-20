from typing import Callable, List

class CallSequencer:
    """
    Represents a block in a chain of functions.
    """

    def __init__(self, function: Callable = None, value = None, args: List = None, kwargs: dict = None):
        """
        Initialize a Block with function, value, args, and kwargs.
        """
        self.function = function
        self.value = value
        self.args = args if args is not None else []
        self.kwargs = kwargs if kwargs is not None else {}

    def __call__(self):
        """
        Execute the function with its arguments and keyword arguments.
        """
        if self.function:
            try:
                if self.kwargs:
                    return self.function(self.value, *self.args, **self.kwargs)
                return self.function(self.value, *self.args)
            except Exception as e:
                raise RuntimeError(f"Error executing function: {e}")
        return self.value

    def __execute_chain_next_node(self, other):
        """
        Execute the next block in the chain with the result of the current block.
        """
        if self.function:
            result = self()
        else:
            result = self.value
        return (
            CallSequencer(other.function, result, other.args, other.kwargs)
            if isinstance(other, CallSequencer)
            else other(result)
        )

    def __rshift__(self, other):
        """
        Implement the >> operator for chaining blocks.
        """
        return self.__execute_chain_next_node(other)

    @staticmethod
    def start(value=None):
        """
        Static method to start a chain with an initial value.
        """
        return CallSequencer(value=value)

    @staticmethod
    def simple(func: Callable):
        """
        Static method to create a block with a simple function.
        """
        return CallSequencer(func)

    @staticmethod
    def with_args(func: Callable):
        """
        Static method to create a block with a function that accepts arguments.
        """
        def wrapper(*args, **kwargs):
            return CallSequencer(func, args=args, kwargs=kwargs)
        return wrapper
