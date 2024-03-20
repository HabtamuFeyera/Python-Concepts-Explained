# A decorator function takes another function as argument, wraps its behaviour inside
# an inner function, and returns the wrapped function.
def start_end_decorator(func):

    def wrapper():
        print('This is where I Start')
        func()
        print('At this point I will finish it')
    return wrapper

def print_name():
    print('Alex')

print_name()

print()

# Now wrap the function by passing it as argument to the decorator function
# and asign it to itself -> Our function has extended behaviour!
print_name = start_end_decorator(print_name)
print_name()



print("This is the examples of the decorators")

@start_end_decorator
def print_name():
    print('Alex')

print_name()