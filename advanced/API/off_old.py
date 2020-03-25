import requests


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
            print(self.status_api)
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

        print(prod[1]["generic_name"])
        return prod[1]["generic_name"]

    def similarto(self):

        generic = self.findgeneric("jambon")

        payload = {
            "search_terms": "{}".format(generic),
            "page_size" : 1,
            "json" : 1
        }

        res = requests.get(SEARCH_URL, params=payload)
        results = res.json()
        products = results["products"]

        for product in products:
            print(product["product_name"])
        

if __name__ == "__main__":
    OFF_reach = Api_reach()
    OFF_reach.similarto()