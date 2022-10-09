def linear_search_dictionary(dict1, target):
    for k,v in dict1.items():
        if v == target:
            print("Target found.  Its key value is", k + ".")
            return k
    print("This dictionary doesnt contain the value", str(target) + ".")
    return None


my_dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}
linear_search_dictionary(my_dictionary, 5)
linear_search_dictionary(my_dictionary, 3)
linear_search_dictionary(my_dictionary, 8)