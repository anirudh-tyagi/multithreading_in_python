import threading
import time
import random

def normal_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return normal_quicksort(left) + middle + normal_quicksort(right)

def threaded_quicksort(arr, depth=0, max_depth=3):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    if depth < max_depth:
        left_sorted = []
        thread = threading.Thread(target=lambda: left_sorted.extend(
            threaded_quicksort(left, depth + 1, max_depth)
        ))
        thread.start()
        right_sorted = threaded_quicksort(right, depth + 1, max_depth)
        thread.join()
        return left_sorted + middle + right_sorted
    else:
        return (threaded_quicksort(left, depth + 1, max_depth) +
                middle +
                threaded_quicksort(right, depth + 1, max_depth))

if __name__ == "__main__":
    arr_size = 100000  # Adjust the size based on your system's capability
    arr = [random.randint(0, 1000000) for _ in range(arr_size)]
    print(f"Array size: {arr_size}")

    # Normal quicksort
    start_time = time.time()
    sorted_normal = normal_quicksort(arr.copy())
    normal_time = time.time() - start_time
    print(f"Normal Quicksort Time: {normal_time:.4f} seconds")

    # Threaded quicksort
    start_time = time.time()
    sorted_threaded = threaded_quicksort(arr.copy(), max_depth=3)
    threaded_time = time.time() - start_time
    print(f"Threaded Quicksort Time: {threaded_time:.4f} seconds")

    # Verify correctness
    assert sorted_normal == sorted_threaded, "The sorted arrays do not match."
    print("Both sorted arrays match.")