def filter_by_state(list_of_dict: list, chosen_state: str = "EXECUTED") -> list:
    '''pass'''
    new_list_of_dict = []
    for dictionary in list_of_dict:
        if dict.get("state") == chosen_state:
            new_list_of_dict.append(dictionary)
    return new_list_of_dict


def sort_by_state(list_of_dict: list, is_reverse: bool = True) -> list
    '''pass'''
    sorted_list = sorted(list_of_dict, key = lambda x: x["date"],reverce=is_reverse)
    return sorted_list