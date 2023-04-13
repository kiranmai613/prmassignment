n = int(input("enter : "))
lst = []
for i in range(n):
    lst.append(input())

# define the custom key function
def sort_key(s):
    return s[-2]

# sort the list using the custom key function
sorted_lst = sorted(lst, key=sort_key)

# print the sorted list
print(sorted_lst)


