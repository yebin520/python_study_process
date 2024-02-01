#alien.py
alien_0 ={
    'alien1':'yellow',
    'alien2':'green',
    'alien3':'red',
    'alien4':'pinl',
    'alien4':'pinl',
}
print (alien_0)
del alien_0['alien4']
amd = alien_0.get('alien3','No this word')
alien_0 ['alien4']='pink'

for k in alien_0.keys():
    if k =='alien2':
        print (alien_0[k])
print (set(alien_0.values()))