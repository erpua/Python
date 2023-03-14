average_price = 17.25

print(average_price)
# 17.25

print('type(average_price): ', type(average_price))
# type(average_price):  <class 'float'>

average_price = 28.75
price = int(average_price)

print('price: ', price)
# price:  28

print('type(price): ', type(price))
# type(price):  <class 'int'>


""" str_temperature = 'qwe'
temperature = float(str_temperature)

print('temperature: ', temperature) """
# ValueError: could not convert string to float: 'qwe'

str_temperature = '14.5'
temperature = float(str_temperature)

print('temperature: ', temperature)
# 14.5

print('type(temperature): ', type(temperature))
# type(temperature):  <class 'float'>

another_price = 18.23

print('round(another_price): ', round(another_price))
# round(another_price):  18

rate = 0.78
print('round(rate): ', round(rate))
# round(rate):  1

print('type(round(rate)): ', type(round(rate)))
# type(round(rate)):  <class 'int'>
