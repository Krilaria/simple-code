import numpy as np
import matplotlib.pyplot as plt

# Параметры контура
L = 1  # Индуктивность (в генри)
R = 0.04  # Сопротивление потерь из-за заземления(в омах)
C = 1  # Ёмкость (в фарадах)
V0 = 1  # Начальное напряжение (в вольтах)
alpha = R / (2 * L)  # Коэффициент затухания

# Временные параметры
dt = 0.01  # Шаг времени (в секундах)
t = np.arange(0, 100, dt)  # Временная ось

# Инициализация массивов для хранения значений тока и напряжения
I = np.zeros_like(t)
V = np.zeros_like(t)

# Начальные условия
I[0] = 0  # Начальный ток
V[0] = V0  # Начальное напряжение на конденсаторе

# Моделирование изменения тока и напряжения в контуре
for i in range(1, len(t)):
    I[i] = I[i-1] - (V[i-1] / (L* C) + alpha * I[i-1]) * dt
    V[i] = V[i-1] + (I[i-1] / C) * dt

# Построение графиков
plt.figure(figsize=(10, 6))
plt.plot(t, I, label='Ток, А')
plt.plot(t, V, label='Напряжение, В')
plt.xlabel('Время, с')
plt.ylabel('Значение')
plt.title('Изменение тока и напряжения конденсатора колебательного контура')
plt.legend()
plt.grid(True)
plt.show()