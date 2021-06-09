def beCheerful(name='', repeat=2): #default parameters can be optional for the caller of the function 
    print(f'good morning {name}\n' * repeat)
beCheerful()
beCheerful('Bennett')
beCheerful(name='Jospeh')
beCheerful(repeat=6)
beCheerful(name='Ife', repeat=4)
beCheerful(repeat=7, name='King Okotcha')