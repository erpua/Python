is_authorized = True

print('is_authorized: ', is_authorized)
# is_authorized:  True

print('type(is_authorized: ', type(is_authorized))
# type(is_authorized:  <class 'bool'>

print(100 > 24)  # True

print(-5 > 0)  # False

print('Long String' > 'Long')  # True
print('Long string' > 'String')  # False (symbol comparing)
print('Long string' > 'long')  # False (symbol comparing)

print([] == [])  # True
print([1] == [])  # False
print({'a': 3} == {'a': 5})  # False


print([1, 2, 3] == [1, 2, 3])  # True

"""  """

db_is_available = False

print('db_is_available: ', db_is_available)
# db_is_available:  False

print('type(db_is_available): ', type(db_is_available))
# type(db_is_available):  <class 'bool'>


db_is_available = True

print('db_is_available: ', db_is_available)
# db_is_available:  True

print(bool(10))
# True
print(bool('qwe'))
# True
print(bool([]))
# False
print(bool([1, 2]))
# True
print(bool(None))
# False
