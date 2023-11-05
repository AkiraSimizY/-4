import json
import csv
from collections import OrderedDict
INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"
def task() -> None:
    with open(INPUT_FILENAME, 'r') as file:
        reader = csv.DictReader(file)
        records = []
        for row in reader:
            record = {}
            for column, value in row.items():
                record[column] = value
            records.append(record)
    json_data = json.dumps(records, indent=4)
    with open(OUTPUT_FILENAME, "w", encoding="utf-8") as f:
        f.write(json_data)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")