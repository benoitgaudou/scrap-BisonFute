import bs4
import os
from urllib import request

BF_EXTENSION = "ext"
BF_LOCATION = "location"
BF_DAY = "day"
BF_TIME = "time"

REP_DATA = "Data"
URL_BISON_FUTE = "http://tipi.bison-fute.gouv.fr/bison-fute-ouvert/publicationsDIR/TRAFICOLOR-DIR/"

def fileNameinfo(href):
    mapInfo = {}
    # Extenion
    list_elt_href = href.split(".")
    mapInfo[BF_EXTENSION] = list_elt_href[-1]

    fileName = "".join(list_elt_href[:-1])
    l_elt_name = fileName.split("_")
    mapInfo[BF_LOCATION] = l_elt_name[0]
    mapInfo[BF_DAY] = l_elt_name[-2]
    mapInfo[BF_TIME] = l_elt_name[-1]
    return mapInfo

def hasExtension(href, ext):
    list_elt_href = href.split(".")
    return list_elt_href[-1] == ext


os.makedirs(REP_DATA, exist_ok=True)

request_text = request.urlopen(URL_BISON_FUTE).read()
page = bs4.BeautifulSoup(request_text, "lxml")

for link in page.findAll("a"): #[1:10]:
    if hasExtension(link.get("href"), "xml"):
        fileLink = link.get("href")
        linkInfo = fileNameinfo(fileLink)
        path_to_save_rep = os.path.join(REP_DATA, linkInfo[BF_LOCATION], linkInfo[BF_DAY])
        os.makedirs(path_to_save_rep, exist_ok=True)
        path_to_save_file = os.path.join(path_to_save_rep, fileLink)

        if not os.path.isfile(path_to_save_file):
            request.urlretrieve(URL_BISON_FUTE + fileLink, path_to_save_file)
            print(fileLink, " downloaded")
        else:
            print(path_to_save_file, " already exists")
