"""
Exercise 7
"""

def sortfunc(mylist):
    ss = True
    while ss:
        ss = False
        for i in range(len(mylist)-1):
            if mylist[i] > mylist[i+1]:
                mylist[i], mylist[i+1] = mylist[i+1], mylist[i]
                ss = True
    return mylist


if __name__ == '__main__':
    if sortfunc([3, 7, 2, 4, 5, 8, 6, 1]) != [1, 2, 3, 4, 5, 6, 7, 8]:
        print("Some mistake")

print(sortfunc([]))
print(sortfunc([5]))
print(sortfunc([2, 4, -5, 3, 0, -1]))

