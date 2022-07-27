def quick_sort(string_list, first, last):
    if first < last:
        divider = list_divider(string_list, first, last) 
        quick_sort(string_list, first, divider - 1)
        quick_sort(string_list, divider + 1, last)
    return string_list

def list_divider(string_list, first, last):
    pivot = string_list[last]
    delimiter = first - 1

    for i in range(first, last):
        if string_list[i] <= pivot:
          delimiter = delimiter + 1
          string_list[i], string_list[delimiter] = string_list[delimiter], string_list[i]

    string_list[delimiter + 1], string_list[last] = string_list[last], string_list[delimiter + 1]

    return delimiter + 1



def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    try:
        if len(first_string) != len(second_string):
            return False
        else:
            first_to_list = list(first_string.lower())
            second_to_list = list(second_string.lower())

            sort_first = quick_sort(first_to_list, 0, len(first_string) - 1)
            sort_second = quick_sort(second_to_list, 0, len(second_string) - 1)

            if sort_first == sort_second:
                return True

        return False
    except TypeError:
        return False
