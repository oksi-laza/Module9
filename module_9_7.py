from math import sqrt


def is_prime(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        prime_flag = 0
        if res > 1:
            for divider in range(2, int(sqrt(res)) + 1):
                if res % divider == 0:
                    prime_flag = 1
                    break
            if prime_flag == 0:
                print("Простое")
            else:
                print("Составное")
        else:
            print("Составное")
        return res

    return wrapper


@is_prime
def sum_three(a, b, c):
    amount = a + b + c
    return amount


# Проверка кода:
result = sum_three(2, 3, 6)  # Простое
print(result)
print()

result_2 = sum_three(8, 1, 16)  # Составное
print(result_2)
print()

result_3 = sum_three(1, 1, 1)  # Простое
print(result_3)
print()

result_4 = sum_three(3, 1, 1)  # Простое
print(result_4)
print()

result_5 = sum_three(17, 5, 9)  # Простое
print(result_5)
print()

result_6 = sum_three(6, 11, 1)  # Составное
print(result_6)
print()

result_7 = sum_three(25, 15, 35)  # Составное
print(result_7)
print()
