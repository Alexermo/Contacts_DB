from contacts.view import read_contact_from_file, write_contact_to_file, change_contact_to_file, search_contact_by_key


def start():
    """
    Запускает главный цикл программы, в котором предлагает пользователю выбор одной из пяти опций.
    Если происходит ошибка, она отлавливается и выводится на экран.
    """
    try:
        # Главный цикл программы
        while True:
            print()
            print("ВЫБЕРЕТЕ ОДНУ ИЗ ОПЦИЙ:")
            print()
            print("1. Показать все контакты")
            print("2. Добавить новый контакт")
            print("3. Изменить существующий контакт")
            print("4. Поиск контакта по ключевым данным")
            print("5. Завершить")
            print()

            option = input("ВАШ ВЫБОР: ")

            if option == '1':
                read_contact_from_file()
            elif option == '2':
                write_contact_to_file()
            elif option == '3':
                change_contact_to_file()
            elif option == '4':
                search_contact_by_key()
            elif option == '5':
                break
            else:
                print("Введен неверный параметр, попробуйте еще раз.")

    except Exception as e:
        print(f"Произошла ошибка: {e}")


start()