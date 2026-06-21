import sys
sys.path.append('..')
from app.math import add, subtract, multiply, divide
# Тест с ветвлениями (для branch coverage)
def test_divide_branches():
    # Проверяем положительное деление
    assert divide(10, 2) == 5
    # Проверяем деление с дробным результатом
    assert divide(5, 2) == 2.5
    # Проверяем деление на 1
    assert divide(100, 1) == 100
    # Проверяем деление отрицательных чисел
    assert divide(-10, 2) == -5
    # Проверяем деление на отрицательное
    assert divide(10, -2) == -5
    # Проверяем деление 0 на число
    assert divide(0, 5) == 0
