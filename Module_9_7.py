def is_prime(func):
    def wrapper(*nums: int):
        result = func(*nums)  # Вызов переданной функции с аргументами
        for div in range(2, result):  # Проверка числа на простоту
            if result % div == 0:
                print('Составное')  # Число не простое
                break
        else:
            print('Простое')  # Число простое
    return wrapper  # Возвращает обёртку

@is_prime
def sum_three(first, second, third):
    print(first + second + third)
    return first + second + third

sum_three(2, 3, 6)