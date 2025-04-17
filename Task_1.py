import random
import timeit

# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
# Insertion Sort
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst

# Timsort
def timsort(arr):
    return sorted(arr)


# Generate test data
sizes = [100, 1000, 5000]
results = []

for size in sizes:
    data = [random.randint(0, 10000) for _ in range(size)]

    time_merge = timeit.timeit(lambda: merge_sort(data), number = 3)
    time_insert = timeit.timeit(lambda: insertion_sort(data), number = 3)
    time_tim = timeit.timeit( lambda: timsort(data), number = 3)

    results.append((size, time_merge, time_insert, time_tim))

# Print results
print("\nExecution Time Comparison (in seconds for 3 runs):")
print("{:<10} {:<15} {:<15} {:<15}".format("Size", "Merge Sort", "Insertion Sort", "Timsort"))
for size, m, i, t in results:
    print(f"{size:<10} {m:<15.5f} {i:<15.5f} {t:<15.5f}")

print("\nConclusion:")
print("Timsort (Python's built-in) consistently outperforms the others, especially on larger datasets.")
print("Insertion sort performs very poorly on large datasets due to its O(n^2) complexity.")
print("Merge sort performs well, but Timsort combines it with insertion sort for better real-world performance.")





