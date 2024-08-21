with open("file1.txt", "r") as f:
    string1 = f.readlines()
print(string1)
with open("file2.txt", "r") as f:
    string2 = f.readlines()
print(string2)
def replace_new_line_item(string):
    string = string.replace("\n", "")
    return string
def turn_str_to_int(string):
    string = int(string)
    return string

list1 = [replace_new_line_item(item) for item in string1]
list2 = [replace_new_line_item(item) for item in string2]
list1_int = [turn_str_to_int(item) for item in list1]
list2_int = [turn_str_to_int(item )for item in list2]
print(list1_int)
print(list2)





result = [item for item in list1_int if item in list2_int]

print(result)