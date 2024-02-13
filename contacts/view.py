import json
from contacts.models import Contact


# contacts = 'contacts_bd.txt'

def read_contact_from_file():
    """
    Функция для чтения файла контактов и вывода информации о контактах.
    Файл должен быть в формате JSON и содержать список контактов, где каждый контакт - это словарь.

    Ключи и значения для каждого контакта выводятся на одной строке, разделенные запятыми.

    Если с файлом произошла ошибка (например, если его не существует,
    он поврежден или не соответствует ожидаемому формату JSON), функция будет
    выводить сообщение об ошибке.

    Функция не принимает никаких аргументов и не возвращает никаких значений.
    """
    try:
        with open('contacts_bd.txt', 'r') as file:
            contact_data = json.load(file)
            print()
            print('РЕЗУЛЬТАТ ПОИСКА')
            for contact in contact_data:
                contact_info = ", ".join(f"{k}: {v}" for k, v in contact.items())
                print(contact_info)
    except Exception as e:
        print(f"Произошла ошибка: {e}")


def write_contact_to_file():
    """
        Функция для создания нового контакта и добавления его в файл контактов.

        Ваш файл контактов должен быть в формате JSON и содержать список контактов,
        где каждый контакт представлен в форме словаря.

        Если файл контактов не существует или он пуст, функция создаст новый список контактов.

        Функция использует метод 'create_contact' класса 'Contact' для создания нового контакта,
        а также метод 'to_dict' того же класса для преобразования контакта в словарь перед
        сохранением в файл.

        Функция не принимает никаких аргументов и не возвращает никаких значений. Она непосредственно
        влияет на содержимое файла 'contacts_bd.txt'.
        """
    new_contact = Contact.create_contact()
    with open('contacts_bd.txt', 'r') as file:
        content = file.read()
        contacts = json.loads(content) if content else []

    contacts.append(new_contact.to_dict())

    with open('contacts_bd.txt', 'w') as file:
        json.dump(contacts, file)


def change_contact_to_file():
    """
        Функция для изменения контакта или его удаления из файла контактов.

        Функция сначала считывает данные из файла контактов, затем предоставляет
        пользователю возможность выбрать контакт по его идентификатору.

        Если контакт найден, функция показывает пользователю меню настроек,
        предлагающее изменить определенные поля контакта, удалить контакт
        или отказаться от изменений.

        Функция не принимает никаких аргументов и не возвращает никаких значений. Она непосредственно
        влияет на содержимое файла 'contacts_bd.txt'.

        Имейте в виду, что функция примет фактические вводы пользователя через средство ввода
        (обычно клавиатуру), и будет продолжать выполнять операции, пока пользователь не
        решит выйти из меню настроек.
        """
    with open('contacts_bd.txt', 'r+') as file:
        contact_data = json.load(file)

        for contact in contact_data:
            print(contact)

        contact_id = int(input('Enter contact id you want to change: '))

        to_change = None
        index_to_change = None

        for i, contact in enumerate(contact_data):
            if contact['id'] == contact_id:
                to_change = contact
                index_to_change = i
                break
        while to_change:
            answer = input(f'Вы хотите изменить этот контакт\n'
                           f'{to_change} '
                           f'да/нет: ')

            if answer.lower() == 'да':
                break
            elif answer.lower() == 'нет':
                return change_contact_to_file()
            else:
                print("ВВЕДИТЕ 'да' ИЛИ 'нет'!!!")
                continue
        else:
            print("Contact not found")

    while True:
            print()
            print("1. Фамилия")
            print("2. Имя")
            print("3. Отчество")
            print("4. Организация")
            print("5. Раб.телефон")
            print("7. Удалить этот контакт")
            print("8. Quit")
            option = input("Введите опцию: ")
            # key_id = str(contact_id + 1)
            if option == '1':
                to_change['surname'] = input('Enter new surname: ')
            elif option == '2':
                to_change['name'] = input('Enter new name: ')
            elif option == '3':
                to_change['midname'] = input('Enter new midname: ')
            elif option == '4':
                to_change['org'] = input('Enter new org: ')
            elif option == '5':
                to_change['work_phone'] = input('Enter new work phone: ')
            elif option == '6':
                to_change['personal_phone'] = input('Enter new personal phone: ')
            elif option == '7':
                del contact_data[index_to_change]
                print("Контакт успешно удален.")
                break
            elif option == '8':
                break
            else:
                print("Введен неверный параметр, попробуйте еще раз.")
            contact_data[index_to_change] = to_change

    with open('contacts_bd.txt', 'w') as file:
        json.dump(contact_data, file)


def search_contact_by_key():
    """
        Функция для поиска контакта по значению ключа в файле контактов.

        Пользователь предоставляет ключ и значение, которые функция затем использует
        для поиска соответствующего контакта.

        Если контакт найден, он выводится на экран, и пользователю предоставляется
        возможность изменить контакт или продолжить поиск.

        Если нет соответствия, выводится сообщение, указывающее, что контакт не найден.

        Функция не принимает никаких аргументов и не возвращает значений. Она влияет на
        содержимое файла 'contacts_bd.txt', если пользователь выбирает изменить контакт.

        Имейте в виду, что для функции требуется ввод пользователя. Она продолжает работать,
        пока пользователь не решит выйти из функции.
        """
    with open('contacts_bd.txt', 'r') as file:
        contact_data = json.load(file)

    while True:  # Основной цикл
        print('Вы находитесь в разделе поиска контакта, по ключу и значению')
        print('Выберете ключ')
        print("1. Фамилия")
        print("2. Имя")
        print("3. Отчество")
        print("4. Организация")
        print("5. Раб.телефон")
        print("6. Личный телефон")
        print("7. Quit")
        option = input('Введите ключ для поиска (например, имя, фамилия и т.д.): ')
        search_key = str()
        if option == '1':
            search_key = 'surname'
        elif option == '2':
            search_key = 'name'
        elif option == '3':
            search_key = 'midname'
        elif option == '4':
            search_key = 'org'
        elif option == '5':
            search_key = 'work_phone'
        elif option == '6':
            search_key = 'personal_phone'
        elif option == '7':
            break
        else:
            print("Введен неверный параметр, попробуйте еще раз.")

        search_value = input(f'Введите значение для поиска по {search_key}: ')

        found_contacts = []
        for contact in contact_data:
            if contact[search_key] == search_value:
                found_contacts.append(contact)

        # если контакты найдены
        if found_contacts:
            print('Найденные контакты:')
            for contact in found_contacts:
                print(f'{contact} \n')
        else:
            print('Контакт по заданному критерию не найден')

        while True:
            answer = input('Хотите ли вы редактировать контакт? (да/нет): ')
            if answer.lower() == 'да':
                change_contact_to_file()
            elif answer.lower() == 'нет':
                break
            else:
                print('Введите некорректный ответ')

        # спросить пользователя, хочет ли он продолжить
        while True:
            next_search = input('Хотите ли вы продолжить поиск? (да/нет): ')
            if next_search.lower() == 'да':
                search_contact_by_key()
            elif next_search.lower() == 'нет':
                return False
            else:
                print('Введите некорректный ответ')