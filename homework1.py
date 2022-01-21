import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset_url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv"
data = pd.read_csv(dataset_url, sep='\t')
data.head()

#1 Количество наблюдений

print('Количество наблюдений:', data.shape[0])


#2 Названия столбцов

print(list(data.columns))


#3 Самая частая позиция

print('Самая частая позиция:', data['item_name'].value_counts().idxmax())


#4 Гистограмма частоты заказов по позициям

data['item_name'].value_counts().plot.bar()
plt.title('Частота заказов по позициям')
plt.show()


#5 Изменение типа переменной item_price

data['item_price'] = data.apply(
    lambda x: float(x['item_price'].replace('$', '')),
    axis=1
)

#6 Гистограмма заработанных денег по каждой позиции

data[['item_name', 'item_price']].groupby('item_name').sum()['item_price'].plot.bar()
plt.title('Кол-во денег, заработанных по каждой позиции')
plt.show()


#7.1 Средняя сумма заказа

print((data[['order_id', 'item_price']].groupby('order_id').sum().sum() /
       data.order_id.max()).tolist()[0])


#7.2 Средняя сумма заказа

print(data[['order_id', 'item_price']].groupby('order_id').sum().mean().tolist()[0])


#8 Количество позиций в заказе

print('Максимальное, минимальное, среднее, медианное количество позиций в заказе:')
print(data[['order_id']].value_counts().agg(['max', 'min', 'mean', 'median']))

#9 Статистика заказов стейков, статистика заказов по прожарке

steak = data.loc[data['item_name'].str.contains('Steak')]
print('Заказы стейков:', steak.groupby('item_name')[['item_price', 'quantity']].describe())
steak_mild = steak.loc[steak['choice_description'].str.contains('Mild')]
steak_hot = steak.loc[steak['choice_description'].str.contains('Hot')]
steak_medium = steak.loc[steak['choice_description'].str.contains('Medium')]
print('Статистика заказов прожарки Mild:',
      steak_mild.groupby('item_name')[['item_price', 'quantity']].describe())
print('Статистика заказов прожарки Medium:',
      steak_medium.groupby('item_name')[['item_price', 'quantity']].describe())
print('Статистика заказов прожарки Hot:',
      steak_hot.groupby('item_name')[['item_price', 'quantity']].describe())


#10 Добавление столбца с ценами в рублях

data['r_price'] = round(data.item_price * 76.68, 2)
print(data['item_price'], data['r_price'])


#11 Группировка заказов по входящим позициям, по стейкам

print(data['item_name'].value_counts())
print('Uруппировка по стейкам:')
print (steak['item_name'].value_counts())


#12 Определение цены по каждой позиции

price = []
for id, row in data.iterrows():
    if 'and' not in row['item_name']:
        price.append(row['item_name'] + ' cost '
                      + str(round(row['item_price'] / row['quantity'], 2)) + '$')           

price = list(set((price)))
for i in price:
    print(i)







