import random

def get_numbers_ticket(min, max, quantity):
    # Перевіряю чи вхідні параметри відповідають заданим обмеженням
    if min >= 1 and max <= 1000 and quantity > 0 and min <= max and quantity <= (max - min + 1):
        # Генеруємо випадковий, відсортований список унікальних чисел
        numbers = sorted(random.sample(range(min, max+1), quantity))
        return numbers
    else:
        # Якщо параметри не відповідають вимогам, повертаємо пустий список
        return []
