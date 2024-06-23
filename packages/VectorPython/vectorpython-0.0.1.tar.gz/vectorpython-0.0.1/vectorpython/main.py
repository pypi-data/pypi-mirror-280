import argparse
from benchmarks.addition import AdditionBenchmark
from benchmarks.subtraction import SubtractionBenchmark
from test import run_bench

def main():
    parser = argparse.ArgumentParser(description="vectorpython Benchmark Runner")
    subparsers = parser.add_subparsers(dest='command', help='Commands')

    all_parser = subparsers.add_parser('benchmarks', help='Run all benchmarks')
    addition_parser = subparsers.add_parser('addition', help='Run addition benchmarks')
    subtraction_parser = subparsers.add_parser('subtraction', help='Run addition benchmarks')

    args = parser.parse_args()

    if args.command == 'benchmarks':
        run_bench(AdditionBenchmark)
        run_bench(SubtractionBenchmark)  # You can add more benchmarks to run here
    elif args.command == 'addition':
        run_bench(AdditionBenchmark)
    elif args.command == 'subtraction':
        run_bench(SubtractionBenchmark)

if __name__ == '__main__':
    main()