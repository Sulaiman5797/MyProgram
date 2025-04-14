for i in range (1, 9):
    print(f'{i} * 5 = {i*5}')
for i in range (1, 9):
    print(i) #looping over a range with a for loop.
names = ['sulaiman', 'minhaz', 'toky']
for name in names:
    print(name) #looping over a list with a for loop.
    if name == 'toky': #using condition for find out a spcific name.
        for char in name:
            print(char) #looping over char variable which contain a name.
for x in range (5): 
    for y in range (7):
        print (x, y) #looping over a looop.[nested (loop]
dict1 = {'name': 'sulaiman', 'age':'27', 'home': 'habiganj'}
for dict2 in dict1:
    print(f'{dict2} : {dict1[dict2]}') #looping over a dictionary data type.
adress= {'name': 'sulaiman', 'home': 'sylhet'}
for ads, v in adress.items():
    print(f'{ads} : {v}')  #looping over a dictionary data type.

num = [4,5,3,6,-6,-5,-4,-3, 0]
for number in num:
    if number > 0:
        print(f'{number} is positive')
    elif number <0:
        print (f'{number} is positive')
    else:
        print(f'{number} is zero')
for number in num:
    if number %2==0:
        print (f'{number} is even')
    else:
        print (f'{number} is odd')
for z in range (1, 10):
    if z == 5:
        break
    print(z)
for z in range (1, 10):
    if z == 5:
        continue
    print(z)
