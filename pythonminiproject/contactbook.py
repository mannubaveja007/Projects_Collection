import csv
import os
FILENAME = "contactt.csv"
if not os.path.exists(FILENAME):
    with open(FILENAME,"w",encoding = "utf-8") as f:
        write = csv.writer(f)
        write.writerow(["Name","mobile no","email"])
def add_contact():
    name = input("Enter your name :- ").lower().strip()
    mobile = int(input("enter your mobile no :- "))
    email = input("enter your email")
    with open(FILENAME,"r",encoding = "utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Name"].lower() == name :
                print("Cntact name already exit")
                return
    with open(FILENAME,"a",encoding = "utf-8") as f:    
        writer = csv.writer(f)
        writer.writerow([name,mobile,email])
        print("contact Book added ")
def view_contact():
    with open(FILENAME,"r",encoding = "utf-8") as f:
        readerr = list(csv.reader(f))
        row = list(readerr)
        if len(row) < 1:
            print("NO contact")
            return
        for row in readerr[1:]:
            print(f"{row[0]},{row[1]},{row[2]}")
def main():
    while True:
        choice = """
        Welcome to Contact Book App
        1. Add contact
        2 . view contact
        """
        print(choice)
        choicee = int(input("Enter the option from 1-2 :- "))
        if choicee == 1:
            add_contact()
        elif choicee == 2:
            view_contact()
        else:
            print("Invalid option")

main()
