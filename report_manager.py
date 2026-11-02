from storage import load_records


def show_report():
    records = load_records()

    total = len(records)

    pending = sum(
        1 for record in records
        if record["status"] == "Pending"
    )

    in_progress = sum(
        1 for record in records
        if record["status"] == "In Progress"
    )

    completed = sum(
        1 for record in records
        if record["status"] == "Completed"
    )

    estimated_total = sum(
        record["estimated_cost"] for record in records
    )

    actual_total = sum(
        record["actual_cost"] for record in records
    )

    print("\n========== MAINTENANCE REPORT ==========")
    print(f"Total Tasks       : {total}")
    print(f"Pending Tasks     : {pending}")
    print(f"In Progress Tasks : {in_progress}")
    print(f"Completed Tasks   : {completed}")
    print("----------------------------------------")
    print(f"Estimated Expense : Rs. {estimated_total:.2f}")
    print(f"Actual Expense    : Rs. {actual_total:.2f}")
    print("========================================")
