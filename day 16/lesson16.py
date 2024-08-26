even_list = []
odd_list = []


def summ(listen):
    for i in listen:
        if i % 2 == 0:
            even_list.append(i)
        elif i %2 != 0:
            odd_list.append(i)
            sum_even = sum (even_list)
            sum_odd = sum (odd_list)
    return [sum_even,sum_odd]






print(summ([1,2,3,4,5]))







































