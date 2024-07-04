import sys
import json


def read_json_file(filepath: str) -> dict[str, any]:
    """
    Читает данные из JSON файла и возвращает их в виде словаря.
    """
    with open(filepath, 'r') as file:
        return json.load(file)


def write_json_file(data: dict[str, any], filepath: str) -> None:
    """
    Записывает данные в JSON файл.
    """
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)


def build_value_lookup(values: dict[str, any]) -> dict[int, str]:
    """
    Строит словарь для быстрого доступа по ID и значению из данных values.json.
    """
    return {el["id"]: el["value"] for el in values["values"]}


def fill_values(
        tests: list[dict[str, any]], id_to_value_map: dict[int, str]) -> None:
    """
    Заполняет значения 'value' в тестах на основе карты ID к значениям.
    """
    for test in tests:
        if test["id"] in id_to_value_map:
            test["value"] = id_to_value_map[test["id"]]
        if "values" in test:
            fill_values(test["values"], id_to_value_map)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Использование: python task3.py <values.json> <tests.json>"
              " <report.json>")
        sys.exit(1)

    values_filepath = sys.argv[1]
    tests_filepath = sys.argv[2]
    report_filepath = sys.argv[3]

    values_data = read_json_file(values_filepath)
    tests_data = read_json_file(tests_filepath)

    value_lookup = build_value_lookup(values_data)
    fill_values(tests_data["tests"], value_lookup)

    write_json_file(tests_data, report_filepath)
