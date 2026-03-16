import sys
sys.path.append('utils')
sys.path.append('sortingAlgos')
sys.path.append('graphs')
import time

from utils.testCaseGenerator import read_array
from sortingAlgos.heapSort import heapSort
from sortingAlgos.mergeSort import mergeSort
from sortingAlgos.radixSort import radixSort
from sortingAlgos.bubbleSort import bubbleSort
from sortingAlgos.insertionSort import insertionSort
from sortingAlgos.selectionSort import selectionSort
# from sortingAlgos.quickSortFirst import quickSortFirst
from sortingAlgos.quickSortMedian import quickSortMedian
from sortingAlgos.quickSortRandom import quickSortRandom

from utils.plotter import plot_results
from utils.plotter import plot_comparisons


def time_sort(sort_func, arr):
    arr_copy = arr.copy()
    start = time.perf_counter()
    return_result = sort_func(arr_copy)
    end = time.perf_counter()
    t = end - start

    if isinstance(return_result, tuple):
        comparisons = return_result[1]
    else:
        comparisons = None
    return t, comparisons


def average_random_times(times, arrays_per_size=5):     # for each size of the array 5 random arrays are generated, and average runtime is calculated
    averaged = []
    for i in range(0, len(times), arrays_per_size):
        group = times[i : i + arrays_per_size]
        averaged.append(sum(group) / len(group))
    return averaged

if __name__ == '__main__':
    sorts = [heapSort, mergeSort, radixSort
             , bubbleSort, insertionSort, selectionSort, quickSortMedian, quickSortRandom
            ]

    ascending_arrays = read_array('testcases/ascending_dataset.txt')
    descending_arrays = read_array('testcases/descending_dataset.txt')
    random_arrays = read_array('testcases/random_dataset.txt')

    results = {}
    REPEAT_EXPERIMENT = 5   # Number of times each sorting algorithm is tested for a specific dataset

    
    for sort_func in sorts:
        name = sort_func.__name__
        results[name] = {
            'ascending': [],
            'descending': [],
            'random': [],
            'ascending_comparisons': [],
            'descending_comparisons': [],
            'random_comparisons': []
        }

        for arr in ascending_arrays:
            times = []
            for _ in range(REPEAT_EXPERIMENT):
                t, comparisons = time_sort(sort_func, arr)
                times.append(t)
            results[name]['ascending'].append(sum(times)/REPEAT_EXPERIMENT) # average runtime per testcase
            results[name]['ascending_comparisons'].append(comparisons)  # does not change across repeated experiments

        for arr in descending_arrays:
            times = []
            for _ in range(REPEAT_EXPERIMENT):
                t, comparisons = time_sort(sort_func, arr)
                times.append(t)
            results[name]['descending'].append(sum(times)/REPEAT_EXPERIMENT)    # average runtime per testcase
            results[name]['descending_comparisons'].append(comparisons) # does not change across repeated experiments

        for arr in random_arrays:
            t, comparisons = time_sort(sort_func, arr)
            results[name]['random'].append(t)
            results[name]['random_comparisons'].append(comparisons)

        results[name]['random'] = average_random_times(results[name]['random'])
        results[name]['random_comparisons'] = average_random_times(results[name]['random_comparisons'])

    plot_results(results, 'ascending', 'Best Case Runtime')
    plot_results(results, 'descending', 'Worst Case Runtime')
    plot_results(results, 'random', 'Average Case Runtime')

    plot_comparisons(results, 'ascending', 'Comparisons - Best Case')
    plot_comparisons(results, 'descending', 'Comparisons - Worst Case')
    plot_comparisons(results, 'random', 'Comparisons - Average Case')
