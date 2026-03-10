arr = [45, 78, 62, 90]

largest = arr[0]

for num in arr:
    if num > largest:
        largest = num

print("Largest number:", largest)