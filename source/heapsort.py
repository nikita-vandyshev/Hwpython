def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def siftdown(arr, i, upper):
    while True:
        left = 2 * i + 1
        right = 2 * i + 2

        if left >= upper:
            break

        largest = left
        if right < upper and arr[right] > arr[left]:
            largest = right

        if arr[i] >= arr[largest]:
            break

        swap(arr, i, largest)
        i = largest


def heapsort(arr):
    n = len(arr)

    for j in range((n - 2) // 2, -1, -1):
        siftdown(arr, j, n)

    for end in range(n - 1, 0, -1):
        swap(arr, 0, end)
        siftdown(arr, 0, end)


if __name__ == "__main__":
    sp = input("Введите элементы списка через пробел: ").strip()

    if sp == "":
        arr = []
    else:
        arr = [int(x) for x in sp.split()]

    print("Исходный список:", arr)
    heapsort(arr)
    print("Отсортированный список:", arr)
