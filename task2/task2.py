import sys
import math


def read_circle_data(filename: str) -> tuple[float, float, float]:
    """
    Читает данные о круге из файла и возвращает координаты центра и радиус.
    """
    with open(filename, 'r') as f:
        center_x, center_y = map(float, f.readline().strip().split())
        radius = float(f.readline().strip())
    return center_x, center_y, radius


def read_points_data(filename: str) -> list[tuple[float, float]]:
    """
    Читает данные точек из файла и возвращает список координат точек.
    """
    points = []
    with open(filename, 'r') as f:
        for line in f:
            x, y = map(float, line.strip().split())
            points.append((x, y))
    return points


def find_position(center_x: float, center_y: float, radius: float,
                  point_x: float, point_y: float) -> int:
    """
    Определяет положение точки относительно круга.

    Возвращает:
    int: 0 - точка лежит на окружности,
         1 - точка внутри окружности,
         2 - точка снаружи окружности.
    """
    distance_squared = (point_x - center_x) ** 2 + (point_y - center_y) ** 2
    radius_squared = radius ** 2

    if math.isclose(distance_squared, radius_squared):
        return 0
    elif distance_squared < radius_squared:
        return 1
    else:
        return 2


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Использование: python task2.py <circle_data_file> "
              "<points_data_file>")
        sys.exit(1)

    circle_file, points_file = sys.argv[1], sys.argv[2]

    center_x, center_y, radius = read_circle_data(circle_file)
    points = read_points_data(points_file)

    results = []
    for point_x, point_y in points:
        position = find_position(center_x, center_y, radius, point_x, point_y)
        results.append(position)

    for result in results:
        print(result)
