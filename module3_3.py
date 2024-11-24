def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [59, True, 'Фермент']
values_dict = {'a': 'breakfest', 'b': 88, 'c': False}
print_params(*values_list)
print_params(**values_dict)

values_list2 = [77.5, 'Birmingham']
print_params(*values_list2, 14)
