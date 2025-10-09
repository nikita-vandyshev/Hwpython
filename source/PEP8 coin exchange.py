def calculate_coin_combinations(coin1, coin2, coin3, target_sum):
    """
    Находит комбинацию монет для размена заданной суммы.
    
    Args:
        coin1 (int): номинал первой монеты
        coin2 (int): номинал второй монеты  
        coin3 (int): номинал третьей монеты
        target_sum (int): сумма для размена
        
    Returns:
        str: строка с комбинацией монет или 0 если размен невозможен
    """
    # Перебираем все возможные количества монет каждого номинала
    for count1 in range(target_sum // coin1 + 1):
        for count2 in range(target_sum // coin2 + 1):
            for count3 in range(target_sum // coin3 + 1):
                # Проверяем, дает ли текущая комбинация нужную сумму
                if coin1 * count1 + coin2 * count2 + coin3 * count3 == target_sum:
                    return f'{coin1}*{count1}, {coin2}*{count2}, {coin3}*{count3}'
    
    return 0


# Получаем номиналы монет на основе длины введенных пользователем данных
first_name_length = len(input('Введите имя: '))
last_name_length = len(input('Введите фамилию: '))
patronymic_length = len(input('Введите отчество (если нет, то нажмите Enter): '))

# Если отчество не введено, используем значение по умолчанию
if not patronymic_length:
    patronymic_length = 19

# Получаем сумму для размена
target_amount = int(input('Введите сумму для размена: '))

# Пытаемся найти комбинацию для размена
combination_result = calculate_coin_combinations(
    first_name_length, 
    last_name_length, 
    patronymic_length, 
    target_amount
)

# Выводим результат или сообщение об ошибке
if combination_result:
    print(combination_result)
else:
    print(-42)