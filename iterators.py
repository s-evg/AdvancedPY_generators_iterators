class FlatIterator:
    def __init__(self, nested_list):
        self.nested_list = nested_list
        self.cursor = -1
        self.list_len = len(self.nested_list)

    def __iter__(self):
        self.cursor += 1
        self.nest_cursor = 0
        return self

    def __next__(self):
        if self.nest_cursor == len(self.nested_list[self.cursor]):
          iter(self)
        if self.cursor == self.list_len:
          raise StopIteration
        self.nest_cursor += 1
        return self.nested_list[self.cursor][self.nest_cursor - 1]


if __name__ == '__main__':
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
        [99, 131, 743]
    ]
    flat_list = [item for item in FlatIterator(nested_list)]
    for i in flat_list:
        print(i)