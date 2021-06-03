

def decorators_function(original_function):
    def wrapper_function():
        return original_function
    return wrapper_function()

def dispay():
    print('display function ran')

decorated_function = decorators_function(dispay())

decorated_function