# import pandas as pd
# index = int(input("введите cтрока: "))
# df = pd.read_excel('что-то.xlsx')
# print(df.iloc[index])

# import pandas as pd
# indexy = int(input("введите cтолбец: "))
# df = pd.read_excel('что-то.xlsx')
# print(df.iloc[:,indexy])

import pandas as pd
indexy = int(input("введите cтолбец: "))
df = pd.read_excel('что-то.xlsx')
print(df.iloc[:,indexy])
indexx = int(input("введите cтрока: "))
print(df.iat[indexx,indexy])

