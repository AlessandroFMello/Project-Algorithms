def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    try:
        if word == '' or word[0] != word[-1]:
            return False
        elif len(word) == 1 or (len(word) == 2 and word[0] == word[-1]):
            return True
        else:
            return is_palindrome_recursive(word[1:-1], low_index, high_index)
    except ValueError:
        return False
