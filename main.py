from bs4 import BeautifulSoup
import requests
url = "https://www.allrecipes.com/gallery/best-easy-cake-recipes-for-beginners/"
response = requests.get(url)

ingrDict = {}
endArr = []

ingrFracDict = {"½":0.5,
                "¾":0.75,
                "⅔":0.67,
                "¼":0.25,
                "1 ½":1.5,
                "1 ¾":1.75,
                "2 ½":2.5}

def getItem(soup):
    table = soup.find('ul', attrs={"class": "mntl-structured-ingredients__list"})
    if table:
        for ingr in table.find_all("li"):
            item = ingr.find("p")
    return item
def getIngrs(item):
    ingrs = []
    if item:
        oneIngr = []
        for part in item.find_all("span"):
            oneIngr.append(part.get_text())
            ingrs.append(" ".join(oneIngr))
    return ingrs
                
def getUnit(item):
    
    if item.find('span', attrs={"data-ingredient-unit":"true"}):
        ingrUnit = item.find('span', attrs={"data-ingredient-unit":"true"}).get_text()
    else:
        ingrUnit = None

    ingrName = item.find('span', attrs={"data-ingredient-name":"true"}).get_text()
    ingr = item.find('span', attrs={"data-ingredient-quantity":"true"}).get_text()
                
    if ingr != '':
        if ingr in ingrFracDict:
                ingrAmnt = ingrFracDict[ingr]
                
        else:
            ingrAmnt = int(ingr)
                
        i = 0
        while True:
            if i > len(ingrDict):
                break
            i += 1
            if ingrUnit != None:
                tempArr=[ingrName, ingrUnit]
                if ingrDict.get(str(tempArr)) != None:
                            
                    ingrDict[str(tempArr)] += ingrAmnt
                else:
                    ingrDict[str(tempArr)] = ingrAmnt   
    return ingrDict
                
        
def getCakeName():
    names = []
    heading = soup.find_all('h2', attrs={"class":"comp mntl-sc-list-item-title mntl-sc-block allrecipes-sc-block-heading mntl-sc-block-heading"})
    for i in range(len(heading)):
        name = heading[i].find('span', attrs={"class":"mntl-sc-block-heading__text"})
        names.append(name.get_text())
    return names

def useLink(cLink, i):
    arrEntry=[]
    link = cLink
    respond = requests.get(link)
    stew = BeautifulSoup(respond.content, "html.parser")
    
    printState = str(getCakeName()[i]) + "'s ingredients are: " + str(getIngrs(getItem(stew)))
    currentItem = getUnit(getItem(stew))

    arrEntry.append(printState)
    arrEntry.append(currentItem)

    return arrEntry
        
        




if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find_all('a', attrs={"class":"mntl-sc-block-featuredlink__link mntl-text-link button--contained-standard type--squirrel"})
    for i in range(5):
        print(useLink(links[i].get("href",None), i)[0])
    for i in range(10):
        print(useLink(links[i].get("href",None), i)[1])           
else:
    print("nope")

