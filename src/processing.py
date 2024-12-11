def filter_by_state(list_of_dict: list, chosen_state: str = "EXECUTED") -> list:
    '''Функция принимает список словарей и опционально значение для ключа
state (по умолчанию 'EXECUTED'). Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
state соответствует указанному значению'''
    new_list_of_dict = []
    for dictionary in list_of_dict:
        if dictionary.get("state") == chosen_state:
            new_list_of_dict.append(dictionary)
    return new_list_of_dict


def sort_by_date(list_of_dict: list, is_reverse: bool = True) -> list[dict[str, str]]:
    '''Функция принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание).     Функция возвращает новый список, отсортированный по дате'''
    sorted_list = sorted(list_of_dict, key=lambda x: x.get('date'), reverse=is_reverse)
    return sorted_list
