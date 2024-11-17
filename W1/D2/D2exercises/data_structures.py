#list

my_list = [5,1,4,7,55,6,4,88,55,48,55]
my_list = list()

my_list.append(5)

#remove()
#pop(element)default = delete the last
#insert(index, element)
#index(element)

# while 55 in my_list:
#     my_list.pop(55)

# print(my_list)

sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

finished_sandwiches = []

while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

for sandwich in sandwich_orders.copy(): #because the list changes within the loop, we make a copy of it to avoid mutation during iteration
    finished_sandwiches.append(sandwich)
    sandwich_orders.remove(sandwich)

print(finished_sandwiches)
print(sandwich_orders)



