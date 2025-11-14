import datetime
import os

TASK_FILE = "tasks.txt"

def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as f:
            data = f.readlines()
            return [task.strip() for task in data]
    return []

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        for t in tasks:
            f.write(t + "\n")

tasks = load_tasks()


GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def display_menu():
    print(f"\n{CYAN}======= UNIQUE TO-DO LIST APP ======={RESET}")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Clear All Tasks")
    print("5. Exit")

def add_task():
    task = input("Enter task description: ")
    priority = input("Priority (High/Medium/Low): ").capitalize()
    time_added = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")

    final_task = f"{task} | Priority: {priority} | Added: {time_added}"
    tasks.append(final_task)
    save_tasks(tasks)

    print(f"{GREEN} Task Added Successfully!{RESET}")

def view_tasks():
    if not tasks:
        print(f"{YELLOW}No tasks available.{RESET}")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{CYAN}{i}. {task}{RESET}")

def remove_task():
    view_tasks()
    if tasks:
        num = int(input("Enter task number to remove: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"{GREEN} Removed: {removed}{RESET}")
        else:
            print("Invalid choice.")

def clear_all():
    tasks.clear()
    save_tasks(tasks)
    print(f"{YELLOW} All tasks cleared!{RESET}")

def main():
    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            clear_all()
        elif choice == "5":
            print("Exiting... Bye ")
            break
        else:
            print("Invalid input, try again.")

if __name__ == "__main__":
    main()