import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1

data_list = [[1, 2, 3], [4, 5, 6]]
df_from_list = pd.DataFrame(data_list, columns=['A', 'B', 'C'])
print("DataFrame из списка:")
print(df_from_list)

data_array = np.array([[7, 8, 9], [10, 11, 12]])
df_from_array = pd.DataFrame(data_array, columns=['D', 'E', 'F'])
print("\nDataFrame из NumPy массива:")
print(df_from_array)

data_dict = {
    'G': [13, 14],
    'H': [15, 16]
}
df_from_dict = pd.DataFrame(data_dict)
print("\nDataFrame из словаря:")
print(df_from_dict)

# 2
non_intersecting_elements = df_from_list[~df_from_list['A'].isin(df_from_array['D'])]
print("\nНе пересекающиеся элементы в столбце A:")
print(non_intersecting_elements)

# 3
frequency_A = df_from_list['A'].value_counts()
frequency_B = df_from_list['B'].value_counts()

print("\nЧастота уникальных элементов в столбце A:")
print(frequency_A)

print("\nЧастота уникальных элементов в столбце B:")
print(frequency_B)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.bar(frequency_A.index, frequency_A.values)
plt.title('Гистограмма частоты A')
plt.xlabel('Элементы A')
plt.ylabel('Частота')

plt.subplot(1, 2, 2)
plt.bar(frequency_B.index, frequency_B.values)
plt.title('Гистограмма частоты B')
plt.xlabel('Элементы B')
plt.ylabel('Частота')

plt.tight_layout()
plt.show()

# 4
vertical_concat = pd.concat([df_from_list, df_from_array], axis=0, ignore_index=True)
print("\nВертикальная конкатенация DataFrame:")
print(vertical_concat)

horizontal_merge = pd.merge(df_from_list, df_from_dict, left_index=True, right_index=True)
print("\nГоризонтальное объединение DataFrame:")
print(horizontal_merge)

# 5.
data_plot = {
    'X': [1, 2, 3, 4, 5],
    'Y1': [2, 3, 5, 7, 11],
    'Y2': [1, 4, 6, 8, 10]
}
df_plot = pd.DataFrame(data_plot)

plt.figure(figsize=(10, 6))
plt.plot(df_plot['X'], df_plot['Y1'], marker='o', label='Y1', color='blue')
plt.plot(df_plot['X'], df_plot['Y2'], marker='s', label='Y2', color='orange')
plt.title('График зависимости Y от X')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid()
plt.show()
import numpy as np
import matplotlib.pyplot as plt