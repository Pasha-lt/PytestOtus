def word_count(string_a):
    string_a =string_a.replace(',', '').replace('.','')
    dict_count = {}
    for word in string_a.split():
        if word in dict_count:
            dict_count[word] +=1
        else:
            dict_count[word] = 1
    return dict_count


print(word_count('раз раз. два три'))