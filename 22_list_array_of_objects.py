users = [
    {
        'user_id': 134,
        'user_name': 'Alice'
    },
    {
        'user_id': 831,
        'user_name': 'Bob'
    }
]

print(users)
# [{'user_id': 134, 'user_name': 'Alice'}, {'user_id': 9831, 'user_name': 'Bob'}]

print('len(users): ', len(users))
# len(users):  2


print('users[1]["user_id"]:', users[1]['user_id'])
# users[1]["user_id"]: 831

my_fruit = 'apple'
other_fruit = 'banana'
another_fruit = 'mango'

all_fruits = [my_fruit, other_fruit, another_fruit]

print('all_fruits:', all_fruits)
# all_fruits: ['apple', 'banana', 'mango']
