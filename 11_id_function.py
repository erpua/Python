# id => returns address of object
my_number = 10
print(id(my_number))
#  140731262694472

my_string = 'qwe'
print(id(my_string))
#  2564135707760

# different object can have one link in memory space
my_number = 11
print(id(my_number))
# 140731262694504

my_other_number = my_number
print(id(my_other_number))
# 140731262694504 => the same

my_name = 'Ievgen'
print('id(my_name) => ')
print(id(my_name))

my_num = 100
print('id(my_num) =>', id(my_num))

other_num = my_num
print('id(other_num) =>', id(other_num))
