def count_elements(lst):
    count = {}
    for element in lst:
        data_type = type(element).__name__
        if data_type in count:
            count[data_type] += 1
        else:
            count[data_type] = 1
    return count