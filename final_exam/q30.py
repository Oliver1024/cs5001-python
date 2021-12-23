def sum_list(list, acc):
    if len(list) == 0:
        return acc
    else:
        acc = acc + list[0]
        return sum_list(list[1:], acc)
print(sum_list([1,3,5,7], 0))


# output result is 16 is that the right answer.  choose this code of choice