# Написать программу на Python в любой парадигме для бинарного поиска.
# На вход подаётся целочисленный массив и число.
# На выходе - индекс элемента или -1, в случае если искомого элемента нет в массиве.

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 3

result = binary_search(arr, target)
print(result)  # Выводит: 2

# Если искомый элемент найден в массиве, функция вернет его индекс.
# В противном случае, функция вернет -1.

