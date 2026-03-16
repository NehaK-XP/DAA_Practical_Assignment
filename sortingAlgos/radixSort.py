def radixSort(arr):
    max_num = max(arr)
    exp = 1             # represents the current digit place

    while max_num // exp > 0 :
        n = len(arr)
        output = [0] * n
        count = [0] * 10    # for digits 0-9
        # count the occurence of each digit
        for num in arr :
            index = (num // exp) % 10
            count[index] += 1
        # convert count to the actual positions
        for i in range(1, 10) :
            count[i] += count[i - 1]
        # build output array (stable sort)
        for i in range(n - 1, -1, -1) :
            index = (arr[i] // exp) % 10 
            output[count[index] - 1] = arr[i]
            count[index] -= 1
        # copy output back to arr
        for i in range(n) :
            arr[i] = output[i]
        # move to next digits place
        exp *= 10

    return arr, 0

