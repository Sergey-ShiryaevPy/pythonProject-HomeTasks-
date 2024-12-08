def filter_by_state(list_of_dict: list, chosen_state: str = "EXECUTED") -> list:
    new_list_of_dict = []
    for dictionary in list_of_dict:
        if dict.get("state") == chosen_state:
            new_list_of_dict.append(dictionary)
    return new_list_of_dict


def sort_by_state()
    '''pass'''