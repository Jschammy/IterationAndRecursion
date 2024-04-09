# Justin Schamel
# CIS261
# IterationAndRecursion

# Make list with required
number_list = [0, 5, 10, 25, 50, 100]

# Function using For Loop to find factorials
def iterative_function(number):
    result = 1
    for i in range(1, number):
        result *= number
        number -= 1
    return result

# Function using Recursion to find factorials
def recursive_function(number):
    if number <= 1:
        return 1
    else:
        return number * recursive_function(number - 1)

# Show which method is being used
print("Factorial results using an iterative function:\n")

# Loop through number list to find all factorials
for item in(number_list):
    print(f"{item}! = {iterative_function(item)}")


# Show which method is being used
print("\nFactorial results using a recursive function:\n")

# Loop through number list to find all factorials
for item in(number_list):
    print(f"{item}! = {iterative_function(item)}")


    

