#user_name = input("Please enter  your username ")
#username_password = input("Please enter your password ")

#len_of_password = len(username_password)
#stars = '*' * len_of_password

#print(f"{user_name}, your password {stars} is  {len_of_password} letter long")

list_of_products = ['oranges', 'grapes', 'tomatos', 'banana','pineapple']
list_of_products[3] = 'cucumber'

changer_list = list_of_products 
changer_list[3] = 'eggplant'

print(f"this is the proof of concept that list_of_products changed by changer_list \n {list_of_products}", "\n")
print(f'there is the changer_list\n {changer_list}\n')

#this is concept of hard link that "one data source " can be changed by two hard links

# but we can use other slice copy in order to not change initial source we we modify second list 

copy_list = list_of_products [:]
copy_list[3] = 'banana'

print("\t New list", copy_list )

print("\t First intial list ", list_of_products)