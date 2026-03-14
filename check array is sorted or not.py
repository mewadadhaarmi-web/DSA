# Check if array is sorted

arr = [1, 3, 5, 7, 9]

is_sorted = True

for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
        is_sorted = False
        break

if is_sorted:
    print("Array is Sorted")
else:
    print("Array is Not Sorted")