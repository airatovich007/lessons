calls = 0


def count_calls():
    global calls
    calls+= 1

def string_info(string):
    count_calls()
    tuple_1 = [len(string)], string.upper(), string.lower()
    return tuple_1

def is_contains(string,list_to_search):
    count_calls()
    list_ = [s.lower() for s in list_to_search]#Промежуточное преобразование регистра, надеюсь не будет ошибкой
    bool_=(string.lower() in list_)
    return bool_

print(string_info('Чайка'))
print(string_info('Шайка'))
print(string_info('Лейка'))
print(is_contains('minor',['Major', 'maYor', 'MOTOR'] ))
print(is_contains('minor',['minora', 'SIROP', 'Minor']))
print(calls)