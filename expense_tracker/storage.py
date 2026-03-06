import json

file_name = "expenses.json"

def load_expense():
    try:
        with open(file_name, mode="r", encoding="utf-8") as file:
            data = list(json.load(file))
            return data
    except FileNotFoundError:
        return []

def save_expense(liste):
    with open(file_name, mode="w", encoding="utf-8") as file:
        json.dump(liste, file, indent=4)
