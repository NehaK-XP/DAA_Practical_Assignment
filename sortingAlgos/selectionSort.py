def selectionSort(arr):
    n = len(arr)
    comparisons = [0]

    for i in range(n):
        min_idx = i

        for j in range(i + 1, n):
            comparisons[0] += 1
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr, comparisons[0]