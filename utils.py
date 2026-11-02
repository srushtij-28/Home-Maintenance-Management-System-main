from datetime import datetime


def get_next_id(records):
    if not records:
        return 1

    return max(record["id"] for record in records) + 1


def input_required(message):
    while True:
        value = input(message).strip()

        if value:
            return value

        print("This field cannot be empty.")


def input_date(message):
    while True:
        value = input(message).strip()

        try:
            datetime.strptime(value, "%Y-%m-%d")
            return value
        except ValueError:
            print("Enter date in YYYY-MM-DD format.")


def input_amount(message):
    while True:
        try:
            amount = float(input(message))

            if amount < 0:
                print("Amount cannot be negative.")
                continue

            return round(amount, 2)

        except ValueError:
            print("Enter a valid amount.")


def display_record(record):
    print("-" * 65)
    print(f"ID                : {record['id']}")
    print(f"Task              : {record['task']}")
    print(f"Category          : {record['category']}")
    print(f"Description       : {record['description']}")
    print(f"Priority          : {record['priority']}")
    print(f"Due Date          : {record['due_date']}")
    print(f"Service Provider  : {record['provider']}")
    print(f"Estimated Expense : Rs. {record['estimated_cost']:.2f}")
    print(f"Actual Expense    : Rs. {record['actual_cost']:.2f}")
    print(f"Status            : {record['status']}")
