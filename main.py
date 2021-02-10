from contact import Contact

contact = Contact()

while True:
    option = Contact.menu_loop()
    if option == '1':
        contact.list_records()
    elif option == '2':
        contact.search_records()
    elif option == '3':
        contact.add_record()
    elif option == '4':
        contact.delete_record()
    elif option == '5':
        break
