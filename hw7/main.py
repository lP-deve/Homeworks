
# items = input("enter number: ")

# set_items = set()

# for i in items.split():
#     set_items.add(i)

# print(set_items)
# print(frozenset(set_items))




# set_items1 = {"apple", "banana"}
# set_items2 = {"grapes", "orange"}
# tuple_items =tuple(set_items1.union(set_items2))
# print(tuple_items)




# numbers = (input("enter numbers: "))

# tuple_numbers = tuple((numbers).split())
# unique_numbers = list(set(tuple_numbers))

# print(unique_numbers)





# list_items = [("Gega", 24), ("Gaga", 21), ("Goga", 19), ("Giga", 27), ("Gagi", 11)]
# for name, age in list_items:
#     print(f"Name: {name}, Age: {age}")



customers = ["Irakli", "Giorgi", "Nona", "Oto"]
customers2 = ["Kato", "Levani", "Nino", "Dato", "Irakli", "Nemo"]

for user in customers:
    if user in customers2:
        print(user)
        
same_customers = set(customers) & set(customers2)
print(same_customers)





