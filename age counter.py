try:
    age= int(input("Enter your age: "))
    if age%2==0:
        print("This is an even number!")
    else:
        print("This is an odd number")

except ValueError:
    print("Please enter in numbers")

except SyntaxError:
    print("Please don't add unneccesary symbols.")

else:
    print("No exceptions")

finally:
    print("This will execute no matter what.")
