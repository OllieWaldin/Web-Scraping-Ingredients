from bs4 import BeautifulSoup
import requests
url = "https://www.allrecipes.com/recipe/17481/simple-white-cake/"
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    def getIngrs():
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
        return ingrs
                        
    print(getIngrs())
else:
    print("nope")
