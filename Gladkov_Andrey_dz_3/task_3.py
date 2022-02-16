def thesaurus(*names):
    out_dict = {}
    for name in names:
        if not (out_dict.get(name[0])):
            out_dict[name[0]] = [name]
        else:
            out_dict[name[0]].append(name)
    return out_dict

print(thesaurus("Иван", "Мария", "Петр", "Илья"))