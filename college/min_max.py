arr = [1,2,4,7,5,9]

min = arr[0]
max = arr[0]

for i in range(1, len(arr)):
    if arr[i] > min:
        min = arr[i]
    if arr[i] < max:
        max = arr[i]
print("Minimum = ", min)
print("Maximum = ", max)