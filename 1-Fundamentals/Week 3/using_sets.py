"""numbers_set = {1, 2, 3, 4, 4}
print(numbers_set)"""

""" numbers_set = {1, 2, 3, 4, [5, 6]}"""

""" numbers_set = {1, 2, 3, 4, (5, 6)}
print(numbers_set) """

words_set = {"Alpha", "Bravo", "Charlie"}

""" abcd = ""
for word in words_set:
    abcd += word
print(abcd) """

words_set.add("Delta")
print(words_set)
words_set.discard("Bravo")
print(words_set)
