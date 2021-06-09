# Sytnax + Conditionals
# x = 50
# if x > 50:
#     print('This is MY HOUSE!')
# else:
#     print("THIS IS NOT MY HOUSE, IM RENTING LOL :)".lower())

# x = 8
# if not x > 15 and x < 20:
#     print('Hes a big boy now!') # if its true it will operate the function (print...)
# elif x > 35: 
#     print("I guess we need Thor to deal with these Giants!!") # wont excute because ^ is true and it exits the function.
# else:
#     print('Im just a baby...little baby, give me a break')
# if x < 10:
#     print('smaller than 10') # new function/ if true, this will also print becuase its not part of the other function. 


class EmptyClass:
    pass

# Data-Types

# Tuples immuntable / cant change
# dog = ("Bowser", str(7), True, "multipoo", "mix-breed")
# print("Breed: " + dog[3].title(), "Age: " + dog[1], "Name: " + dog[0].title())


# # List mutable / can change / same as array in JS
# empty_list = []
# ninjas = ['subzero', 'scorpion', 'lu-Kang']
# print("lets name our favrotie ninjas".upper())
# print(ninjas)
# print(ninjas[1].title() + " is my favorite ninja in Mortal-Combat!")
# ninjas[0] = "`Law` from Tekken" #replace [0] with new variable "law from tekken"
# ninjas.append("Yoshimitsu") # add Yoshimitsu to the end of the list [Law from Tekken, scorpion, lu-kang, Yoshimitsu]
# print(ninjas)
# print(ninjas[-1].upper()) #YOSHIMITSU
# ninjas.pop() # removes last element in the list [Law from Tekken, scorpion, lu-kang]
# print(ninjas)
# # print(ninjas.pop()) # prints only the "popped" element lu-kang
# ninjas.append("Raiden") # add Raiden to the list of ninjas 
# print(ninjas) # [Law from tekken, scorpion, lu-kang, Raiden]
# ninjas.pop(0) # remove anyone that is not from mortal combat! 'Law from tekken'
# print(ninjas) # [scorpion, lu-kang, Raiden]

# Dictionaries a group of key-value pairs that are in the form of list with {Brackects}
# empty_dict = {}
# print('This is the fun-guy!'.title())
# fav_athlete = {'name': 'Kawhi Leonard', 'age': 29, 'height': "6'7 inch"}
# print(fav_athlete)
# fav_athlete['weight'] = 230 
# fav_athlete['teams'] = ['Spurs, Raptors, Clippers']
# print (fav_athlete) # print {'name': 'Kawhi Leonard', ('age'): str(29-30), 'height': "6'7 inch", 'teams': ['Spurs, Raptors, Clippers'] }
# how_tall = fav_athlete.pop('height')
# print(how_tall) # print "6'7 inch"
# print (fav_athlete['teams']) # prints list of teams within the dictionary


# print(type(fav_athlete))
# print(type(3.14))

# print(len(fav_athlete))
# print(len(fav_athlete['name'])) # prints the length of value of 'name' in the fav_athlete group.

# LOOPS
# for x in range(0, 10, 1): # x is the iterator// 0 is Start of range// 10 is End of range//1 interation through range
#     if x % 2 == 1:
#         print(str(x) + " is odd") # should print all the odd numbers
# for i in range(0, 10): # implied that it will iterate + 1 without the interation being there
#     if not i % 2 == 1:
#         print(str(i) + " is even") # should print all even numbers
# for n in range(10): # start of 0 and increment of +1 is implied with ounly the Range being listed!
#     if n >= 5:
#         print(str(n) + " >= 5")
# for t in range(0, 21, 4): # loop through 20 and grab every 4th number
#     print (str(t) + " is a multiple of 4") # should print 4 and every multiple of 4 
# for b in range(50, -1, -10): # interate from 50 to -1 by negative 10s
#     print("every-tenth num: " + str(b))

# tier_2avengers = ["winter soldier", "falcon", "black widow", "hawkeye"]
# for char in tier_2avengers:
#     print(char.title()) # print every character o the list capitlaized
# for char in range(0, len(tier_2avengers)):
#     print(char, tier_2avengers[char].upper())

kings_landing = {'house': 'Caselty Rock', 'symbol': 'Gold Lion', 'Words': 'Hear me Roar', 'motto': 'a Lannister always pays his debts!'}
# for k in kings_landing:
#     print("Key: " + k.upper()) # print Key: uppercase each key in the k-v pair
# for v in kings_landing:
#     print('Value: ' + kings_landing[v]) # prints all the values of the dictionary
# for v in kings_landing:  
#     print(v + ':', kings_landing[v])

# for key in kings_landing.keys():
#     print(key.title()) # keys in dictionary should print capt first letter
# for val in kings_landing.values():
#     print(val.upper()) # prints values uppercase
# for key, val in kings_landing.items():
#     print(key.title() + ' = ' + val.title()) 
# print(kings_landing['Words'].upper()) # not in the loop should just print value of key chosen uppercase.

# WHILE LOOPS // while a certain condition is true run the loop
count = 0
while count < 5: # do somehting until its false or else its an infinite loop 
    print("loop", count)
    count += 1

count = 5
while count > 0:
    print(str(count) + " seconds left")
    count -= 1
else:
    print("buzzer".upper()) # clock runs down to 5 by 1s and prints BUZZER when its done or at 0git