def name_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            print (f"The name has to be more than 2 letters" ) 
            return None
    return inner

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me a name and a phone please."
        except IndexError:
            return "Give me a name and data please"
    return inner

def contact_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError: 
            return "The contact is not found"
        except IndexError:
            return "Give a valid name"
        except ValueError:
            return "Give a valid phone number please"
    return inner


def date_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Provide the correct number. Use DD.MM.YYYY"
        except KeyError:
            return "The contact is not found"
    return inner

