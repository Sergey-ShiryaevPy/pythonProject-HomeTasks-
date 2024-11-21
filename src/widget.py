from masks import get_mask_card_number, get_mask_account


def mask_account_card(card_info: str) -> str:
    """Функция, маскирующая информацию карты и счета"""
    if "Счет" in card_info:
        return f"Счет {get_mask_card_number(card_info)}"
    else
        card_number = get_mask_card_number(card_info[-16:])
        card_mask = card_info.replace(card_info[-16:],card_number)
        return card_mask


def get_date(date: str) -> :
    """Функция, возвращающая дату в ином формате"""
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
