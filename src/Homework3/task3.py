# Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.

lst = ['a', 'b', 'c']
tlp = tuple(lst)
print(tlp)


# Создайте кортеж ('a', 'b', 'c'), И сделайте из него список

tlp1 = ('a', 'b', 'c')
lst1 = list(tlp1)
print(lst1)


# Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.

a, b, c = "a", 2, "python"
print(a, b, c)


# Создайте кортеж из одного элемента, чтобы при итерировании по этому элементы последовательно
# выводились значения 1, 2, 3. Убедитесь что len() исходного кортежа возвращает 1.

tlp = (0, )
n = 0
while n < 3:
    for element in tlp:
        n = n + 1
        print(n)
print("len = ", len(tlp))
