from os import system as sc
from sys import argv
import logging


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

token = "06494ef126fe6d600cf401fcec1f431966092e3a"
usr = "Neltarim"
url= "https://api.github.com/"
auth = "\"Authorization: token {}\"".format(token)


if argv[1] == "auth":
    url += "users/" + usr
    logger.debug("url = {}".format(url))
    sc("curl -i -u {}:${} {}".format(usr, token, url))

elif argv[1] == "get":
    url += argv[2] + argv[3]
    sc("curl -i {}".format(url))