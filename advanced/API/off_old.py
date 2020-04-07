import requests
from sys import argv
import json


OFF_URL = "http://fr.openfoodfacts.org/"
SEARCH_URL = OFF_URL + "cgi/search.pl?"
HEADERS = {"UserAgent": "PyBeurre - ubuntu-18.04 - Version 0.1"}


class Api_reach():
    """ Interface between python programs and Open Food Facts API """

    def __init__(self):
        self.status_api = False

    def test(self):
        res = requests.get(OFF_URL, headers=HEADERS)
        if res.status_code == requests.codes.ok:
            self.status_api = True
        else:
            print("Open Food Facts API is not currently available.")
            exit(0)

    def findBrand(self, brand_name):

        payload = {
            "search_terms": "{}".format(brand_name),
            "search_tag": "brands",
            "sort_by": "unique_scans_n",
            "page_size": 50,
            "json": 1
        }

        res = requests.get(SEARCH_URL, params=payload)
        results = res.json()

        products = results["products"]
        product_nbr = 0
        for product in products:
            print(product["product_name"])
            product_nbr += 1

        print("{} products found.".format(product_nbr))

    def findgeneric(self, product):

        payload = {
            "search_terms": "{}".format(product),
            "search_tag": "product",
            "json" : 1
        }

        res = requests.get(SEARCH_URL, params=payload)
        results = res.json()

        prod = results["products"]

        print("GENERIC NAME :" + prod[1]["generic_name"])
        return prod[1]["generic_name_fr"]

    def similarto(self, product):

        generic = self.findgeneric(product)

        payload = {
            "search_terms": "{}".format(generic),
            "page_size" : 1,
            "json" : 1
        }

        res = requests.get(SEARCH_URL, params=payload)
        results = res.json()
        products = results["products"]

        print("SIMILAR PRODUCTS :")
        for product in products:
            print(product["product_name"])

    def getalltags(self):

        payload = {
            "search_terms": "coca cola",
            "search_tag": "product",
            "language": "fr",
            "json" : 1
        }

        res = requests.get(SEARCH_URL, params=payload)
        results = res.json()

        tags = results["products"][1]

        for info in tags:
            print(info)

        return tags

    def slicetags(self):
        tags = self.getalltags()
        print()
        print(tags["generic_name_fr"])
        print(tags["nutriscore_score"])


    def get_categories(self):
        '''get categories from the URL API'''
        req = requests.get('https://fr.openfoodfacts.org/categories&json=1')
        data_json = req.json()
        data_tags = data_json.get('tags')
        data_cat = [d.get('name', 'None') for d in data_tags]
        i = 0
        for cat in data_cat:
            print(cat)
            i += 1
            if i == 10:
                break

        print(i)

    def get_category(self):
        '''get categories from the URL API'''
        r_cat = requests.get('https://fr.openfoodfacts.org/categories&json=1')
        data_json = r_cat.json()
        data_tags = data_json.get('tags')
        data_cat = [d.get('name', 'None') for d in data_tags]
        i = 2
        while i < 12:
            print("{}".format(data_cat[i]))

            i=i+1

    def test(self):
        payload = {
            'action': 'process',
            'tagtype_0': 'categories', #which subject is selected (categories)
            'tag_contains_0': 'contains', #contains or not
            'tag_0': 'snacks', #parameters to choose
            'sort_by': 'unique_scans_n',
            'page_size': '100',
            'countries': 'France',
            'json': 1,
            'page': 150
        }

        r_food = requests.get('https://fr.openfoodfacts.org/cgi/search.pl', params=payload)
        food_json = r_food.json()
        test2 = food_json.get('products')
        print(test2[1]['product_name_fr'])

        i = 0
        for product in test2:
            print(test2[i]['product_name'])
            i+=1

    def insert_values_aliment(self):
        CATEGORIES_TO_DISPLAY = [(None, "boissons-alcoolisees")]
        """Method that inserts our aliemnt into the aliment table
            by searching through our API : Openfoodfacts"""

        id_category = 0
        for names in CATEGORIES_TO_DISPLAY:
            # We get our aliment based on our categories
            for page in range(1, 4):
                link = f"""https://fr.openfoodfacts.org/categorie/
                        {CATEGORIES_TO_DISPLAY[id_category][1]}
                        /{page}.json"""
                response = requests.get(link)
                category_json = json.loads(response.text)


                for products in category_json["products"]:

                    sql_formula_aliment = {products["product_name"]}
                    print(sql_formula_aliment)


if __name__ == "__main__":
    OFF_reach = Api_reach()
    OFF_reach.insert_values_aliment()
