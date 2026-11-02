from storage import initialize_storage

from maintenance_manager import (
    add_task,
    view_tasks,
    search_tasks,
    update_task_status,
    delete_task,
    view_overdue_tasks
)

from report_manager import show_report


def main():
    initialize_storage()

    while True:
        print("\n====================================")
        print("   HOME MAINTENANCE MANAGEMENT")
        print("====================================")

        print("1. Add Maintenance Task")
        print("2. View All Tasks")
        print("3. Search Tasks")
        print("4. Update Task Status")
        print("5. Delete Task")
        print("6. View Overdue Tasks")
        print("7. View Expense Report")
        print("8. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            search_tasks()

        elif choice == "4":
            update_task_status()

        elif choice == "5":
            delete_task()

        elif choice == "6":
            view_overdue_tasks()

        elif choice == "7":
            show_report()

        elif choice == "8":
            print("\nThank you for using the application!")
            break

        else:
            print("\nInvalid choice. Try again.")


if __name__ == "__main__":
    main()
