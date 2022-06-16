contacts = {}

def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except (KeyError, ValueError, IndexError): 
            return "You should enter command (space) name (space) phone"
    
    return wrapper



def hello(*args):
    return 'How can I help you?'

def exit(*args):
    return 'Good bye'

@input_error
def add(*args):
    name=args[0]
    phone=args[1]
    # global contacts
    contacts[name]=phone
    return f'contact {name} added successfully'
    
@input_error
def change(*args):
    name=args[0]
    phone_n=args[1]
    for key in contacts.keys():
        if name == key:
            contacts[name] = phone_n
            return f'Contact {name} changed successfully'
        

def get_phone(*args):
    name=args[0]
    for key in contacts.keys():
        if name == key:
            user_phone = contacts.get(key)
    return user_phone

def show_all(*args):
    # return '\n'.join([f'{k}:{v}' for k,v in contacts.items()])
    lst=['{:<12}:{:>12}'.format(k,v) for k,v in contacts.items()]
    return '\n'.join(lst)

# COMM_EXIT=['good bye', 'exit', 'close', '.']
COMMANDS={exit:['good bye', 'exit', 'close', '.'],add:['add', 'додай'],change:['change','заміни'], get_phone:['phone', 'номер'],show_all:['show all','show'],hello:['hello','hi']}


def parse_command(request:str):
    for k,v in COMMANDS.items():
        for i in v:
            if request.lower().startswith(i.lower()):
                return k,request[len(i):].strip().split(' ')

def main():
    while True:
        request = input('You: ')
        
        result,data=parse_command(request)
        # print(data)
        # print(result())
        print(result(*data))
        
        if result is exit: #if result==exit:
            break
        
           
if __name__ == '__main__':
    main()
