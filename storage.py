import json
import os
from config import DATA_DIR, DATA_FILE


def initialize_storage():
    os.makedirs(DATA_DIR, exist_ok=True)

    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as file:
            json.dump([], file, indent=4)


def load_records():
    initialize_storage()

    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def save_records(records):
    initialize_storage()

    with open(DATA_FILE, "w") as file:
        json.dump(records, file, indent=4)
