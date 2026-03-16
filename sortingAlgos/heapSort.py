def heapSort(arr) :
    n = len(arr)
    comparisons = [0]

    def heapify(arr, n, i) :
        largest = i
        l = 2*i + 1
        r = 2*i + 2

        if l < n and arr[l] > arr[largest] :
            comparisons[0] += 1
            largest = l
        if r < n and arr[r] > arr[largest] :
            comparisons[0] += 1
            largest = r

        if largest != i :
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    for i in range(n // 2 - 1, -1, -1) :
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1) :
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr, comparisons[0]

