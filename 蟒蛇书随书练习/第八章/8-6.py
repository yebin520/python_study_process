#8-6.py
def city_country(city,country):
    full_word = f"{city},{country}"
    return full_word
while True :
    print("enter 'quit' to break")
    city = input("\nThe city is :")
    if city == 'quit':
        break
    country = input("\nThe country is :")
    full_countrysied = city_country(city,country)
    print (full_countrysied)
    
