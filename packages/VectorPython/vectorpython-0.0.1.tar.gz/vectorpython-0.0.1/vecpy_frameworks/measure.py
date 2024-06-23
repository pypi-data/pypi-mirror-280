import time

class Timer:
    """A class dedicated to measuring execution time of functions."""
    
    @staticmethod
    def time_function(func, *args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken for {func.__name__}: {end_time - start_time:.6f} seconds\n")
        return result