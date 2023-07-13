def is_anagram(first_string, second_string):
    insensitive_first = first_string.lower()
    insensitive_second = second_string.lower()

    sorted_first = ''.join(insertion_sort(insensitive_first))
    sorted_second = ''.join(insertion_sort(insensitive_second))

    if insensitive_first == "" and insensitive_second == "":
        return False
    
    if len(insensitive_first) != len(insensitive_second):
        return (sorted_first, sorted_second, sorted_first == sorted_second)

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

result = is_anagram('amor', '')
print(result)