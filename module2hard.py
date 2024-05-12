
print('Добро пожаловать')
print('Задание "Слишком древний шифр"')
n = int(input('Введите число от 3 до 20 '))
result = ''
for i in range(1, n):
    for j in range(1, n):
        if n % (i+j) == 0 and i < j:
            result += str(i)+str(j)
print(f'Шифр для числа {n}: {result}')

