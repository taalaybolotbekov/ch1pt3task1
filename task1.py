def number():
    n = input('Введите трехзначное число: ')
    sum = 0
    for i in n:
        sum += int(i)
    return sum
print(number())