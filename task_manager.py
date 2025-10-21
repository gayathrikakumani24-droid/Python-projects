tasks=[]
def display_menu():
    print("\n===Task Manager===")
    print("1. Add Task")
    print("2. View Task")
    print("3. Complete Task")
    print("4. Delete Task")
    print("0. Exit")
def add_task():
    title=input("Enter the Task: ")
    tasks.append({"title":title,"completed":False})
    print(f"Task {title} added successfully!")
def view_task():
    if not tasks:
        print("No tasks found")
        return
    print("\n=== MY TASKS ===")
    for index,task in enumerate(tasks):
        status="*" if task["completed"] else " "
        print(f"{index+1}. [{status}] {task["title"]}")
def complete_task():
    if not tasks:
        return
    try:
        task_number=int(input("Enter task number to mark as completed: "))
        task_completed=tasks[task_number-1]
        task_completed["completed"]=True
        print(f"Task {task_completed["title"]} marked as completed!")
    except ValueError:
        print("Enter a valid number")

def delete_task():
    task_number=int(input("Enter the task number to delete: "))
    deleted_task=tasks.pop(task_number-1)
    print(f"{deleted_task["title"]} deleted successfully!")
def main():
    while True:
        display_menu()
        choice=int(input("Enter your choice(0-4): "))
        if(choice==1):
            add_task()
        elif(choice==2):
            view_task()
        elif(choice==3):
            complete_task()
        elif(choice==4):
            delete_task()
        elif(choice==0):
           exit()
           break
        else:
            print("Enter a valid choice from (0-4)")
main()
        