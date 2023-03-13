my_name = 'Ievgen'
print('len(my_name) =>', len(my_name))
# length => 6

print('my_name[0] =>', my_name[0])
# I

print('my_name[3:6] =>', my_name[3:6])
# gen

print('my_name[2:] =>', my_name[2:])
# vgen

print('my_name[2:5] =>', my_name[2:5])
# vge => 2:5 means 2,3,4. 5 => Until 5, not include

# methods
# upper(), lower(), capitalize(), count(), index(), replace() etc.

my_comment = "This is my short comment"

print(len(my_comment))
# 24

my_comment.replace('short', 'long')
print(my_comment)
# This is my short comment => Returned first my_comment

print('my_comment.count(' ') =>', my_comment.count(' '))
# 4 spaces

print('my_comment.count("c") =>', my_comment.count('c'))
# 1 "c" symbol in my_comment

print('my_comment.count("is") =>', my_comment.count('is'))
# 2

print('my_comment[0] =>', my_comment[0])
# T

print('my_comment[-3] =>', my_comment[-3])
# e => -3 element from the end

print('my_comment[8:] =>', my_comment[8:])
# my_comment[8:] => my short comment

print('my_comment[:10] =>', my_comment[:10])
# my_comment[:10] => This is my  => from 0 to 9 included

print('my_comment[:] =>', my_comment[:])
# my_comment[:] => This is my short comment
