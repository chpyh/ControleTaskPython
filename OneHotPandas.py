# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего 
#из 1 столбца. 
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?
import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
print(data)
print()
unique_elements = data['whoAmI'].unique()
oneHot_df = pd.DataFrame(0, index = data.index, columns = unique_elements)
for value in unique_elements:
    oneHot_df.loc[data['whoAmI'] == value, value] = 1
print(oneHot_df)

