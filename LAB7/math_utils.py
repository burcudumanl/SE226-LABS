def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        print("You can't divide by zero")
def power(x,y):
    return x**y
def mod(x,y):
    return x%y
if __name__ == "__main__":
    print(f"Add: {add(3,4)}")
    print(f"Sub: {subtract(8,10)}")
    print(f"Multiply: {multiply(32,9)}")
    print(f"Divide: {divide(6,2)}")
    print(f"Power: {power(12,1)}")
    print(f"Mod: {mod(24,3)}")
