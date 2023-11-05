import json
FILENAME = "input.json"
def task() -> float:
        with open(FILENAME) as file:
            data = json.load(file)
        total_score_weight = 0
        for item in data:
            score = item["score"]
            weight = item["weight"]
            total_score_weight += score * weight
        return round(total_score_weight, 3)

print(task())
