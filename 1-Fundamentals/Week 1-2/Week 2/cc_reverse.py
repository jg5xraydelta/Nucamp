
def reverse(str):
    rev_str = ''
    for i in range(len(str)-1,-1,-1):
        rev_str = rev_str + str[i]
    return rev_str

name = input("What is your name? ")
print("Your name reversed is:", reverse(name))