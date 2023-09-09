from bs4 import BeautifulSoup
import requests
url = "https://www.allrecipes.com/gallery/best-easy-cake-recipes-for-beginners/"
response = requests.get(url)

ingrDict = {}
ingrFracDict = {"½":0.5,
                "¾":0.75,
                "⅔":0.67,
                "¼":0.25,
                "¾":0.75,
                "¾":0.75,}

def getIngrs(soup):
    ingrs = []
    table = soup.find('ul', attrs={"class": "mntl-structured-ingredients__list"})
    if table:
        for ingr in table.find_all("li"):
            item = ingr.find("p")
            if item:
                oneIngr = []
                for part in item.find_all("span"):
                    oneIngr.append(part.get_text())
                ingrs.append(" ".join(oneIngr))
                ingrName = item.find('span', attrs={"data-ingredient-name":"true"})
                #ingrAmnt = int(item.find('span', attrs={"data-ingredient-quantity":"true"}))
                # print(type(int(item.find('span', attrs={"data-ingredient-quantity":"true"}).get_text())))
                # for i in range(len(ingrDict)):
                #     if ingrDict.get(ingrName) != None:
                #         break
        return ingrs
def getCakeName():
    names = []
    heading = soup.find_all('h2', attrs={"class":"comp mntl-sc-list-item-title mntl-sc-block allrecipes-sc-block-heading mntl-sc-block-heading"})
    for i in range(len(heading)):
        name = heading[i].find('span', attrs={"class":"mntl-sc-block-heading__text"})
        names.append(name.get_text())
    return names
def useLink(cLink, i):
    link = cLink
    respond = requests.get(link)
    stew = BeautifulSoup(respond.content, "html.parser")
    print(str(getCakeName()[i]) + "'s ingredients are: " + str(getIngrs(stew)))


if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find_all('a', attrs={"class":"mntl-sc-block-featuredlink__link mntl-text-link button--contained-standard type--squirrel"})
    for i in range(5):
        useLink(links[i].get("href",None), i)           
else:
    print("nope")

