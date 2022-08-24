def flat_generator(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            for sub_elem in flat_generator(item):
                yield sub_elem
        else:
            yield item

if __name__ == '__main__':
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        [1, 2, None],
        17,
        None
    ]

    for item in flat_generator(nested_list):
        print(item)