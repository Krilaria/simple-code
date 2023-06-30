import matplotlib.pyplot as plt
import numpy as np

# Создание фигуры и осей
fig, ax = plt.subplots()

# Задание координат и размеров квадрата
square_size = 1

# Рисование квадрата
square = plt.Rectangle((0, 0), square_size, square_size, edgecolor='blue', facecolor='none')
ax.add_patch(square)

# Задание центра и радиуса окружности
circle_center = (square_size/2, square_size/2)
circle_radius = square_size / 2

# Рисование окружности
circle = plt.Circle(circle_center, circle_radius, edgecolor='red', facecolor='none')
ax.add_patch(circle)

# Генерация случайных точек внутри квадрата
num_points = 1000  # Количество точек
points_x = np.random.uniform(0, 0 + square_size, num_points)
points_y = np.random.uniform(0, 0 + square_size, num_points)

# Подсчет количества точек, попавших в круг
points_inside_circle = np.sqrt((points_x - circle_center[0])**2 + (points_y - circle_center[1])**2) <= circle_radius

# Отображение графика с постепенным добавлением точек и обновлением числа точек внутри круга
points_inside_circle_count = 0  # Счетчик точек внутри круга
plt.draw()
for i in range(num_points):
    ax.plot(points_x[i], points_y[i], 'bo', markersize=4)
    points_inside_circle_count += points_inside_circle[i]  # Обновление счетчика точек внутри круга
    points_inside_circle_ratio = points_inside_circle_count / (i+1)  # Расчет доли точек внутри круга
    legend_text = f'Pi number estimate: {points_inside_circle_ratio*4:.2f}, Point number: {i+1}/{num_points}'
    plt.title([legend_text])
    plt.pause(0.00005)  # Задержка между точками (в секундах)
    
plt.show()