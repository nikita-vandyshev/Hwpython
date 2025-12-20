def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


if __name__ == "__main__":
    numbers_input = input("Введите элементы списка через пробел: ")
    numbers = [int(x) for x in numbers_input.split()]
    bubble_sort(numbers)
    print("Отсортированный список:", numbers)
