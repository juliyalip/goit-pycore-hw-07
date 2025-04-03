from decorators import input_error, contact_error, date_error
from classes import AddressBook, Record, Phone

def parse_input(user_input):
    print("Raw user input:", user_input)
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    print("Parsed cmd:", cmd)
    print("Parsed args:", args)
    return cmd, *args

@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    
    if not Phone(phone).is_valid():
        return "The phone must be 10 nummbers"
    
    record = book.find(name)
    message = "Contact updated."
    if record is None:    
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    
    record.add_phone(phone)
    return message

@input_error
@contact_error
def change_contact(args, book: AddressBook):
   name, number = args
   
   if not Phone(number).is_valid():
        raise ValueError    
   book[name]=number
   return "Contact updated."


@input_error
@contact_error
def show_phone(args, book: AddressBook):
    name = args[0]
    return book[name] 


@input_error
@date_error
def add_birthday(args, book: AddressBook):
    if len(args)<2:
        raise IndexError("Give me a name and data please.")
    name, date_br, *_ = args
    record = book.find(name)
    if not record:
        raise KeyError
    if not record.add_birthday(date_br):
        raise ValueError
    return "The date was added"
    
@input_error
@contact_error
def show_birthday(args, book: AddressBook):
    name=args[0]
    birthday = book[name].birthday
    return birthday.strftime("%d.%m.%Y") if birthday else "The birthday is not set" 
    

def birthdays(book: AddressBook):
   return book.get_upcoming_birthdays()



    
