import threading
import time
import random

def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged += left[i:]
    merged += right[j:]
    return merged

def normal_merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = normal_merge_sort(arr[:mid])
    right = normal_merge_sort(arr[mid:])
    return merge(left, right)

def threaded_merge_sort(arr, max_depth=3):
    def sort_helper(arr, depth):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = []
        right = []
        if depth < max_depth:
            t1 = threading.Thread(target=lambda: left.extend(sort_helper(arr[:mid], depth + 1)))
            t2 = threading.Thread(target=lambda: right.extend(sort_helper(arr[mid:], depth + 1)))
            t1.start()
            t2.start()
            t1.join()
            t2.join()
        else:
            left = sort_helper(arr[:mid], depth + 1)
            right = sort_helper(arr[mid:], depth + 1)
        return merge(left, right)
    return sort_helper(arr, 0)

if __name__ == "__main__":
    # Generate a large array of random integers
    arr_size = 10000  # Adjust size based on your system's capability
    arr = [random.randint(0, 100000) for _ in range(arr_size)]
    print(f"Array size: {arr_size}")
    
    # Normal merge sort
    start_time = time.time()
    sorted_normal = normal_merge_sort(arr.copy())
    normal_time = time.time() - start_time
    print(f"Normal Merge Sort Time: {normal_time:.4f} seconds")
    
    # Threaded merge sort with max_depth=3
    start_time = time.time()
    sorted_threaded = threaded_merge_sort(arr.copy(), max_depth=3)
    threaded_time = time.time() - start_time
    print(f"Threaded Merge Sort Time: {threaded_time:.4f} seconds")
    
    # Verify correctness
    assert sorted_normal == sorted_threaded, "The sorted arrays do not match."
    print("Both sorted arrays match.")