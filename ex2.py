"""
Exercise 2
"""

class calculate(object):
    def add(self, x, y):
        return x+y

if __name__ =='__main__':
    calc = calculate()
    result = calc.add(2, 5)
    print(result)

if __name__ =='__main__':
    calc = calculate()
    result = calc.add("Hello ", "Friends!")
    print(result)
    