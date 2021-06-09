def add(a,b): # function name - 'add', parameters: a and b
    x = a + b # process/equation
    return x # return value: x
print(add(21, 9))

# def say_hi(name):
#     print('Hi ' + name)
# say_hi('Bennett')
# say_hi('Collins')
# say_hi('Bowser')

def say_hi(name):
    return "Hi " + name
greeting = say_hi('Bennett')
print(greeting)
