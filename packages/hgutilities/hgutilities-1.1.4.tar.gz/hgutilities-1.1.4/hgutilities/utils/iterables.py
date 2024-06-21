def remove_none_values(dictionary):
    filtered_dictionary = {key: value for key, value in dictionary.items()
                           if value is not None}
    return filtered_dictionary

def transpose_list(my_list):
    transposed_list = list(map(list, zip(*my_list)))
    return transposed_list

def get_dict_string(dictionary):
    keys = list(dictionary.keys())
    max_length = max([len(str(key)) for key in keys])
    string = "\n".join([f"{key}: {(max_length - len(str(key)))*' '}{value}"
                        for key, value in dictionary.items()])
    return string
