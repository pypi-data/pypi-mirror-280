"""
sequence processing library
"""

def lst_keep_first_val(input_seq):
    """
    keep the first value for same values
    """
    seen = set()
    result = []

    for item in input_seq:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result

def iter_unique_val(input_list):
    """
    Generate the first value for each unique value in the input list.
    """
    seen = set()

    for item in input_list:
        if item not in seen:
            seen.add(item)
            yield item

def lst_remove_val(lst, val):
    """
    remove all value in the list
    """
    return [x for x in lst if x != val]


