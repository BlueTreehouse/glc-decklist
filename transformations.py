def replacer(text):
    new_list = []
    split = text.split()
    for word in split:
        if word.isdigit() == True:
            stripped = word.rstrip("1")
            new_list.append(stripped)
        else:
            new_list.append(word)
    return new_list


def line_maker(list):
    new_list = []
    for word in list:
        if word.isdigit() == True:
            new_list.append(f"{word}\n")
        else:
            new_list.append(word)
    return new_list


def joiner(list):
    joined = ""
    for word in list:
        #print(word)
        joined += (f"{word} ")
    return joined
        
def quantity(string):
    return string.replace("\n", "\n1")