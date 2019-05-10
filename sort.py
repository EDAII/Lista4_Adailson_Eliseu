#!/bin/python3
import time
import sys
from os.path import isfile
from gera_vector import gera_vector_rapido as gera_vector
import benchmark
from merge_sort.recursive_merge_sort import recursive_merge_sort as merge_sort
from merge_sort.parallel_merge_sort import parallel_merge_sort
from bucket_sort.bucket_sort import iterative_bucket_sort
from bucket_sort.bucket_sort import bucket_iterative_radix_sort
from radix_sort.radix_sort import iterative_radix_sort
from radix_sort.radix_sort import recursive_radix_sort
from heap_sort.heap_sort import heap_sort#, good_heap_sort
# from quick_sort.quick_sort import quick_sort # need to use another sort strategy

strategies = {
    'merge_sort': merge_sort,
    'parallel_merge_sort': parallel_merge_sort,
    'iterative_bucket_sort': iterative_bucket_sort,
    'bucket_iterative_radix_sort': bucket_iterative_radix_sort,
    'recursive_radix_sort': recursive_radix_sort,
    'iterative_radix_sort': iterative_radix_sort,
    'heap_sort': heap_sort,
    # 'quick_sort': quick_sort
}

def usage():
    usage_text = """USAGE
    {} <sort_strategy> <iterations_per_benchmark> <start_with_n_elements> <end_with_n_elements> <range_step> <new_benchmark>\n""".format(sys.argv[0])
    usage_text = usage_text + """OPTIONS
    --help\t\t\tShow this usage text
    --test\t\t\tInterative mode
    --probe\t\t\tRun merge sort with 100.000 randomic elements""" + """
    sort_strategy\t\tSelect one of sort methods\n"""
    for st in strategies.keys():
        usage_text = usage_text + "\t\t\t\t{}\n".format(st)
    usage_text = usage_text + """    iterations_per_benchmark\tNumber of tests with same vector length
    start_with_n_elements\tInitial number of elements (Must be greater than 1)
    end_with_n_elements\t\tFinal number of elements  (Must be greater than start_with_n_elements)
    range_step\t\t\tNumber of elements is increased in range_step per iteration (Must be in [end_with_n_elements, start_with_n_elements] interval)
    new_benchmark\t\tIf True recriate the benchmark file
    """
    return usage_text

def time_to_ms(time):
    return (int(1000*1000*time))/1000 # Use int() to truncate value in microseconds

def run_test(sort_strategy=merge_sort, sort_strategy_name='merge_sort', number_of_elements=100000, start_of_range=0, end_of_range=1000000):
    vector = gera_vector([start_of_range, end_of_range], number_of_elements)
    start = time.time()
    vector = sort_strategy(vector)
    end = time.time()
    time_in_ms = time_to_ms((end-start))
    return [sort_strategy_name, len(vector), time_in_ms, True]

def run_benchmark(sort_strategy=merge_sort, sort_strategy_name='merge_sort', iterations_per_benchmark=100, start_with_n_elements=100, end_with_n_elements=100000, range_step=10000, new_benchmark=False):
    benchmark_file_path = "tests_{}_{}_{}.csv".format(sort_strategy_name, start_with_n_elements, end_with_n_elements)
    if new_benchmark or not isfile(benchmark_file_path):
        benchmark.clear_file(benchmark_file_path)
    else:
        pass
    start_with_n_elements = int(start_with_n_elements)
    end_with_n_elements = int(end_with_n_elements)
    range_step = int(range_step)
    if end_with_n_elements < start_with_n_elements:
        raise Exception("\nEnd must be greater than start.\n")
    elif range_step >= (end_with_n_elements-start_with_n_elements) :
        raise Exception("\nThe step range be in [start-end] interval.\n")
    for i in range(int(iterations_per_benchmark)):
        tests = []
        for number_of_elements in range(start_with_n_elements, end_with_n_elements+1, range_step):
            single_test = run_test(sort_strategy, sort_strategy_name, number_of_elements)
            tests.append(single_test)
        benchmark.write(
                benchmark_file_path,
                tests
                )

def main():
    print('Deseja:\n1) Realizar uma analise de performance\n2) Executar o algoritmo apenas uma vez?\n')
    opcao = int(input(''))
    if opcao == 1:
        # some other inputs
        pass
    else:
        elementos = int(input("Deseja ordenar quantos elementos?"))
        single_test = run_test(number_of_elements=elementos)
        print("{} elementos em {} ms".format(single_test[1], single_test[2]))

def get_sort_strategy(sort_strategy_name):
    sort_strategy = None
    for sort in strategies:
        if sort_strategy_name == sort:
            sort_strategy = strategies[sort]
    if sort_strategy == None:
        raise Exception("\nInvalid sort_strategy argument.\n")
    return sort_strategy

if __name__ == '__main__':
    if (len(sys.argv) >= 6):
        sort_strategy_name = sys.argv[1]
        sort_strategy = get_sort_strategy(sort_strategy_name)
        iterations_per_benchmark = sys.argv[2]
        start_with_n_elements = sys.argv[3]
        end_with_n_elements = sys.argv[4]
        range_step = sys.argv[5]
        new_benchmark = True if sys.argv[6] == "True" else False
        run_benchmark(sort_strategy, sort_strategy_name, iterations_per_benchmark, start_with_n_elements, end_with_n_elements, range_step, new_benchmark)
    elif(len(sys.argv) == 2):
        if sys.argv[1] == "--probe":
            single_test = run_test(number_of_elements=100000)
            print("{} elementos em {} ms".format(single_test[1], single_test[2]))
        elif sys.argv[1] == "--test":
            main()
        elif sys.argv[1] == "--help":
            print(usage())
    else:
        print(usage())
