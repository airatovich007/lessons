summa =0
def calculate_structure_sum(*args):
    global summa
    for i in args:
        if isinstance(i, int or float):
            summa += i
        elif  isinstance(i, str):
           summa += len(i)
        elif isinstance(i, dict):
            list_= i.items()
            calculate_structure_sum(*list_)
        else:
            calculate_structure_sum(*i)
    return summa
data_structure = [[1, 2, 3],{'a': 4, 'b': 5},(6, {'cube': 7, 'drum': 8}),"Hello",((), [{(2, 'Urban', ('Urban2', 35))}])]
result = calculate_structure_sum(*data_structure)

print(result)
