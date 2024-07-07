def filter_by_state(list_dict: list[dict], state='EXECUTED') -> list[dict]:
    temp_list = list()
    for item in list_dict:
        if item['state'] == state:
            temp_list.append(item)
    return temp_list



