from vectorpython_frameworks import vectorpythonBenchmark
from vectorpython import add_vectors

class AdditionBenchmark(vectorpythonBenchmark):
    
    def time_empty(self):
        add_vectors([], [])

    def time_five(self):
        add_vectors([1, 2, 3, 4], [1, 2, 3, 4])


