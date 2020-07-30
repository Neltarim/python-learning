import requests

OFF_URL = "http://fr.openfoodfacts.org/"
SEARCH_URL = OFF_URL + "cgi/search.pl?"
HEADERS = {"UserAgent": "PyBeurre - ubuntu-18.04 - Version 0.1"}

def dump_tags():
    '''get categories tags from the URL API'''
    response = requests.get(OFF_URL + 'categories&json=1')
    data_json = response.json()
    data_tags = data_json.get('tags')
    wild_tags = [tag.get('name', 'None') for tag in data_tags]
    i = 0
    tags = []

    for cat in wild_tags:
        tags.append(cat)

        i += 1
        if i == 10:
            break

    return tags


def list_to_str(lst):
    listToStr = '$'.join([str(elem) for elem in lst])
    return listToStr

def str_to_list(str1):
    lst = []
    elem = ""
    
    for char in str1:
        if char != "$":
            elem += char

        else:
            lst.append(elem)
            elem = ""

    return lst

def cat_nbr(str1):
    nbr = ""
    for char in str1:
        if char == 'c' or char == 'a' or char == 't':
            pass
        else:
            nbr += char

    return nbr


def test(dict):
    str1 = ""
    salt    = "!salt:$"             + dict['salt']          + "&"
    sugars  = "!sugars:$"           + dict['sugars']        + "&"
    sat     = "!saturated-fat:$"    + dict['saturated-fat'] + "&"
    fat     = "!fat:$"              + dict['fat']           + "&"

    str1 += salt
    str1 += sugars
    str1 += sat
    str1 += fat

    return str1

def nutrient_to_str(dict):
    str1 = ""
    column = ""
    value = " "
    for col in dict:
        column = ""
        value = " "
        column = col
        value += dict[col]
        str1 += column + value + ","

    return str1

def nutrient_to_dict(str1):
    dest = {
        "salt"          : None,
        "sugars"        : None,
        "saturated-fat" : None,
        "fat"           : None
    }
    word = ""
    column = ""
    value = ""

    for char in str1:
        if char != " " and char != ",":
            word += char

        elif char == " ":
            column = word
            word = ""

        elif char == ",":
            dest[column] = word
            word = ""
            column = ""

    return dest

def prod_score(prod):
    lvls = {
        "low" : 1,
        "moderate" : 2,
        "high" : 3
    }

    types = {
        "salt" : 2,
        "sugars" : 2,
        "saturated-fat" : 4,
        "fat" : 3
    }

    score = 0

    for lvl in prod:
        if prod[lvl] != None:
            column = lvl
            value = prod[lvl]

            score += types[column] * lvls[value]

    return score



nutrient_levels = { 
         "salt":"low",
         "saturated-fat":"high",
         "fat":"high",
         "sugars": "high"
      }

dico1 = nutrient_to_str(nutrient_levels)
dico2 = nutrient_to_dict(dico1)

print(dico1)
print(dico2)

for lvl in dico2:
    if dico2[lvl] != None:
        print(dico2[lvl])

prod_score(dico2)