# Parameters and without return value
def greet():
    print("Welcome to the function example")

# Parameters and return value
def add_numbers(a, b):
    result = a + b
    return result

# Arbitrary positional arguments
def print_info(*args):
    print("Arbitrary positional arguments:")
    for arg in args:
        print(arg)

# Arbitrary keyword arguments
def print_details(**kwargs):
    print("Arbitrary keyword arguments:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Default values
def power_of(base, exponent=2):
    result = base ** exponent
    return result

#Main Porogram
# Calling function without parameters and without return value
greet()

# Calling function with parameters and return value
num1 = 5
num2 = 3
sum_result = add_numbers(num1, num2)
print(f"Sum of {num1} and {num2} is: {sum_result}")

# Calling function with arbitrary positional arguments
print_info("John", 25, "Male")

# Calling function with arbitrary keyword arguments
print_details(name="Alice", age=30, gender="Female")

# Calling function with default values
base_num = 4
exponent_num = 3
result_power = power_of(base_num, exponent_num)
print(f"{base_num} raised to the power of {exponent_num} is: {result_power}")

# Calling function with default values (using the default exponent value)
result_default_power = power_of(base_num)
print(f"{base_num} raised to the default power is: {result_default_power}")

#Links
#https://codesolid.com/python-function-arguments-and-parameters-examples/
#https://builtin.com/software-engineering-perspectives/arguments-in-python
#https://www.datacamp.com/tutorial/functions-python-tutorial
#https://realpython.com/python-return-statement/#:~:text=A%20Python%20function%20will%20always,a%20default%20value%20for%20you.
#https://towardsdatascience.com/python-basics-functions-ed7c35e194a9?gi=4e7dfba59357
#https://www.toppr.com/guides/python-guide/references/methods-and-functions/function-argument/python-function-arguments-default-keyword-arbitrary/
#https://libguides.ntu.edu.sg/python/functionkwargs
#https://www.geeksforgeeks.org/default-arguments-in-python/

