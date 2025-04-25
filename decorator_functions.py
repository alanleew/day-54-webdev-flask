# TODO 1: Passing first-class objects (functions) as arguments
# def add(n1, n2):
#     return n1 + n2
#
# def calculate(function, n1, n2):
#     return function(n1, n2)
#
# result = calculate(add, 1, 2)
# print(result)


# TODO 2: Nested functions
# def outer_function():
#     print("This is the outer function")
#
#     def nested_function():
#         print("I'm inner!")
#
#     nested_function() # This would not work if it is outside of scope
#
# outer_function()

# TODO 3: Functions returned from other functions
# def outer_function():
#     print("This is the outer function")
#
#     def nested_function():
#         print("I'm inner!")
#
#     return nested_function    # Omit () to avoid activating function
#                               # Remember to avoid adding () when returning functions
#
# inner_function = outer_function()
# inner_function()

# TODO 4: Python Decorator Function
# def decorator_function(function):
#     """Adds additional features to preexisting methods"""
#     def wrapper_function():
#         # add_functionality()
#         function()
#     return wrapper_function

def doubler_decorator(function):
    def wrapper_function():
        function()
        function()
    return wrapper_function

@doubler_decorator
def say_hello():
    print("Hello")

def say_bye():
    print("Bye")

say_hello() # Has decorator
say_bye()   # Does not have decorator

