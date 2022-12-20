# Welcome section
welcome_text="""
Welcome to game \'Leaguage Of Empires\'!
In this game you rebuild your own civilization and you\'ll figth on a few wars, I hope you are ready for new adventure.
But firstly choose your character. Good luck!
"""
print(welcome_text)

# Select nation
print(70*'-')
nation_list=('ROMAN', 'VIKING', 'EGIPTIAN', 'ZULUS', 'GERMAN', 'GREEK')
print(f'Okay, so who do you choose? You want to be {nation_list}')
nation=input('Provide your nation: ').upper()
while nation not in nation_list:
    nation=input(f'Sorry, I do not understand your input: {nation}, please enter again: ').upper()
print(f'Great! You have choosen: {nation}')

# Define player's name.
print(70*'-')
name=input('So, what\'s your name? Please enter your name: ')
print(f'Welcome emperor: {name}')

# Create first player's city.
print(70*'-')
city=input('So, let\'s begin with first step, how do you call your first town?: ')
print(f'New city: {city} is built by: {name}. ')

# Build first building in the city.
print(70*'-')
print('You have done first step, now what do you want to build in your new town?')
building_list=('BARACKS', 'HOUSES', 'TENTS', 'CASTLE')

building=input(f'Provide your building which you want to build: {building_list} ').upper()
while building not in building_list:
    building=input(f'You can\'t build this building: {building}').upper()
print(f'Great! Emperor {name} built: {building} in city: {city}')

print(70*'-')
#Choose people to work for you.
people_list=('MILITARY', 'NORMAL', 'FARMERS', 'BUILDERS')
people=input(f'Do you want to have more miltary people, or normal people? You can choose: {people_list}.').upper()

while people not in people_list:
    people=input(f'This people are not yet unlocked plase try again').upper()
print('Very good, now you have 110 people in your city')

print(70*'-')
#You have finished LVL1.
print('Great! You have finished LVL1. Now you are on the LVL2.')
print(70*'-')






