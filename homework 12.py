import pandas as pd
import matplotlib.pyplot as plt

# Пример данных
data = 'D:\Python\Mall_Customers.csv'
df = pd.read_csv(data, sep=',')
average_income_female = df[df['Genre'] == 'female']['Annual Income (k$)'].mean()
print(f"Средняя доходность женщин: {average_income_female}")
# Определяем половую принадлежность людей с большими расходами
average_expenses = df['Spending Score (1-100)'].mean()
high_expenses = df[df['Spending Score (1-100)'] > average_expenses]
print("Люди с большими расходами:")
print(high_expenses[['Genre', 'Spending Score (1-100)']])
# График зависимости доходов от возраста для мужчин
plt.figure(figsize=(10, 5))
plt.plot(df[df['Genre'] == 'male']['Age'], df[df['Genre'] == 'male']['Annual Income (k$)'], color='blue', alpha = 1)
plt.title('Зависимость доходов от возраста для мужчин')
plt.xlabel('Возраст')
plt.ylabel('Доход')
plt.grid()
plt.ylim(-15, 15) 
plt.xlim(-15, 15) 
plt.show()
# Столбчатый график распределения расходов в зависимости от доходов
plt.figure(figsize=(10, 5))

# Группируем данные по доходам и суммируем расходы
grouped = df.groupby(['Annual Income (k$)', 'Genre'])['Spending Score (1-100)'].sum().unstack()

# Столбчатый график
grouped.plot(kind='bar', color=['blue', 'pink'], edgecolor='black')
plt.title('Распределение расходов в зависимости от доходов')
plt.xlabel('Доход')
plt.ylabel('Суммарные расходы')
plt.xticks(rotation=45)
plt.legend(title='Пол')
plt.grid(axis='y')
plt.show()