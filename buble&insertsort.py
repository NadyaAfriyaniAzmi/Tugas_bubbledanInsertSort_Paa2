import time

def bubble_sort(arr):
    n = len(arr)
    swap_count = 0
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap_count += 1
    return swap_count

def insertion_sort(arr):
    n = len(arr)
    swap_count = 0
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            swap_count += 1
        arr[j + 1] = key
    return swap_count

# Kasus pengujian
arr = [5, 2, 1, 6, 3, 4]

# Bubble Sort
start_time = time.time()
bubble_swap_count = bubble_sort(arr)
end_time = time.time()
bubble_sort_time = end_time - start_time
print("Hasil Bubble Sort:", arr)
print("Waktu eksekusi Bubble Sort:", bubble_sort_time)

# Insertion Sort
start_time = time.time()
insertion_swap_count = insertion_sort(arr)
end_time = time.time()
insertion_sort_time = end_time - start_time
print("Hasil Insertion Sort:", arr)
print("Waktu eksekusi Insertion Sort:", insertion_sort_time)

# Kesimpulan
if bubble_sort_time < insertion_sort_time:
    print("Bubble Sort lebih cepat.")
elif bubble_sort_time > insertion_sort_time:
    print("Insertion Sort lebih cepat.")
else:
    print("Bubble Sort dan Insertion Sort memiliki waktu eksekusi yang sama.")

# Perbandingan jumlah pertukaran elemen dalam kasus terbaik
if bubble_swap_count < insertion_swap_count:
    print("Bubble Sort melakukan lebih sedikit pertukaran elemen dalam kasus terbaik.")
elif bubble_swap_count > insertion_swap_count:
    print("Insertion Sort melakukan lebih sedikit pertukaran elemen dalam kasus terbaik.")
else:
    print("Bubble Sort dan Insertion Sort melakukan jumlah pertukaran elemen yang sama dalam kasus terbaik.")
