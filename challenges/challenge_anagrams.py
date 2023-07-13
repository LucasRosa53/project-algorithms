def is_anagram(first_string, second_string):
    if not isinstance(first_string, str) or not isinstance(second_string, str):
        return False
    
    insensitive_first = first_string.lower()
    insensitive_second = second_string.lower()

    if len(insensitive_first) != len(insensitive_second):
        return False

    sorted_first = ''.join(insertion_sort(insensitive_first))
    sorted_second = ''.join(insertion_sort(insensitive_second))

    return (sorted_first, sorted_second, sorted_first == sorted_second)


def insertion_sort(string):
    sorted_string = list(string)
    for i in range(1, len(sorted_string)):
        key = sorted_string[i]
        j = i - 1
        while j >= 0 and sorted_string[j] > key:
            sorted_string[j + 1] = sorted_string[j]
            j -= 1
        sorted_string[j + 1] = key
    
    return (''.join(sorted_string))
