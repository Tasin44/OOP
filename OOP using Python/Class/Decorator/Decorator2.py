#approach 1
def timer(get_factorial):
    def inner():
        print('Time start')
        get_factorial()
        print('Time End')
    return inner


def get_factorial():
    print('Factorial')

timer(get_factorial)()



#approach2
def timer(get_factorial):
    def inner():
        print('Time start2')
        get_factorial()
        print('Time End2')
    return inner

#Apply timer decorator to get_factorial:
@timer
def get_factorial():
    print('Factorial2')

get_factorial()