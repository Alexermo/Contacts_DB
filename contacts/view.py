import json
from contacts.models import Contact


# contacts = 'contacts_bd.txt'

def read_contact_from_file():
    try:
        with open('contacts_bd.txt', 'r') as file:
            contact_data = json.load(file)
            for contact in contact_data:
              print(contact)
    except json.JSONDecodeError:
        print("Файл пустой или данные нераспознаваемы")


def write_contact_to_file():
    new_contact = Contact.create_contact()
    with open('contacts_bd.txt', 'r') as file:
        content = file.read()
        contacts = json.loads(content) if content else []

    contacts.append(new_contact.to_dict())

    with open('contacts_bd.txt', 'w') as file:
        json.dump(contacts, file)


def change_contact_to_file():
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

        # спросить пользователя, хочет ли он продолжить
        while True:
            next_search = input('Хотите ли вы продолжить поиск? (да/нет): ')
            if next_search.lower() == 'да':
                break
            elif next_search.lower() == 'нет':
                break
            else:
                print('Введите некорректный ответ')

        while True:
            answer = input('Хотите ли вы редактировать контакт? (да/нет): ')
            if answer.lower() == 'да':
                change_contact_to_file()
                break
            elif next_search.lower() == 'нет':
                return
            else:
                print('Введите некорректный ответ')

