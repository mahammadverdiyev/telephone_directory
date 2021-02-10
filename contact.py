import pickle
import os


class Contact:
    @staticmethod
    def __display_menu() -> None:
        print('''1. Show contacts
2. Search contact
3. Add contact
4. Delete contact
5. Exit''')
        print()

    @staticmethod
    def menu_loop() -> str:
        while True:
            Contact.__display_menu()
            option = input("Option (1-5): ")
            print('\n')
            if option.strip() in ['1', '2', '3', '4', '5']:
                break
        return option

    def list_records(self) -> None:
        records = self.__read_file()
        if len(records) == 0:
            print('No contact is exist.')
        else:
            print(f"Number of records: {len(records)}\n")
            print(f"{'Name':^10} {'Surname':^10} {'Phone':^13}")

            for record in records:
                print(
                    f"{record.get('name', ' '):10.10} {record.get('surname', ' '):10.10} {record.get('phoneNumber', ' '):13.13}")
        print()

    def search_records(self) -> None:
        print('Search a contact')
        name = input("Name: ")
        surname = input("Surname: ")
        records = self.__search_record_from_file(name, surname)
        if len(records) == 0:
            print('\nContact is not found.')
        else:
            print('Phone number: ', end='')
            for record in records:
                print(f"{record.get('phoneNumber'):13.13}", end='')
        print('\n')

    def add_record(self) -> None:
        print('Add new contact')
        name = input("Name: ")
        surname = input("Surname: ")
        phoneNumber = input("Telephone number: ")
        print(f"New record: {name} {surname} - {phoneNumber}")
        if self.__are_you_sure():
            self.__record_to_file(name, surname, phoneNumber)
            print('New contact is added successfully.\n')

    def delete_record(self) -> None:
        print('Delete a contact')
        name = input("Name: ")
        surname = input("Surname: ")
        records = self.__search_record_from_file(name, surname)
        if len(records) == 0:
            print('\nThere is no such contact to delete\n')
        else:
            print('Phone number: ', end='')
            for record in records:
                print(f"{record.get('phoneNumber'):13.13}", end='  ')
            print('\n')
            if self.__are_you_sure():
                self.__delete_record_from_file(records)
            print('Contact is deleted.')

    def __are_you_sure(self) -> bool:
        while True:
            answer = input("Are you sure? (Y)es/(N)o  ")
            print()
            if answer.upper() == 'Y':
                return True
            elif answer.upper() == 'N':
                return False

    def __read_file(self) -> list:
        if os.path.isfile('data.bin'):
            with open('data.bin', 'rb') as fileObject:
                records = pickle.load(fileObject)
        else:
            records = list()
        return records

    def __write_file(self, recordsParam: list) -> None:
        with open('data.bin', 'wb') as fileObject:
            pickle.dump(recordsParam, fileObject)

    def __search_record_from_file(self, nameParam: str, surnameParam: str) -> list:
        records = self.__read_file()
        response = list()
        for record in records:
            if record.get('name').lower() == nameParam.lower() and \
                    record.get('surname').lower() == surnameParam.lower():
                response.append(record)

        return response

    def __record_to_file(self, nameParam: str, surnameParam: str, phoneNumberParam: str) -> None:
        records = self.__read_file()
        record_dict = dict(name=nameParam, surname=surnameParam, phoneNumber=phoneNumberParam)
        records.append(record_dict)
        self.__write_file(recordsParam=records)

    def __delete_record_from_file(self, recordsParam: list) -> None:
        records = self.__read_file()
        for record in records:
            for recordForDelete in recordsParam:
                if record['name'].lower() == recordForDelete['name'].lower() and \
                        record['surname'].lower() == recordForDelete['surname'].lower():
                    records.remove(recordForDelete)
                    continue

        self.__write_file(records)
