def flat_generator(nested_list):

    new_list = []
    for i in nested_list:
        if type(i) is not list:
            new_list.append(i)
        else:
            for _ in i:
                new_list.append(_)

    return new_list

def flat_com(nested_list):

    new_list = []
    data = [[new_list.append(item) if type(item) is not list else [new_list.append(_) for _ in item]]  for item in nested_list]
    return new_list

if __name__ == '__main__':
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        [1, 2, None],
        17,
        None
    ]
    data = flat_generator(nested_list)
    for i in data:
        print(i)

    data_com = flat_com(nested_list)
    print(data_com)
    for i in data_com:
        print(i)