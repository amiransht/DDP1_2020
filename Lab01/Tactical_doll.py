nama = input("tactical doll name: ")
firepower = input('firepower: ')
firepower = int(firepower)
rate_of_fire = input('rate of fire: ')
rate_of_fire = int(rate_of_fire)
accuracy = input('accuracy: ')
accuracy = int(accuracy)
evasion = input('evasion: ')
evasion = int(evasion)


damage_per_second = firepower * rate_of_fire / 60
combat_effectiveness = 30 * firepower + 40 * (rate_of_fire**2/120) + 15 * (accuracy + evasion)

def dps():
    print("Damage per second: ", round(damage_per_second,2))
def ce():
    print("combat effectiveness: ", round(combat_effectiveness,2))

dps()
ce()

"""
CHALLENGE
"""
name = input("\ntactical doll name: ")
firepower = input('firepower: ')
firepower = int(firepower)
rate_of_fire = input('rate of fire: ')
rate_of_fire = int(rate_of_fire)
accuracy = input('accuracy: ')
accuracy = int(accuracy)
evasion = input('evasion: ')
evasion = int(evasion)

name2 = input("\ntactical doll opponent: ")
firepower2 = input('opponent firepower: ')
firepower2 = int(firepower2)
rate_of_fire2 = input('opponent rate of fire: ')
rate_of_fire2 = int(rate_of_fire2)
accuracy2 = input('opponent accuracy: ')
accuracy2 = int(accuracy2)
evasion2 = input('opponent evasion: ')
evasion2 = int(evasion2)

damage_per_second = firepower * rate_of_fire / 60
combat_effectiveness = 30 * firepower + 40 * (rate_of_fire**2/120) + 15 * (accuracy + evasion)
damage_per_second2 = firepower2 * rate_of_fire2 / 60
combat_effectiveness2 = 30 * firepower2 + 40 * (rate_of_fire2**2/120) + 15 * (accuracy2 + evasion2)

x = round(damage_per_second,2)
y = round(combat_effectiveness,2)
a = round(damage_per_second2,2)
b = round(combat_effectiveness2,2)


def dps():
    print("\n" + name + "\nDamage per second: " + str(x))
def ce():
    print("combat effectiveness: "+ str(y))
def dps2():
    print("\n" + name2 + "\nDamage per second: " + str(a))
def ce2():
    print("combat effectiveness: " + str(b))

dps()
ce()
dps2()
ce2()

if x > a and y > b:
    print("LAWAN DIA!")
else:
    print("MENGHINDAR")



