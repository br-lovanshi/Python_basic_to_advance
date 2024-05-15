str1 = "this is string"
str1 = str1.capitalize()
str1 = str1.upper()
str1 = str1.lower()

# boolean values
is_lower = str1.islower()
is_upper = str1.isupper()

#find substring in strings
sub_string = str1.find('string')

f_name = "Brajesh"
l_name = "Lovanshi"

#length of string
f_name_len = len(f_name)

# concatiation of strings
full_name = f_name + " " + l_name

#split string into list 
list = full_name.split(" ")


# access character 
char = full_name[0]
last_char = full_name[-1]

#extract substring using slice
sub_string = full_name[8:len(full_name)]
print(sub_string)