import types


def flat_generator(list_of_lists):
    new_list = []
    list_of_lists = list_of_lists
    while list_of_lists:
        for lists in list_of_lists:
            for item in lists:
                yield new_list.append(item)
    ...

list_of_lists_1 = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]

for i in flat_generator(list_of_lists_1):
    print(i)

# def test_2():
#
#     list_of_lists_1 = [
#         ['a', 'b', 'c'],
#         ['d', 'e', 'f', 'h', False],
#         [1, 2, None]
#     ]
#
#     for flat_iterator_item, check_item in zip(
#             flat_generator(list_of_lists_1),
#             ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
#     ):
#
#         assert flat_iterator_item == check_item
#
#     assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
#
#     assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)
