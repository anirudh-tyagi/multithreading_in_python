# Concurrency Assignment: Multi-threaded Python Programming

This repository contains solutions to three multithreading tasks implemented in Python. These assignments demonstrate how concurrency can be applied to improve the performance of computational and I/O-bound operations. All programs were developed and tested in a dedicated Python virtual environment named `multithreading`.

## Python Environment

To maintain clean dependencies, a separate virtual environment was created for this project:

```bash
python -m venv multithreading
source multithreading/bin/activate  # On Windows: multithreading\Scripts\activate
pip3 install requests
```

> **Note**: Only the `requests` library is required for the downloader script.

## 1. Multi-threaded Merge Sort

**Objective:**  
Implement a merge sort algorithm that utilizes multiple threads to perform sorting concurrently.

**Approach:**  
- Uses recursive merge sort logic with threading for parallel sorting of subarrays.
- A `max_depth` parameter limits thread creation to prevent overhead.
- Benchmarked against a standard single-threaded merge sort implementation.
- Verified output accuracy using array comparison.

## 2. Multi-threaded Quicksort

**Objective:**  
Create a quicksort implementation that uses threads to sort subarrays concurrently.

**Approach:**  
- Applies classic quicksort logic with partitioning around a pivot.
- Threads are used to sort one of the partitions concurrently up to a `max_depth` limit.
- Balances thread usage to avoid resource saturation.
- Compared with a normal quicksort for both speed and correctness.

## 3. Concurrent File Downloader

**Objective:**  
Write a program that downloads multiple files concurrently using threads and compare it to a sequential downloader.

**Approach:**  
- Accepts file URLs via command-line arguments or a `.txt` file.
- Implements sequential and threaded download functions.
- Downloads are executed concurrently by creating one thread per URL.
- Threads are joined to ensure synchronized execution.
- Measures and compares total execution time for both methods.

**Sample Output:**
```
--- Comparison ---
Sequential Time: 3.55 sec
Concurrent Time: 0.58 sec
Concurrent download was 6.09x faster!
```

---

## How to Run

### 1. Activate the environment
```bash
source multithreading/bin/activate  # or multithreading\Scripts\activate on Windows
```

### 2. Execute the scripts
```bash
python merge_sort.py
python quicksort.py
python downloader.py urls.txt
```

---

## Performance Notes

- **CPU-bound tasks (Sorting):** Threads can offer moderate gains due to parallel computation, though limited by Python's Global Interpreter Lock (GIL).
- **I/O-bound tasks (Downloading):** Multithreading significantly improves performance by allowing overlapping I/O operations.
- Thread depth and management are critical in all cases to avoid excessive overhead.

---

## Requirements

```
requests
```

Create a `requirements.txt`:
```bash
echo requests > requirements.txt
```

---

## License

This project is provided for educational purposes and is licensed under the MIT License.
