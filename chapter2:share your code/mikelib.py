
"""
this is my comment!

"""

cast = [1, 2, 3,[4,5,6,7]]

def myLoop(temp):
    for item in temp:
        print(item)


def myLoopAll(temp):
    for item in temp:
        if isinstance(item, list):
            myLoop(item)
        else:
             print(item)

myLoop(cast)

print("-----------")

myLoopAll(cast)

print("-----------")

for num in range(4):
    print(cast[num])



print("\t", end='')
print("ttttt")