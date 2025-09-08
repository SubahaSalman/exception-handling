try:
    num1, num2 = eval(input("Enter two number in this format: , "))
    result = num1/num2
    print("Result is", result)

except ZeroDivisionError:
    print("Division by zero leads to an error!")

except SyntaxError:
    print("Comma is missing. Please enter using the given format: , ")

except:
    print("Wrong input")

else:
    print("No exceptions")

finally:
    print("This will execute no matter what.")