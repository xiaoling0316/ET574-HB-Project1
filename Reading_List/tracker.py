"""
tracker.py - Core operations for logging, viewing, and calculating workout metrics.
"""

import data


def add_workout():
    workout_type = input("Enter workout type: ").strip()
    while not workout_type:
        print("Workout type cannot be blank.")
        workout_type = input("Enter workout type: ").strip()

    while True:
        duration_input = input("Enter duration (minutes): ").strip()
        try:
            duration = int(duration_input)
            if duration <= 0:
                print("Duration must be a positive number greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a whole number for minutes.")

    # Access lists via data.<list_name>
    data.workout_types.append(workout_type)
    data.workout_durations.append(duration)
    print("Workout recorded!\n")


def view_all_workouts():
    if not data.workout_types:
        print("\nNo workouts recorded yet.\n")
        return

    print("\n--- All Workouts ---")
    for i in range(len(data.workout_types)):
        print(f"{i + 1}. Type: {data.workout_types[i]} | Duration: {data.workout_durations[i]} mins")
    print("--------------------\n")


def summary_report():
    if not data.workout_durations:
        print("\nNo workout data available to generate a summary.\n")
        return

    total_time = sum(data.workout_durations)
    count = len(data.workout_durations)
    avg_duration = total_time / count
    longest_workout = max(data.workout_durations)
    shortest_workout = min(data.workout_durations)

    print("\n--- Summary Report ---")
    print(f"Total time spent:          {total_time} minutes")
    print(f"Number of workouts:        {count}")
    print(f"Average duration:          {avg_duration:.2f} minutes")
    print(f"Longest workout duration:  {longest_workout} minutes")
    print(f"Shortest workout duration: {shortest_workout} minutes")
    print("----------------------\n")