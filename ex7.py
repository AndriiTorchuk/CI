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

print(sortfunc([3, 7, 7, 3, 5, 8, 9, 1]))