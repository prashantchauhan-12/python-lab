def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    L = arr[left:left + n1]
    R = arr[mid + 1:mid + 1 + n2]

    i = 0
    j = 0
    k = left
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = left + (right - left) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def main():
    # Read array size and elements
    size = int(input("Enter the number of elements: "))
    arr = [int(x) for x in input("Enter the elements: ").split()]
    
    if len(arr) != size:
        print("The number of entered elements does not match the specified size.")
        return

    # Display menu
    print("Choose sorting algorithm:")
    print("1. Bubble Sort")
    print("2. Merge Sort")
    print("3. Selection Sort")
    print("4. Insertion Sort")
    choice = int(input("Enter your choice (1-4): "))

    # Copy the array for each sort to avoid modifying the original input
    arr_copy = arr.copy()

    # Perform the sorting based on user's choice
    if choice == 1:
        bubble_sort(arr_copy)
        print("Sorted array using Bubble Sort:", arr_copy)
    elif choice == 2:
        merge_sort(arr_copy, 0, len(arr_copy) - 1)
        print("Sorted array using Merge Sort:", arr_copy)
    elif choice == 3:
        selection_sort(arr_copy)
        print("Sorted array using Selection Sort:", arr_copy)
    elif choice == 4:
        insertion_sort(arr_copy)
        print("Sorted array using Insertion Sort:", arr_copy)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
