# Создайте декоратор, который хранит результаты вызовов функции (за все время вызовов,
# не только текущий запуск программы)

def my_dec(func):
    value = 0

    def wrapper():
        nonlocal value
        value += 1
        return value
    return wrapper


@my_dec
def fun():
    pass


print(fun())
print(fun())
