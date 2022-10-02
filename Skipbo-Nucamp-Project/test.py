import skipbo

""" build = {"b1": ['1', '2'], "b2": ['3', '4'],
         "b3": ['5', '6'], "b4": ['7', '8']}
card = [int(max(i)) + 1 for i in list(build.values())]

#print(list(build.values()))
print([i[-1] for i in list(build.values())]) """

"""hand = [1,2,3]

discards = [10,12]

discards.remove(12)

print(discards)"""

""" a = skipbo.player("a")

a.hand = ['1','2','3','4']

print(a.top_discards())
print(a.discard_pile)

a.discard('4','d3')

print(a.top_discards())
print(a.discard_pile) """

list = []
print(list[-1])