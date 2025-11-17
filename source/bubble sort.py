def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
numbers_input = input("Введите элементы списка через пробел: ")
numbers = numbers_input.split()
numbers = [int(x) for x in numbers]
bubble_sort(numbers)
print("Отсортированный список:", numbers)