complex_a = 10 + 9j
complex_b = 4 + 7j

sum = complex_a + complex_b

print('sum: ', sum)
# sum:  (7+12j)

mines = complex_a - complex_b

print('mines: ', mines)
# mines:  (6+2j)

mult = complex_a * complex_b
print('mult: ', mult)
"""  
 (10 + 9j)(4 + 7j) = 40 + 70j + 36j + 63j^2 => means (^2) = -1 => means
 (10 + 9j)(4 + 7j) = 40 + 70j + 36j - 63
"""
""" !! mult:  (-23+106j) """


print('type(sum): ', type(sum))
# type(sum):  <class 'complex'>
