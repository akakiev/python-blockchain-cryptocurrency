# 1) Write a normal function that accepts another function as an argument. Output the result of that other function in your “normal” function.
def another_func():
    return 'Hello function'

def normal_func(func):
    result = func()
    print(result)

another_func()
normal_func(another_func)
# 2) Call your “normal” function by passing a lambda function – which performs any operation of your choice – as an argument.
normal_func(lambda :'Hello from lambda')
normal_func(lambda :'Hello from lambda'*2)
# 3) Tweak your normal function by allowing an infinite amount of arguments on which your lambda function will be executed. 
def tweaked_func(func, *args):
    result = args[0]
    for i in args[1:]:
        if i > result: result = i
    print(result)
tweaked_func(lambda x:x, 1,2,5,4,3)
# 4) Format the output of your “normal” function such that numbers look nice and are centered in a 20 character column.
def fixed_tweaked_func(func, *args):
    result = args[0]
    for i in args[1:]:
        if i > result: result = i
    print(f'{result:.20f}')
fixed_tweaked_func(lambda x:x, 1,2,5,4,3)
