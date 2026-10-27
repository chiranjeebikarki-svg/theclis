import csv

FILENAME = "thesecond.csv"

def main():
    while True:
        print("\n1. view taks")
        print("2. add task")
        print("3. remove task")
        print("4. update task")
        print("5. exit")

        choice = input("enter an option: ").strip()

        if choice == "1":
            show_list()

        elif choice == "2":
            add_task()

        elif choice == "3":
            delete_task()

        elif choice == "4":
            update_task()

        elif choice == "5":
            print("exiting")
            break

        else:
            print("correct entry only, redo")
                

def add_task():
    adding = input("what is the task? ").strip()
    
    if adding:
        with open(FILENAME, "a", newline = "") as file:
            writer = csv.writer(file)
            writer.writerow([adding])
            print("task added succesfully")

def delete_task():   
    pass     
        
def update_task():
    pass
        
def show_list():
    try:

        with open(FILENAME, mode = "r", newline = "") as file:
            reader = csv.reader(file)
            tasks = list(reader)

            if not tasks:
                print("tasks not found")
                return

            for index, row in enumerate(tasks, 1):
                if row:
                    print(f"{index}. {row[0]} ")

    except FileNotFoundError:
        print("No tasks added yet")

if __name__ == "__main__":
    main()
