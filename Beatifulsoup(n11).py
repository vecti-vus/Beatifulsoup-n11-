from bs4 import BeautifulSoup
import requests
url =("https://www.n11.com/bilgisayar/dizustu-bilgisayar")

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

list = soup.find_all("li", {"class": "column"})

for li in list:
    name = li.div.a.h3.text.strip()
    link = li.div.a.get("href")
    if len(li.find("div", {"class": "proDetail"}).find_all("a")) > 1:
        oldprice = li.find("div", {"class":"proDetail"}).find_all("a")[0].text.strip().strip("TL")
        newprice = li.find("div", {"class": "proDetail"}).find_all("a")[1].text.strip().strip("TL")
    print(f"name: {name} link: {link} oldprice: {oldprice} newprice: {newprice}")