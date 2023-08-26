from bs4 import BeautifulSoup
import requests
url = "https://www.shcp.edu/academics/standardized-tests"
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('div', attrs={"class": "container grid-lg contentblock-text"})
    if table:
        for date in table.find_all("li")[:4]:
            print(date.get_text())
    #print(table)
else:
    print("nope")
