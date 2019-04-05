import time
import sys
from gera_vector import gera_vector
import benchmark
from recursive_merge_sort import recursive_merge_sort

def single_run(number_of_elements=10000, start_of_range=0, end_of_range=100000):
    vector = gera_vector([start_of_range, end_of_range], number_of_elements)
    start = time.time()
    vector = recursive_merge_sort(vector)
    end = time.time()
    time_in_ms = (int(1000*1000*(end-start)))/1000
    return ["recursive_merge_sort", len(vector), time_in_ms, True]

def run_benchmark(iterations_per_benchmark=100, start_with_n_elements=100, end_with_n_elements=100000):
    benchmark_file_path = "benchmark_merge_sort.csv"
    clear_benchmark_file(benchmark_file_path)
    start_with_n_elements = int(start_with_n_elements)
    end_with_n_elements = int(end_with_n_elements)
    for number_of_elements in range(start_with_n_elements, end_with_n_elements, int((end_with_n_elements-start_with_n_elements)/1000)):
        for i in range(int(iterations_per_benchmark)):
            benchmark = single_run(number_of_elements)
            write_benchmark(
                benchmark_file_path,
                benchmark[0],
                benchmark[1],
                benchmark[2],
                benchmark[3]
                )

def main():
    if (len(sys.argv) == 4):
        run_benchmark(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        benchmark = single_run()
        print("{} elementos em {} ms".format(benchmark[1], benchmark[2]))

if __name__ == '__main__':
    main()