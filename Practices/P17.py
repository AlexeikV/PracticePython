import requests
from bs4 import BeautifulSoup

base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text)

for cssbyr0y in soup.find_all(class_="css-14byr0y e1voiwgp0"):
    if cssbyr0y.a:
        print(cssbyr0y.a.text.replace("\n", " ").strip())
    else:
        print(cssbyr0y.contents[0].strip())