import csv

FILENAME = "thethird.csv"

def main():

    while True:
        print("\n1. add expense")
        print("2. view expeses")
        print("3. exit")

        choice = input("enter an option").strip()

        if choice == 1:
            print("add expese")

        elif choice == 2:
            print("view expeses")

        elif choice == 3:
            print("exiting")
            break
        
        else:
            print("invalid option")
        

def add_expense():

    category = input("what is the category (food, transport), etc.").strip()
    amount = float(input("what is the expense ?"))

    if categorry and amount > 0:
        with open (FILENAME, mode = "a", newline = "") as file:
            writer = csv.writer(file)
            writer.writerow([category, amount])
            print("expense added succesfully")


def show_expense():
    try:
        with open(FILENAME, mode = "r", newline = "") as file:
            reader = csv.reader(file)
            expense = list(reader)

            if not expense: 
                print("no expense")
                return

            for index, row in enumerate(expense, 1):
                if row: 
                    print(f"{index}". row{[0]}: $row{[1]}")

    except FileNotFoundError:
        print("No File Found")

if __name__ == "__main__":
    main()
       
