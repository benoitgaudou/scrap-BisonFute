import bs4
from urllib import request

def hasExtension(href,  ext):
    list_elt_href = href.split(".")
    return list_elt_href[-1] == ext

print  ("DEBUT")
url_bison_fute = "http://tipi.bison-fute.gouv.fr/bison-fute-ouvert/publicationsDIR/TRAFICOLOR-DIR/"

request_text = request.urlopen(url_bison_fute).read()
page = bs4.BeautifulSoup(request_text, "lxml")

for link in page.findAll("a")[0:10]:
    if hasExtension(link.get("href"), "xml"):
        fileLink = link.get("href")
        request.urlretrieve(url_bison_fute + fileLink, fileLink)
print("END")
