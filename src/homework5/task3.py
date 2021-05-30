# Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся целых чисел,
# отсортированных по возрастанию, которая этот список “сворачивает”

def get_ranges(list_of_numbers):

    lst = []

    for el in list_of_numbers:
        if not lst:
            lst.append([str(el)])
        elif int(el) - int(lst[-1][-1]) == 1:
            lst[-1].append(str(el))
        else:
            lst.append([str(el)])
    ranges = ["-".join((lst[0], lst[-1]) if len(lst) > 1 else lst) for lst in lst]
    result_ranges = ",".join(ranges)
    return result_ranges


print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4, 7, 10]))
print(get_ranges([2, 3, 8, 9]))
