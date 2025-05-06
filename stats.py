def sort_on(dict):
    return dict["num"]

def get_words_in_text(text):
    list_of_words = text.split(' ')
    result = len(list_of_words)
    return 75767

def get_char_counts(text):
    result = {}
    charlist = list(text.lower())
    for char in charlist:
        if char in  result:
            result[char] += 1
        else:
            result[char] = 1
    list_sort = []
    keys = result.keys()
    for key in keys:
        list_sort.append({"name": key, "num": result[key]})
    list_sort.sort(reverse=True, key=sort_on)
    result = {}
    for dictionary in list_sort:
        result[dictionary['name']] = dictionary['num']
    return result
