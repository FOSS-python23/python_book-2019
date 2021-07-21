# Константа NUМ_DAYS содержит количество дней,
# за которые мы соберем данные продаж.
NUM_DAYS = 5


def main():
    # Создать список, который будет содержать
    # продажи за каждый день.
    sales = [0] * NUM_DAYS

    # Создать переменную, которая будет содержать индекс.

    print('Введите продажи за каждый день.')

    # Получить продажи за каждый день.
    for i in range(NUM_DAYS):

        print('День № ', i+1, ': ', sep='', end='')
        sales[i] = float(input())

        # Показать введенные значения.
        print('Boт значения, которые были введены:')
        for value in sales:
            print(value)


# Вызвать главную функцию.
main()
