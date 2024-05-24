data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print('Исходный массив: ', data_structure)
sum = 0

def sum_items(param):
    global sum
    for i in param:
        if isinstance(i, int) == True:
            sum += i
        elif isinstance(i, str) == True:
            sum += len(i)
        elif isinstance(i, list) == True or isinstance(i, tuple) == True or isinstance(i, set) == True:
            sum_items(i)
        elif isinstance(i, dict) == True:
           for key in i.items():
               sum_items(key)

sum_items(data_structure)
print('Сумма элементов: ', sum)


