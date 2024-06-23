from benchmarks.addition import AdditionBenchmark
from benchmarks.subtraction import SubtractionBenchmark
from vectorpython_frameworks import Timer
import inspect


def run_bench(bench_class):

    print(f"\n...Running benchmarks for {bench_class.__name__}...\n")
    # Create an instance of the benchmark class
    bench_instance = bench_class()
    # Loop through all methods of the instance
    for name, method in inspect.getmembers(bench_instance, predicate=inspect.ismethod):
        # Check if the method name starts with 'time_'
        if name.startswith('time_'):
            print(f"Running {name}...")
            # Time the method using Timer
            Timer.time_function(method)

# Example usage with your AdditionBenchmark class
# run_bench(AdditionBenchmark)
# run_bench(SubtractionBenchmark)