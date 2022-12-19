welcome_text="""
Welcome to game \'Leaguage Of Empires\'!
In this game you rebuild your own civilization and you\'ll figth on a few wars, I hope you are ready for new adventure.
But firstly choose your character. Good luck!
"""
print(welcome_text)
print(70*'-')
nations=('ROMAN', 'VIKING', 'EGIPTIAN', 'ZULUS', 'GERMAN', 'GREEK')
print(f'Okay, so who do you choose? You want to be {nations}')
nation=input('Provide your nation: ').upper()
while nation not in nations:
    nation=input(f'Sorry, I do not understand your input: {nation}, please enter again: ').upper()

print(f'Great! You have choosen: {nation}')
print(70*'-')
name=input('So, what\'s your name? Please enter your name: ')
print(f'Welcome new lord {name}')
print(70*'-')
city=input('So, let\'s begin with first step, how do you call your first town?: ')
print(f'New city: {city} is built by: {name}. ')
print(70*'-')
print('You have done first step, now what do you want to build in your new town?')
buildings=('BARACKS', 'HOUSES', 'TENTS', 'CASTLE')
building=input(f'Provide your building which you want to build: {buildings} ').upper()
while building not in buildings:
    building=input(f'You can\'t build this building: {building}').upper()

