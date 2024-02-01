#people.py
people ={
    'Cyb':{
    'name':'Chen Yebin',
    'age':16,
    'school':'qz5z',
    },

    'Cj':{
    'name':'Chen Jing',
    'age':'16',
    'school':'qz1z',
    },

    'Zlx':{
    'naem' : 'ZLX',
    'age':17,
    'school': 'qz7z'
    },
}
for name,information in people.items():
    print (f"The name is {name} and his or her information is:\t")
    for name2,information2 in information.items():
        print ("\t",f"{name2}:{information2}")