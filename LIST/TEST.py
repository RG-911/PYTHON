def remove_duplicates(dupe_list):
    new_list = []
    for el in dupe_list:
        if el not in new_list:
            new_list.append(el)
    return new_list


#### TESTS SHOULD ALL BE TRUE ####
print("{0}\n should equal \n{1}\n {2}\n".format(remove_duplicates(['a', 'a', 'x', 'x', 'x', 'g', 't', 't']),
                                                ['a', 'x', 'g', 't'],
                                                remove_duplicates(['a', 'a', 'x', 'x', 'x', 'g', 't', 't']) == ['a',
                                                                                                                'x',
                                                                                                                'g',
                                                                                                                't']))

print("{0}\n should equal \n{1}\n {2}\n".format(remove_duplicates(['c', 'c', 'd', 'd', 'e', 'e', 'f', 'a', 'a']),
                                                ['c', 'd', 'e', 'f', 'a'],
                                                remove_duplicates(['c', 'c', 'd', 'd', 'e', 'e', 'f', 'a', 'a']) == [
                                                    'c', 'd', 'e', 'f', 'a']))

print("{0}\n should equal \n{1}\n {2}\n".format(remove_duplicates([13, 13, 13, 13, 13, 42]), [13, 42],
                                                remove_duplicates([13, 13, 13, 13, 13, 42]) == [13, 42]))