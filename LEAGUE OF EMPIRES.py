import messages as msg

# Welcome section
welcome_text="""
Welcome to game \'Leaguage Of Empires\'!
In this game you rebuild your own civilization and you\'ll figth on a few wars, I hope you are ready for new adventure.
But firstly choose your character. Good luck!
"""
print(msg.welcome)
print(welcome_text)

# Select nation
print(70*'-')
nation_list=('ROMAN', 'VIKING', 'EGIPTIAN', 'ZULUS', 'GERMAN', 'GREEK', 'ARABIAN')
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
building_list=('BARRACKS', 'HOUSES', 'TENTS', 'CASTLE')

building=input(f'Provide your building which you want to build: {building_list} ').upper()
while building not in building_list:
    building=input(f'You can\'t build this building: {building}').upper()
print(f'Great! Emperor {name} built: {building} in city: {city}')

print(70*'-')
#Choose people to work for you.
people_list=('MILITARY', 'NORMAL', 'FARMERS', 'BUILDERS')
people=input(f'Do you want to have more miltary people, or normal people? You can choose: {people_list}: ').upper()

while people not in people_list:
    people=input(f'This people are not yet unlocked plase try again: ').upper()
print('Very good, now you have 110 people in your city')

print(70*'-')
#You have finished LVL1.
print('Great! You have finished LVL1. Now you are on the LVL2.')
print(70*'-')

#Do you want first war?
war_list=('PEACE', 'WAR')
war=input(f'The first lord of other counry came, he want to ask you for peace, but you can say you want a war. {war_list}: ').upper()
print(f'The other emperor is fine with your {war}')
print(70*'-')

if war=="WAR":
    if building in ('BARRACKS','TENTS'):
        print('Great, You won your first war!')
    else:
        print('Unfortunately you lost, you have to restart your game. I\'M SORRY.')
        print(msg.game_over)
        quit()
print(70*'')

# Add new unit to the first city
military_list=('CAVALERY', 'ARCHERS', 'INFANTRY', 'GLADIATORS')
military2=input(f'Now, you can choose new mlitary people which you choose? {military_list}: ').upper()

while military2 not in military_list:
    military2=input('I don\'t understand your selection: {military2}. Please enter again: ')
print(70*'-')

#Build new city
city2=input('Now you can build new city. How do you\'ll call new city? ')
print(f'{name} built new city: {city2}.')
print(70*'-')