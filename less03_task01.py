def my_func():
    try:
        x = int(input('Insert first number: '))
        y = int(input('Insert second number: '))
        return print(x / y)
    except ZeroDivisionError:
        return print('Dividing on zero is not allowed!')


my_func()