import requests
import logging
from getpass import getpass


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

token = "06494ef126fe6d600cf401fcec1f431966092e3a"
usr = "neltarim"
url= "https://api.github.com/"
auth = "\"Authorization: token {}\"".format(token)


def nextInstruction():
    input("Press any key to continue ...")
    pass

def requestGetUser():
    password = getpass("password :")
    #r = requests.get('{}{}'.format(url, usr), auth=(usr, password))
    r = requests.get('{}users/{}'.format(url, usr), auth=(usr, password))
    logger.debug("status code :{}".format(r.status_code))

    if r.status_code == 404:
        exit(0)

    logger.debug("headers :" + r.headers['content-type'])
    nextInstruction()
    logger.debug("text :" + r.text)
    nextInstruction()
    formatted = r.json()
    login = formatted["login"]
    id_g = formatted["id"]
    print("login :{}\nid :{}".format(login, id_g))

def requestGetZen():

    angry = 60
    while angry != 0:
        r = requests.get('{}zen'.format(url, usr))

        if r.status_code == 404:
            logger.debug("status code :{}".format(r.status_code))
            exit(0)
        print(r.text)
        angry -= 1




def requestPost(): #not working but  interesting
    #password = getpass("password :")
    payload = {
        "name": "new_repo",
        "description": "test api with requests py"
    }
    head = {
        "Authorization": "token " + token
    }

    r = requests.post('{}user/repos'.format(url), params=head, data=payload)
    logger.debug("status code:{}".format(r.status_code))

def requestPost2(): #not working butinteresting

    r = requests.post(
    "https://api.github.com/users/{}/repos?access_token={}".format(usr, token), 
    data={
    "name": "Hello-World",
    "description": "This is your first repository",
    "homepage": "https://github.com",
})

requestPost()