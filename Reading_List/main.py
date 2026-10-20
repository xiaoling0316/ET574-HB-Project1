"""
main.py - Entry point and main menu loop for Workout Log Tracker.
"""

import tracker


def display_menu():
    print("Welcome to Workout Log Tracker!")
    print("1. Add Workout")
    print("2. View All Workouts")
    print("3. View Summary")
    print("4. Exit")


def main():
    while True:
        display_menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            tracker.add_workout()
        elif choice == "2":
            tracker.view_all_workouts()
        elif choice == "3":
            tracker.summary_report()
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select an option from 1 to 4.\n")


if __name__ == "__main__":
    main()