first_string = input("Enter a string: ")   #input for string
#blank variable to store the string with alternating upper and lowercase characters
alternates = ""  

#a for loop to convert the letters to upper and lower case
for i in range(len(first_string)):

    if i % 2 == 0:
        alternates = alternates + first_string[i].upper()
    else:
        alternates = alternates + first_string[i].lower()

print(alternates)

def alternate(s):
    words = s.split()
    for i in range(len(words)):
        if i % 2 == 0:
            words[i] = words[i].lower()
        else:
            words[i] = words[i].upper()
    return " ".join(words)

original_string = input("Enter a string: ")
print(alternate(original_string))
    