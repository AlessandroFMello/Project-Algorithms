def quick_sort(array, first, last):
    if first < last:
        divider = list_divider(array, first, last)
        quick_sort(array, first, divider - 1)
        quick_sort(array, divider + 1, last)
    return array


def list_divider(array, first, last):
    pivot = array[last]
    delimiter = first - 1

    for i in range(first, last):
        if array[i] <= pivot:
            delimiter = delimiter + 1
            array[i], array[delimiter] = array[delimiter], array[i]

    array[delimiter + 1], array[last] = array[last], array[delimiter + 1]

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
