#aliens.py
aliens = []
for i in range (30):
    new_alien = {'alien_1':'green','point':5}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print (alien)
print (f"The total number of the aliens is {len(aliens)}")