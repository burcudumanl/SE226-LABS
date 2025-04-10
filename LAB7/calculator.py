from pip._internal import operations
import math_utils
def main():
    operations={
       "+":math_utils.add,
       "-":math_utils.subtract(),
       "*":math_utils.multiply(),
        "/":math_utils.divide(),
        "%":math_utils.mod(),
        "**":math_utils.power(),
    }
    try:
        x=float (input("Enter a number: "))
        y=float (input("Enter another number: "))
        z=input("Enter an operator(+,-,*,/,%,**): ")
        if z in operations:
            result=operations[z](x,y)
            print(f"Result: {result}")
        else:
            print("Invalid operator")
    except ValueError:
        print("Invalid input! Please enter a numeric value")

if __name__=="__main__":
    main()


