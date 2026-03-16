def bubbleSort(arr):
    n = len(arr)
    comparisons = [0]

    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons[0] += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr, comparisons[0]