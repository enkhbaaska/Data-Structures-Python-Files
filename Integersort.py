def counting_sort(arr):
    # Find maximum value (m)
    m = max(arr)
    
    # Create count array A[0..m]
    count = [0] * (m + 1)
    
    # Count occurrences
    for i in range(len(arr)):
        count[arr[i]] += 1
    
    # Reconstruct sorted array
    result = []
    
    for i in range(m + 1):
        while count[i] > 0:
            result.append(i)
            count[i] -= 1
    
    return result

arr = [4, 2, 2, 8, 3, 3, 1]
print(counting_sort(arr))