# todo_app.py
import os

TODO_FILE = "todo_list.txt"

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r", encoding="utf-8") as file:
            return [line.strip() for line in file.readlines()]
    return []

def save_tasks(tasks):
    with open(TODO_FILE, "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("No tasks yet. Taking it easy, huh?")
    else:
        print("\n=== Your Todo List ===")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print("====================\n")

def main():
    tasks = load_tasks()
    while True:
        print("\nOptions: [1] Add task [2] Show tasks [3] Delete task [4] Quit")
        choice = input("What’s your move? (1-4): ")

        if choice == "1":
            task = input("What task to add?: ")
            tasks.append(task)
            save_tasks(tasks)
            print(f"Added '{task}'. Let’s tackle it together!")

        elif choice == "2":
            show_tasks(tasks)

        elif choice == "3":
            show_tasks(tasks)
            if tasks:
                num = int(input("Which task to delete?: ")) - 1
                if 0 <= num < len(tasks):
                    removed = tasks.pop(num)
                    save_tasks(tasks)
                    print(f"Deleted '{removed}'. Nice work!")
                else:
                    print("That number doesn’t exist. Tired eyes?")
        
        elif choice == "4":
            print("See ya! Good job today!")
            break

        else:
            print("Pick 1-4, buddy. Lost in the options?")

if __name__ == "__main__":
    main()