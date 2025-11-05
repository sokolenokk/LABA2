def sum_odd(n: int) -> int:
    summ = 0
    num = 1
    while num <= n:
        summ += num
        num += 2

    return summ


user_number = int(input("Введите число N: "))
answer = sum_odd(user_number)

print("Сумма всех нечетных чисел до N: ", answer)
