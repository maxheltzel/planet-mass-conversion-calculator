#this calculator calculates your approximate weight on each plannet in our solar system
#the following metrics are the rough conversion rates of weights on other plannets
#this calculator will calculate in KG and LBS- no need to input which, it will automatically calculate it



user_planet = input("Which plannet would you like to calculate your weight on?: ")
if user_planet == 'mercury':
    print("Cool! Mercury is the closest planet from the sun and has the strongest gavitational pull!")
elif user_planet == 'venus':
    print('Nice! Did you know that venus is hotter than mercury despite it being further away from the sun?')
elif user_planet == 'earth':
    print("Nice! Did you know that earth's days are getting longer?")
elif user_planet == 'mars':
    print('Sounds Good! Did you know that mars is home to the tallets mountain in our solar system?')
elif user_planet == 'jupiter':
    print("Cool! Did you know that Jupiter's clouds are only 50km thick?")
elif user_planet == 'saturn':
    print('Cool! Did you know that Saturn orbits the Sun once every 29.4 years?')
elif user_planet == 'uranus':
    print('Nice! Did you know that Uranus is the coldest planet in the solar system')
elif user_planet == 'neptune':
    print('Sounds Good! Did you know that Neptune has the strongest winds in the entire Solar System?')
elif user_planet == 'pluto':
    print('Sounds Good! Did you know that Pluto is the largest dwarf plannet?')
if user_planet == 'Mercury':
    print("Cool! Mercury is the closest planet from the sun and has the strongest gavitational pull!")
elif user_planet == 'Venus':
    print('Nice! Did you know that venus is hotter than mercury despite it being further away from the sun?')
elif user_planet == 'Earth':
    print("Nice! Did you know that earth's days are getting longer?")
elif user_planet == 'Mars':
    print('Sounds Good! Did you know that mars is home to the tallets mountain in our solar system?')
elif user_planet == 'Jupiter':
    print("Cool! Did you know that Jupiter's clouds are only 50km thick?")
elif user_planet == 'Saturn':
    print('Cool! Did you know that Saturn orbits the Sun once every 29.4 years?')
elif user_planet == 'Uranus':
    print('Nice! Did you know that Uranus is the coldest planet in the solar system')
elif user_planet == 'Neptune':
    print('Sounds Good! Did you know that Neptune has the strongest winds in the entire Solar System?')
elif user_planet == 'Pluto':
    print('Sounds Good! Did you know that Pluto is the largest dwarf plannet?')


if user_planet == 'mercury':
    masscalc = 0.38
if user_planet == 'venus':
    masscalc = 0.91
if user_planet == 'earth':
    masscalc = 1.00
if user_planet == 'mars':
    masscalc = 0.38
if user_planet == 'jupiter':
    masscalc = 2.34
if user_planet == 'saturn':
    masscalc = 1.06
if user_planet == 'uranus':
    masscalc = 0.92
if user_planet == 'neptune':
    masscalc = 1.19
if user_planet == 'pluto':
    masscalc = 0.06
if user_planet == 'Mercury':
    masscalc = 0.38
if user_planet == 'Venus':
    masscalc = 0.91
if user_planet == 'Earth':
    masscalc = 1.00
if user_planet == 'Mars':
    masscalc = 0.38
if user_planet == 'Jupiter':
    masscalc = 2.34
if user_planet == 'Saturn':
    masscalc = 1.06
if user_planet == 'Uranus':
    masscalc = 0.92
if user_planet == 'Neptune':
    masscalc = 1.19
if user_planet == 'Pluto':
    masscalc = 0.06

user_mass = float(input( "What is your current weight on earth?: "))
final_weight = masscalc * user_mass

print("Your weight on " + str(user_planet) + " is roughly " + str(final_weight))

