
import os
from datetime import datetime

TODO_FILE = "todo_list.txt"

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r", encoding="utf-8") as file:
            return [line.strip().split("|") for line in file.readlines()]
    return []

def save_tasks(tasks):
    with open(TODO_FILE, "w", encoding="utf-8") as file:
        for task in tasks:
            file.write("|".join(task) + "\n")

def is_current_task(start_week, end_week):
    today = datetime.now().strftime("%Y%m")  # ???????: 202503?
    return start_week <= today <= end_week

def show_tasks(tasks):
    if not tasks:
        print("No tasks yet. Taking it easy, huh?")
    else:
        print("\n=== Your Todo List ===")
        for i, task in enumerate(tasks, 1):
            task_name, start_week, end_week = task
            current = " [Now Working!]" if is_current_task(start_week, end_week) else ""
            print(f"{i}. {task_name} (Start: {start_week}, End: {end_week}){current}")
        print("====================\n")

def validate_week(week):
    try:
        datetime.strptime(week, "%Y%m")
        return True
    except ValueError:
        return False

def main():
    tasks = load_tasks()
    while True:
        print("\nOptions: [1] Add task [2] Show tasks [3] Delete task [4] Quit")
        choice = input("What’s your move? (1-4): ")

        if choice == "1":
            task = input("What task to add?: ")
            start_week = input("Start week (yyyymm, e.g., 202503): ")
            end_week = input("End week (yyyymm, e.g., 202504): ")
            
            if validate_week(start_week) and validate_week(end_week) and start_week <= end_week:
                tasks.append([task, start_week, end_week])
                save_tasks(tasks)
                print(f"Added '{task}' (Start: {start_week}, End: {end_week}). Let’s tackle it together!")
            else:
                print("Invalid weeks or start week is after end week. Time travel isn’t an option yet!")

        elif choice == "2":
            show_tasks(tasks)

        elif choice == "3":
            show_tasks(tasks)
            if tasks:
                num = int(input("Which task to delete?: ")) - 1
                if 0 <= num < len(tasks):
                    removed = tasks.pop(num)
                    save_tasks(tasks)
                    print(f"Deleted '{removed[0]}'. Nice work!")
                else:
                    print("That number doesn’t exist. Tired eyes?")
        
        elif choice == "4":
            print("See ya! Good job today!")
            break

        else:
            print("Pick 1-4, buddy. Lost in the options?")

if __name__ == "__main__":
    main()