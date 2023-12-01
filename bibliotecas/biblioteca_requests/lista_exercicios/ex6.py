import requests

dishes = []

for i in range(3):
    response = requests.get('https://www.themealdb.com/api/json/v1/1/random.php').json()
    meal = response['meals'][0]
    dish = meal['strMeal']
    dishes.append(dish)

receita1 = dishes[0]
receita2 = dishes[1]
receita3 = dishes[2]

print(receita1)
print(receita2)
print(receita3)