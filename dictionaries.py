car_prices = {'opel': 5000, 'toyota': 7000, 'bmv': 10000}
print(car_prices)
print(car_prices['toyota'])
car_prices['mazda'] = 4000
print(car_prices)
# del car_prices['toyota']
# print(car_prices)
car_prices.clear()
print(car_prices)

person = {
    'first name': 'Jack',
    'last name': 'Brown',
    'age': 43,
    'hobbies': ['football', 'dancing', 'cooking'],
    'children': {'son': 'Michael', 'daughter': 'Pamela'}

}
print(person['age'])
print(person['hobbies'])
hobbies = person['hobbies']
print(hobbies[2])
print(person['hobbies'][2])
children = person['children']
print(person['children']['son'])

person['car'] = 'mazda'
person['hobbies'][0] = 'basketball'

print(person.keys())  # dict_keys
print(person.values())  # dict_values
print(person.items())  # dict_items

pizza = {
    'name': 'pepperoni',
    'size': 40,
    'meat': ['chicken', 'turkey','beef', 'pork'],
    'sauce': {'white': 'alfredo', 'red': 'tomato sauce'}
}
meat = pizza['meat']
print(meat[3])
print(pizza['name'])



