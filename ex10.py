"""
Exarcise 10. Loops For, If, If else, While
"""

count = [1,2,3,4,5];
fruits = ['apple', 'banan', 'orange', 'lemon', 'plam'];

for i in count:
    print ("This is count %d" %i);

elements = [];
for ii in range(0, 2):
    print ("Adding %d to the list" %ii);
    elements.append(ii);

elements = [];
i = 0;
while i < 6:
    print("At the top i is %d" %i);
    elements.append(i);
    i = i + 1;
    print ("number now: ", elements);

