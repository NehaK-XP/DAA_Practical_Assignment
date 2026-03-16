import random

def quickSortRandom(arr):
    comparisons = [0]

    def partition(low, high):
        pivot_index = random.randint(low, high)
        arr[low], arr[pivot_index] = arr[pivot_index], arr[low]

        pivot = arr[low]
        i = low + 1
        j = high

        while True:
            while i <= j and arr[i] <= pivot:
                comparisons[0] += 1
                i += 1
                if i > high:
                    break

            while i <= j and arr[j] > pivot:
                comparisons[0] += 1
                j -= 1

            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                break

        arr[low], arr[j] = arr[j], arr[low]
        return j

    def quicksort(low, high):
        if low < high:
            p = partition(low, high)
            quicksort(low, p - 1)
            quicksort(p + 1, high)

    quicksort(0, len(arr) - 1)
    return arr, comparisons[0]