# import pandas as pd
# index = int(input("введите cтрока: "))
# df = pd.read_excel('что-то.xlsx')
# print(df.iloc[index])

# import pandas as pd
# indexy = int(input("введите cтолбец: "))
# df = pd.read_excel('что-то.xlsx')
# print(df.iloc[:,indexy])

# import pandas as pd
# indexy = int(input("введите cтолбец: "))
# df = pd.read_excel('что-то.xlsx')
# print(df.iloc[:,indexy])
# indexx = int(input("введите cтрока: "))
# print(df.iat[indexx,indexy])

# написать программу где в консоли пользователь выбирает из меню, что он хочет сделать из вариантов это
# 1 вывести весь дата сэт
# 2 вывести конкретную (по индексу(пользователь вводит его)) строчку из датасэта
# 3 вывести столбец(пользователь вводит индекс)
# 4 вывести ячейку (тоже можно поиск организовать через индекс )
# далее пользователю предлагается выбор что он хочет сделать с ячейкой (удалить, изменить, создать новую ячейку)

# def column():
#     import pandas as pd
#     indexy = int(input("введите cтолбец: "))
#     df = pd.read_excel('что-то.xlsx')
#     print(df.iloc[:, indexy])
#
# def line():
#     import pandas as pd
#     index = int(input("введите cтроку: "))
#     df = pd.read_excel('что-то.xlsx')
#     print(df.iloc[index])
#
# def cell():
#     import pandas as pd
#     indexy = int(input("введите cтолбец: "))
#     df = pd.read_excel('что-то.xlsx')
#     print(df.iloc[:, indexy])
#     indexx = int(input("введите cтрока: "))
#     print(df.iat[indexx, indexy])
#
#
#
# print("1 вывести весь дата сэт")
# print("2 вывести конкретную строчку из датасэта")
# print("3 вывести столбец")
# print("4 вывести ячейку")

import pandas as pd
import matplotlib.pyplot as plt

# Шаг 1: Считываем данные из Excel
df = pd.read_excel('что-то.xlsx')

# Проверяем структуру данных
print(df.head())  # Вывод первых строк для проверки

plt.figure(figsize=(8, 6))  # Размер
# Шаг 2: Построение окна графика

# Используем данные из DataFrame
plt.plot(df['Возраст'], df['Номер'], marker='o', label='Зависимость y от x')

# Настройка графика
plt.title('График из Excel')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.legend()
plt.grid(True)  # Включить сетку

# Шаг 3: Отображаем график
plt.show()
