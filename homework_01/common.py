PATH = 'storage.json'


def check_contact_id(data, contact_id):
    list_of_id = [int(contact['id']) for contact in data['contacts']]

    if contact_id.isdigit() and int(contact_id) in list_of_id:
        return contact_id
    else:
        print('\nВы ввели некорректный ИД!\n')
        return ''
