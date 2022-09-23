a = 0
x = 0

a = int(input("enter multiplier, a > "))
while a <= 0:
    a = int(input("it is better if number is higer, please re-enter > "))
    
x = int(input("enter limit, x > "))
while x <= 0:
    x = int(input("it is better if number is higher, please re-enter > "))

def iterate(multiplier, limit):
    i = 0
    print("currently, multiplier is",multiplier,"and limit is",limit)
    while i*multiplier <= limit:
        print(i*multiplier)
        i = i + 1

iterate(a, x)
iterate(a+1, 2*x)
iterate(a+2, 3*x)
