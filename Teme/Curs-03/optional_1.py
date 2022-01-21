# TEMA 1.
# Realizați comportamentul funcției append() utilizând funcția insert().
my_first_list = [1, 2, 3, 4, 5]
my_second_list = [1, 2, 3, 4, 5]

control_number = 10

my_first_list.append(control_number)
my_second_list.insert(len(my_second_list), control_number)

print(my_first_list == my_second_list)
