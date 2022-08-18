def count_matching_numbers(list1,list2):
    count = 0
    for num in list1:
        if num in list2:
            count += 1
    return count