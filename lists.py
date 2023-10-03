mylist = ["banana", "cherry", "apple"]
print(mylist)

mylist2 = [5, True, "apple", "apple"]
print(mylist2)

# iterations
for item in mylist:
    print(item)

if "banana" in mylist:
    print("yes")
else:
    print("no")

print(len(mylist2))

mylist.append("lemon") # add to the end of the list
mylist.insert(1, "bluberry")

print(mylist)

item = mylist.pop()
print(item)
print(mylist)

new_list = sorted(mylist)
print(new_list)
print(mylist)

mylist.sort() #in-place
print(mylist)

mylist.reverse() #in-place
print(mylist)




mylist = [0] * 5
print(mylist) # [0, 0, 0, 0, 0]

mylist2 = [1, 2, 3, 4, 5]

new_list = mylist + mylist2
print(new_list) # [0, 0, 0, 0, 0, 1, 2, 3, 4, 5]

# Slicing
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]

a = mylist[1:5]
print(a)  # from index 1 to index 4

a = mylist[::2] # from index 1 to the end with a stepper of 2
print(a)


a = mylist[::-1] # a nice way to reverse the list
print(a)  

# appending the cpy will modify the org
list_org = ["banana", "cherry", "apple"]
list_cpy = list_org
list_cpy.append("lemon")
print(list_org)
print(list_cpy)

# correct ways to copy
list_cpy1 = list_org.copy()
list_cpy2 = list(list_org)
list_cpy3 = list_org[:]


# list comprehension
mylist = [1, 2, 3, 4, 5, 6]
b = [i * i for i in mylist] # syntax : expression forloop

print(mylist)
print(b)
