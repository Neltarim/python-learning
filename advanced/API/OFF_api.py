import requests
import logging


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

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
            logger.info(" status API={}".format(self.status_api))
        else:
            logger.debug(" status API={}".format(self.status_api))
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


if __name__ == "__main__":
    OFF_reach = Api_reach()
    OFF_reach.test()
    OFF_reach.findBrand("Lindt")