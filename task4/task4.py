import sys
import statistics


def load_nums(filepath: str) -> list[int]:
    """
    Загружает числа из файла и возвращает их в виде списка целых чисел.
    """
    with open(filepath, 'r') as file:
        nums = [int(line.strip()) for line in file.readlines()]
    return nums


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python task4.py <input_file>")
        sys.exit(1)

    file = sys.argv[1]
    nums = load_nums(file)

    median_num = statistics.median(nums)
    moves = int(sum(abs(num - median_num) for num in nums))

    print(moves)
