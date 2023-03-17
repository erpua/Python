"""
 my_fruits = ['apple', 'banana', 'mango']

posts_ids = [151, 265, 254, 8987]

user_inputs = [True, 'Hi', 'qwe', 10.5] 
"""

post_ids = [121, 125, 568, 7898]

print('post_ids: ', post_ids)
# post_ids:  [121, 125, 568, 7898]

post_ids[0] = 111
post_ids[2] = 333

print('post_ids after changing =>  ', post_ids)
# post_ids after changing =>   [111, 125, 333, 7898]


""" DELETING list elements """

user_inputs = [True, 'Hi', 'qwe', 10.5]

print('len(user_inputs):', len(user_inputs))
# len(user_inputs): 4

del user_inputs[1]
print('user_inputs after deleting:', user_inputs)
# user_inputs after deleting: [True, 'qwe', 10.5]
print('len(user_inputs) after del user_inputs[1]:',  len(user_inputs))
# len(user_inputs) after del user_inputs[1]: 3

del user_inputs[-1]
print('user_inputs after del user_inputs[-1]:', user_inputs)
# user_inputs after del user_inputs[-1]: [True, 'qwe']
print('len(user_inputs) after del user_inputs[-1]:',  len(user_inputs))
# len(user_inputs) after del user_inputs[-1]: 2
