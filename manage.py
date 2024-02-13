from contacts.view import read_contact_from_file, write_contact_to_file, change_contact_to_file, search_contact_by_key

def start():
    while True:
        print()
        print("ВЫБЕРЕТЕ ОДНУ ИЗ ОПЦИЙ:")
        print()
        print("1. Прочитать все контакты")
        print("2. Добавить новый контакт")
        print("3. Изменить существующий контакт")
        print("4. Поиск контакта по ключевым данным")
        print("5. Завершить")
        print()
        option = input("ВАШ ВЫБОР: ")

        if option == '1':
            read_contact_from_file()
            continue
        elif option == '2':
            write_contact_to_file()
            continue
        elif option == '3':
            change_contact_to_file()
            continue
        elif option == '4':
            search_contact_by_key()
            continue
        elif option == '5':
            break
        else:
            print("Введен неверный параметр, попробуйте еще раз.")

start()