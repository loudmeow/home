import numpy as np
import matplotlib.pyplot as plt

# Определяем функцию
def f(x, a, b):
    return (x**b - a**b) / x**b

# Задаем параметры для графиков
params = [
    (1, 1), (2, 1), (1, 2)  # Для x > 0
]

# Графики для x > 0
fig, ax = plt.subplots(figsize=(12, 8))

# Основные графики
colors = ['blue', 'green', 'orange']
for (a, b), color in zip(params, colors):
    x_positive = np.linspace(0.01, 10, 400)
    y = f(x_positive, a, b)
    ax.plot(x_positive, y, label=f'α={a}, β={b}', color=color)

# Прямая f(x) = 0
ax.axhline(0, color='black', lw=0.5, ls='--')

# Настройки графика
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title('Графики функции для x > 0')
ax.grid(True)
ax.legend()
plt.xlim(0, 10)
plt.ylim(-3, 3)

# Сохраняем основной график
plt.savefig('graph_positive.svg')
plt.show()

# Врезки для малых и больших x
fig, ax = plt.subplots(figsize=(12, 8))
for (a, b), color in zip(params, colors):
    x_positive = np.linspace(0.01, 10, 400)
    y = f(x_positive, a, b)
    ax.plot(x_positive, y, label=f'α={a}, β={b}', color=color)

# Врезка для малых x
ax_inset1 = fig.add_axes([0.15, 0.6, 0.25, 0.25])  # [left, bottom, width, height]
x_inset1 = np.linspace(0.01, 1, 100)
for (a, b), color in zip(params, colors):
    y_inset1 = f(x_inset1, a, b)
    ax_inset1.plot(x_inset1, y_inset1, color=color)

ax_inset1.set_title('Малые x')
ax_inset1.grid(True)

# Врезка для больших x
ax_inset2 = fig.add_axes([0.6, 0.15, 0.25, 0.25])  # [left, bottom, width, height]
x_inset2 = np.linspace(5, 10, 100)
for (a, b), color in zip(params, colors):
    y_inset2 = f(x_inset2, a, b)
    ax_inset2.plot(x_inset2, y_inset2, color=color)

ax_inset2.set_title('Большие x')
ax_inset2.grid(True)

# Настройки графика
ax.axhline(0, color='black', lw=0.5)  # Прямая f(x) = 0
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title('Графики функции с врезками для x > 0')
ax.grid(True)
ax.legend()
plt.xlim(0, 10)
plt.ylim(-3, 3)

# Сохраняем график с врезками
plt.savefig('graph_positive_with_insets.svg')
plt.show()

# Графики для x < 0
fig, ax = plt.subplots(figsize=(12, 8))
x_negative = np.linspace(-10, -0.01, 400)

for (a, b), color in zip(params[:3], colors):
    y = f(x_negative, a, b)
    ax.plot(x_negative, y, label=f'α={a}, β={b}', color=color)

# Прямая f(x) = 0
ax.axhline(0, color='black', lw=0.5)

# Врезка для удаления x от 0 к −∞
ax_inset = fig.add_axes([0.15, 0.6, 0.25, 0.25])  # [left, bottom, width, height]
x_inset_neg = np.linspace(-1, -10, 100)
for (a, b), color in zip(params[:3], colors):
    y_inset_neg = f(x_inset_neg * -1 * -1 , a , b)
    ax_inset.plot(x_inset_neg , y_inset_neg , color=color)

# Настройки графика
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title('Графики функции для x < 0')
ax.grid(True)
ax.legend()
plt.xlim(-10, -0.01)
plt.ylim(-3, 3)

# Сохраняем график для x < 0
plt.savefig('graph_negative.svg')
plt.show()