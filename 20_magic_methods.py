int_num = 50
float_num = 7.5
str_val = 'qwe'


print('int_num + float_num :', int_num + float_num)
# int_num + float_num : 57.5

print('int_num * float_num :', int_num * float_num)
# int_num * float_num : 375.0

""" __mul__() """
print('int_num.__mul__(float_num): ', int_num.__mul__(float_num))
# int_num.__mul__(float_num):  NotImplemented

print('int_num.__mul__("string"): ', int_num.__mul__('string'))
# int_num.__mul__("string"):  NotImplemented

""" __rmul__() """
print('float_num.__rmul__(int_num): ', float_num.__rmul__(int_num))
# float_num.__rmul__(int_num):  375.0

print('int_num * str_val :', int_num * str_val)
# qweqweqweqweqweqweqweqweqweqweqweqweqweqweqweqweqweqweqweqweqweqweqweqweqweqweqweqweqweqweqweqweqweqweqweqweqweqweqweqweqweqweqweqweqweqweqweqweqweqwe


print('str_val * int_num: ', str_val * int_num)
# the same

print('int_num.__mul__(str_val): ', int_num.__mul__(str_val))
# int_num.__mul__(str_val):  NotImplemented

print('str_val.__rmul__(int_num) :', str_val.__rmul__(int_num))
# qwe...

print('dir(bool) :', dir(bool))
""" 
dir(bool) : ['__abs__', '__add__', '__and__', '__bool__', '__ceil__',
 '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', 
 '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', 
 '__getattribute__', '__getnewargs__', '__getstate__', '__gt__',
   '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', 
 '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', 
'__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__',
     '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', 
 '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__',
     '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__',
     '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__',
 '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', 
 '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate',
 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']

   """

print('bool.__doc__ :', bool.__doc__)
"""  Returns True when the argument x is true, False otherwise.
 The builtins True and False are the only two instances of the class bool.
 The class bool is a subclass of the class int, and cannot be subclassed. """

print('str.__doc__ :', str.__doc__)

""" 
 str.__doc__ : str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to sys.getdefaultencoding().
errors defaults to 'strict'. """
