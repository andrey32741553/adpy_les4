documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def show_name_by_num():
    doc_num = input('Введите номер документа: ')
    for data in documents:
        if data["number"] == doc_num:
            return data["name"]
    return 'Такого документа нет в списке'


def show_shelf_by_num():
    doc_num = input('Введите номер документа: ')
    for key, item in directories.items():
        if doc_num in item:
            return key
    return 'Такого документа нет в списке'


def show_list_of_doc():
    info_list = []
    for data in documents:
        data_list = list(data.values())
        info_list.append(f'{data_list[0]} {data_list[1]} {data_list[2]}')
    return info_list


def add_new_data():
    # doc_type = input('Введите тип документа: ')
    # doc_num = input('Введите номер документа: ')
    # name = input('Введите имя и фамилию: ')
    # shelf_num = input('Укажите номер полки для хранения: ')

    doc_type = 'passport'
    doc_num = '0945 564783'
    name = 'Гендальф Серый'
    shelf_num = '3'

    for key, value in directories.items():
        if shelf_num == key:
            value.append(doc_num)
            new_dict = {"type": doc_type, "number": doc_num, "name": name}
            documents.append(new_dict)
            return documents, directories
    return 'Такой полки нет'


def move_doc_by_num():
    doc_num = input('Введите номер документа, который нужно переместить: ')
    shelf_num = input(f'Введите номер полки, куда нужно переместить {doc_num}: ')
    for key, value in directories.items():
        try:
            if doc_num in value:
                value.remove(doc_num)
                directories[shelf_num] += {doc_num}
        except KeyError:
            return 'Такой полки нет'
    return directories


def del_doc_by_num():
    # doc_num = input('Введите номер документа для удаления: ')
    doc_num = '2207 876234'
    for data in documents:
        if doc_num == data['number']:
            documents.remove(data)
    for value in directories.values():
        if doc_num in value:
            value.remove(doc_num)
            return directories, documents
    return 'Такого документа нет'


def add_new_shelf():
    new_shelf = input('Введите номер новой полки: ')
    if new_shelf in directories.keys():
        return 'Такая полка уже есть'
    else:
        directories[new_shelf] = []
    return directories
