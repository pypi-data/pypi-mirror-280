from vectorpython_frameworks import vectorpythonBenchmark
from vectorpython import sub_vectors

class SubtractionBenchmark(vectorpythonBenchmark):
    
    def time_empty(self):
        sub_vectors([], [])

    def time_five(self):
        sub_vectors([1, 2, 3, 4], [1, 2, 3, 4])