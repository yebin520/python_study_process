#person.py
def build_person(first_name,last_name,age = None):
    person = {'first':first_name,'last':last_name}
    if age:
        person['age']=age
    return person
musican =build_person('chen','yebin',age = 27)
print(musican)