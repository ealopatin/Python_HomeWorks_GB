# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной
# записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной


def show_menu():
    print(
        "   Главное меню:\n"
        "1. Отобразить весь справочник\n"
        "2. Найти абонента по фамилии\n"
        "3. Найти абонента по номеру телефона\n"
        "4. Добавить абонента в справочник\n"
        "5. Изменить данные абонента в справочнике\n"
        "6. Удалить данные абонента в справочнике\n"
        "0. Закончить работу\n"
        "Выберите необходимое действие: "
    )
    choice = int(input())
    print()
    return choice


def work_with_phonebook():
    choice = show_menu()
    phone_book = read_csv("phonebook.csv")

    while choice != 0:
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            name = get_search_name()
            print(find_by_name(phone_book, name))
        elif choice == 3:
            number = get_search_number()
            print(find_by_number(phone_book, number))
        elif choice == 4:
            user_data = get_new_user()
            add_user(phone_book, user_data)
            write_csv("phonebook.csv", phone_book)
            print("Абонент успешно добавлен")
        elif choice == 5:
            modified, phone_book = change_user(phone_book)
            if modified:
                write_csv("phonebook.csv", phone_book)
                print("Данные изменены")
        elif choice == 6:
            name = get_search_name()
            modified, phone_book = delete_user(phone_book, find_index(phone_book, name))
            if modified:
                write_csv("phonebook.csv", phone_book)
                print("Абонент удален")
        choice = show_menu()
    print("GoodBye!")


def write_csv(filename: str, data: list):
    with open(filename, "w", encoding="utf-8") as fout:
        for i in range(len(data)):
            s = ""
            for v in data[i].values():
                s += v + ","
            fout.write(f"{s[:-1]}\n")


def read_csv(filename: str) -> list:
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, "r", encoding="utf-8") as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(",")))
            data.append(record)
    return data


def print_result(phone_book):
    for i in range(len(phone_book)):
        print(
            phone_book[i]["Фамилия"],
            phone_book[i]["Имя"],
            phone_book[i]["Телефон"],
            phone_book[i]["Описание"],
        )


def get_search_name():
    second_name = input("Введите фамилию: ")
    return second_name


def find_by_name(phone_book, name):
    for i in phone_book:
        if i.get("Фамилия").lower() == name.lower():
            return f'{i.get("Имя")}, {i.get("Телефон")}, {i.get("Описание")}'
    return "Контакт не найден"


def get_search_number():
    phone_num = input("Введите телефон: ")
    return phone_num


def find_by_number(phone_book, number):
    for i in phone_book:
        if i.get("Телефон") == number:
            return f'{i.get("Фамилия")}, {i.get("Имя")}, {i.get("Описание")}'
    return "Контакт не найден"


def get_new_user():
    new_user = {}
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    for i in fields:
        new_user[i] = input(i + "\n")
    return new_user


def add_user(phone_book, user_data):
    phone_book.append(user_data)


def write_txt(filename: str, data: list):
    with open(filename, "w", encoding="utf-8") as fout:
        for i in range(len(data)):
            s = ""
            for v in data[i].values():
                s += v + ","
            fout.write(f"{s[:-1]}\n")


def change_user(phone_book):
    index = find_index(phone_book, get_search_name())
    if index < 0:
        print("Абонент не найден")
        return False, phone_book
    print("Введите новые данные абонента")
    return True, change_record(phone_book, index, get_new_user())


def find_index(phone_book, second_name):
    for i in range(len(phone_book)):
        if phone_book[i]["Фамилия"].lower() == second_name.lower():
            return i
    return -1


def change_record(phone_book, i, record):
    return phone_book[:i] + [record] + phone_book[i + 1 :]


def delete_user(phone_book, i):
    if i < 0:
        print("Абонент не найден")
        return False, phone_book
    return True, phone_book[:i] + phone_book[i + 1 :]


work_with_phonebook()
