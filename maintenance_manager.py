from datetime import date

from storage import load_records, save_records
from utils import (
    get_next_id,
    input_required,
    input_date,
    input_amount,
    display_record
)


def add_task():
    records = load_records()

    print("\n--- ADD MAINTENANCE TASK ---")

    task = input_required("Enter task name: ")
    category = input_required("Enter category: ")
    description = input_required("Enter description: ")

    print("\n1. Low")
    print("2. Medium")
    print("3. High")

    priority_choice = input("Select priority: ").strip()

    priorities = {
        "1": "Low",
        "2": "Medium",
        "3": "High"
    }

    if priority_choice not in priorities:
        print("Invalid priority.")
        return

    due_date = input_date("Enter due date (YYYY-MM-DD): ")
    provider = input_required("Enter service provider: ")
    estimated_cost = input_amount("Enter estimated cost: ")

    record = {
        "id": get_next_id(records),
        "task": task,
        "category": category,
        "description": description,
        "priority": priorities[priority_choice],
        "due_date": due_date,
        "provider": provider,
        "estimated_cost": estimated_cost,
        "actual_cost": 0.0,
        "status": "Pending",
        "created_date": date.today().isoformat()
    }

    records.append(record)
    save_records(records)

    print("\nMaintenance task added successfully!")


def view_tasks():
    records = load_records()

    if not records:
        print("\nNo maintenance records found.")
        return

    print("\n--- ALL MAINTENANCE TASKS ---")

    for record in records:
        display_record(record)


def search_tasks():
    records = load_records()

    keyword = input_required(
        "Enter task name or category: "
    ).lower()

    results = [
        record for record in records
        if keyword in record["task"].lower()
        or keyword in record["category"].lower()
    ]

    if not results:
        print("\nNo matching tasks found.")
        return

    for record in results:
        display_record(record)


def update_task_status():
    records = load_records()

    try:
        task_id = int(input("Enter task ID: "))
    except ValueError:
        print("Enter a valid ID.")
        return

    record = next(
        (item for item in records if item["id"] == task_id),
        None
    )

    if not record:
        print("Task not found.")
        return

    print("\n1. Pending")
    print("2. In Progress")
    print("3. Completed")

    choice = input("Select new status: ").strip()

    statuses = {
        "1": "Pending",
        "2": "In Progress",
        "3": "Completed"
    }

    if choice not in statuses:
        print("Invalid status.")
        return

    record["status"] = statuses[choice]

    if record["status"] == "Completed":
        record["actual_cost"] = input_amount(
            "Enter actual expense: "
        )

    save_records(records)

    print("Task status updated successfully!")


def delete_task():
    records = load_records()

    try:
        task_id = int(input("Enter task ID to delete: "))
    except ValueError:
        print("Enter a valid ID.")
        return

    updated_records = [
        record for record in records
        if record["id"] != task_id
    ]

    if len(updated_records) == len(records):
        print("Task not found.")
        return

    save_records(updated_records)
    print("Task deleted successfully!")


def view_overdue_tasks():
    records = load_records()
    today = date.today()

    overdue = [
        record for record in records
        if record["status"] != "Completed"
        and date.fromisoformat(record["due_date"]) < today
    ]

    if not overdue:
        print("\nNo overdue maintenance tasks.")
        return

    print("\n--- OVERDUE TASKS ---")

    for record in overdue:
        display_record(record)
