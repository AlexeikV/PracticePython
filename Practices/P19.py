import requests
from bs4 import BeautifulSoup

def inspectWeb():
    URL = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
    response = requests.get(URL).text
    soup = BeautifulSoup(response, 'html.parser')
    text = []

    for element in soup.find_all('p'):
        text.append(element.text)

    for idx, p in enumerate(text):
        if idx <= 3 or idx >= len(text) - 4:
            continue
        print('\n' + p)

if __name__ == "__main__":
    inspectWeb()