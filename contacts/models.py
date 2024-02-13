import json


class Contact:
    id_counter = 1  # статическая переменная для подсчета идентификаторов

    def __init__(self, surname, name, midname, org, work_phone, personal_phone):
        self.id = self.get_next_id()
        Contact.id_counter += 1
        self.surname = surname
        self.name = name
        self.midname = midname
        self.org = org
        self.work_phone = work_phone
        self.personal_phone = personal_phone

    def get_next_id(self):
        try:
            with open('contacts_bd.txt', 'r') as file:
                contacts = json.load(file)
                last_contact = contacts[-1]  # получить последний контакт
                last_id = list(last_contact.values())[0]  # получить id последнего контакта
                print(last_id)
                return int(last_id) + 1  # вернуть id последнего контакта + 1
        except (FileNotFoundError, json.JSONDecodeError, IndexError):
            return Contact.id_counter  # вернуть статический счетчик id

    def __str__(self):
        return (f"id: {self.id}, Фамилия: {self.surname}, Имя: {self.name}, Отчество: {self.midname},"
                f" Организация: {self.org}, Раб.телефон: {self.work_phone}, Лич.телефон: {self.personal_phone}")

    def to_dict(self):
        return {
            'id': self.id,
            'surname': self.surname,
            'name': self.name,
            'midname': self.midname,
            'org': self.org,
            'work_phone': self.work_phone,
            'personal_phone': self.personal_phone
        }

    @staticmethod
    def create_contact():
        new_contact = Contact(
            surname=input('Enter your surname: '),
            name=input('Enter your name: '),
            midname=input('Enter your midname: '),
            org=input('Enter your organization: '),
            work_phone=input('Enter your work phone: '),
            personal_phone=input('Enter your personal phone: '),
        )
        return new_contact
