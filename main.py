from bs4 import BeautifulSoup
import requests
url = "https://www.shcp.edu/academics/standardized-tests"
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup.title)
else:
    print("nope")
