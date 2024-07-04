import sys


def array_path(n: int, m: int) -> list[int]:
    """
    Вычисляет путь по круговому массиву из элементов от 1 до n с интервалом m.
    """
    array = list(range(1, n + 1))
    path = []
    current_index = 0

    while len(path) < n:
        path.append(array[current_index])
        current_index = (current_index + m - 1) % n
        if array[current_index] in path:
            break

    return path


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Запуск: python task1.py <n> <m>")
        sys.exit(1)

    n, m = int(sys.argv[1]), int(sys.argv[2])
    result = array_path(n, m)
    print(''.join(map(str, result)))
