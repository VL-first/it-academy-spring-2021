# Напишите программу, которая считает общую цену.
# Вводится M рублей и N копеек цена, а также количество S товара.
# Посчитайте общую цену в рублях и копейках за L товаров.
M = 3
N = 20
S = 3
total_price = (M * 100 + N) * S
print("Общая цена товара", total_price // 100, "рублей", total_price % 100, "копеек")
