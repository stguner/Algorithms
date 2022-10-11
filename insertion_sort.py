# Python program for Insertion Sort
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
 
#sorting the array 7, 50, 19, 5, 6 using insertionSort
numbers = [7, 50, 19, 5, 6]
insertionSort(numbers)
print("Sorted array is : ")
print(numbers)
 
 