# Task1 To Do List
class To_Do_List:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        self.tasks[len(self.tasks) + 1] = task
        print(f'Task "{task}" added successfully.')

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("Tasks:")
            for task_id, task in self.tasks.items():
                print(f"{task_id}. {task}")

    def update_task(self, task_id, new_task):
        if task_id in self.tasks:
            self.tasks[task_id] = new_task
            print(f'Task {task_id} updated successfully.')
        else:
            print(f'Task {task_id} not found.')

    def delete_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
            print(f'Task {task_id} deleted successfully.')
        else:
            print(f'Task {task_id} not found.')


def main():
    to_do_list = To_Do_List()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task = input("Enter the task you want: ")
            to_do_list.add_task(task)
        elif choice == '2':
            to_do_list.view_tasks()
        elif choice == '3':
            task_id = int(input("Enter the task ID to update it: "))
            new_task = input("Enter the new task of your choice: ")
            to_do_list.update_task(task_id, new_task)
        elif choice == '4':
            task_id = int(input("Enter the task ID to delete it: "))
            to_do_list.delete_task(task_id) 
        elif choice == '5':
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1-5.")


if __name__ == "__main__":
    main()