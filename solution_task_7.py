# Write a function that takes a list of numbers, and for each list element it should find the product of rest list
# elements excluding the current one.

# For example, given: [2, 5, 3, 4]
# Your function should return: [60, 24, 40, 30]
# By calculating: [5*3*4, 2*3*4, 2*5*4, 2*5*3]

def foo(list_a):
    mult_number = 1
    for i in list_a:
        mult_number *= i

    new_list = [int(mult_number/list_a[j]) for j in range(len(list_a))]
    return new_list

list_a = [2,5,3,4]
# print(list_a)
print(foo(list_a)) # [60, 24, 40, 30]
