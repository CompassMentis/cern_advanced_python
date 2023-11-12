# Todo: Create a class called 'CombinedList'

# Todo: The constructor should take two lists as parameters
#   and store them as attributes 'list_a', 'list_b'

# Todo: An instance of the class should function like a list
#   Each 'element' should be the sum of the same element from both original lists
#   For instance, combined_list[2] should return list_a[2] + list_b[2]
#   Note: Only sum the elements when you need it, not in advance

# Todo: Note the bonus exercise at the end



net_amount = [15, 20, 33, 100]
tax = [2, 5, 8, 20]
gross_amount_list = CombinedList(net_amount, tax)
print(gross_amount_list[0])

# Expected output:
# 17

# Todo (bonus): Create a method 'show(n)'
#   which prints: (value of list_a[n]) + (value of list_b[n]) = sum of both
#   This should use the method which you've already created to do the sum
# print(gross_amount_list.show(0))
# 15 + 2 = 17
