
build = {"b1": ['1', '2'], "b2": ['3', '4'],
         "b3": ['5', '6'], "b4": ['7', '8']}
card = [int(i[-1]) + 1 for i in build.values()]
print(card)
