import requests
import math

base_url = "https://pokeapi.co/api/v2/pokemon/{}"

file = open("mock.txt", "w+")
content = ""

def largeImageUrl(index):
    return "https://assets.pokemon.com/assets/cms2/img/pokedex/full/" + str(index).zfill(3) + ".png"

def typesStr(types):
    toReturn = "["
    for type in types:
        toReturn += "\"" + type["type"]["name"].capitalize() + "\", "
    toReturn = toReturn[:-2]
    return toReturn + "]"

def weightToPounds(weight):
    return str(round((weight * 0.2205), 1))

def heightFeet(height):
    return str(math.floor(height / 3.048))

def heightInches(height):
    inches = round(((height/10)*39.3701) % 12)
    if (inches < 12):
        return str(inches).zfill(2)
    else:
        return "00"

for index in range(800,808): #965
    print(index)
    pokemon = requests.get(base_url.format(str(index))).json()

    content += "{\n"
    content += "\t\tid: " + str(pokemon["id"]) + ",\n"
    content += "\t\tname: \"" + str(pokemon["name"]).capitalize() + "\",\n"
    content += "\t\tfeet: \"" + heightFeet(pokemon["height"]) + "\",\n"
    content += "\t\tinches: \"" + heightInches(pokemon["height"]) + "\",\n"
    content += "\t\tweight: \"" + weightToPounds(pokemon["weight"]) + "\",\n"
    content += "\t\tlittle_image: \"" + str(pokemon["sprites"]["front_default"]) + "\",\n"
    content += "\t\tlarge_image: \"" + largeImageUrl(index) + "\",\n"
    content += "\t\ttypes: " + typesStr(pokemon["types"]) + "\n"
    content += "},\n"

content = content[:-2]

file.write(content)
file.close()
