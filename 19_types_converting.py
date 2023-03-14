""" 5 + '10' """  # Error

""" 5 + int('10') """  # 15

"""  """
int_num = 5
float_num = 4.5

print('int_num + float_num: ', int_num + float_num)
# int_num + float_num:  9.5
# calls method __add__() [for the int class] =>
print('int_num.__add__(float_num): ', int_num.__add__(float_num))
# int_num.__add__(float_num):  NotImplemented
# IF python sees NotImplemented => it calls .__radd__() for float class
print('float_num.__radd__(int_num): ', float_num.__radd__(int_num))
# float_num.__radd__(int_num):  9.5


print('float_num + int_num: ', float_num + int_num)
# float_num + int_num:  9.5

"""  """

bool_val = True
int_value = 4.5

print('bool_val + int_value: ', bool_val + int_value)
# bool_val + float_num:  5.5

print('int_value + bool_val: ', int_value + bool_val)
# int_value + bool_val:  5.5
