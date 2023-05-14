import csv
import datetime
# name = input()
# body = input()
time = datetime.datetime.today()

def create_note():
    # функция для создания заметки
    with open("Notes.csv", "a", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        name = input()
        body = input()
        writer.writerow(["ggh", name, body, time])

def read_note():
#     # функция для чтения заметки
    with open("Notes.csv", newline="") as file:
        reader = csv.DictReader(file, delimiter=";")
        name = input()
        for row in reader:
            if (name == row["name"]):
                print(row["name"], " - ", row["body"], "(", row["id"], ",", row["time"], ")")


def read_notes():
    # функция для чтения списка заметок
    with open("Notes.csv", newline="") as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            print(row["name"], " - ", row["body"], "(", row["id"], ",", row["time"], ")")

# def edit_note():
#     # функция для редактирования заметки

def delete_note():
    # функция для удаления заметки

while True:
    user_input = input("Введите команду: ")
    if user_input == "create":
        create_note()
    elif user_input == "save":
        save_note()
    elif user_input == "read":
        read_note()
    elif user_input == "log":
        read_notes()
    elif user_input == "edit":
        edit_note()
    elif user_input == "delete":
        delete_note()
    else:
        print("Некорректная команда. Попробуйте снова.")