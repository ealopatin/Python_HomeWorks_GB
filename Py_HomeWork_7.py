def enter_first_name():
    return input("Ведите имя: ").title()


def enter_second_name():
    return input("Введите фамилию: ").title()


def enter_family_name():
    return input("Введите отчество: ").title()


def enter_phone_number():
    return input("Введите номер телефона: ")


def enter_adress_number():
    return input("Введите адрес: ").title()

def enter_data():
    name = enter_first_name()
    surname = enter_second_name()
    family = enter_family_name()
    phone_number = enter_phone_number()
    address = enter_adress_number()
    with open("boox.txt", "a", encoding="utf-8") as file:
        file.write(f"{name} {surname} {family}\n{phone_number}\n{address}\n\n")

def print_data():
    with open("boox.txt", "r", encoding="utf-8") as file:
        print(file.read())

def search_line():
    print(
        "Введите вариант поиска:\n"
        "1. Имя\n"
        "2. Фамилия\n"
        "3. Отчество\n"
        "4. Телефон\n"
        "5. Адрес"
    )
    index = int(input("Введите вариант: ")) - 1

    searched = input("Введите поисковые данные: ").title()
    with open("boox.txt", "r", encoding="utf-8") as file:
        data = file.read().strip().split("\n\n")
    for item in data:
        new_item = item.replace("\n", " ").split()
    if searched in new_item[index]:
        print(item)
        print()
        # file.seek(0)
        # print([file.readlines()])

def edit_data():

def delete_data():

def interface():
    cmd = 0
    while cmd != "6":
        print(
            "Варианты действия: \n"
            "1. Добавить контакт \n"
            "2. Вывести все контакты \n"
            "3. Поиск контакта \n"
            "4. Редактировать контакт"
            "5. Удалить контакт"
            "6. Выход \n"
        )
        cmd = input("Введите действие: ")
        while cmd not in ("1", "2", "3", "4"):
            print("Некорректный ввод")
            cmd = input("Введите действие: ")
        match cmd:
            case "1":
                enter_data()
            case "2":
                print_data()
            case "3":
                search_line()
            case "4":
                ....
            case "5":
                ....
            case "6":
                print("Goodbuye!")

# # search_line()
# # print_data()
# # enter_data()
interface()