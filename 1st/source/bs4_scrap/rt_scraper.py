import urllib.request
from bs4 import BeautifulSoup


url = "https://www.rottentomatoes.com"
html = urllib.request.urlopen(url)

source = html.read()
html.close()

soup = BeautifulSoup(source, 'html.parser')
# print(soup)

table = soup.find(id="Top-Box-Office")
# print(table)

all_tr = table.find_all("tr")
#print(all_tr)

for tr in all_tr:
    all_td = tr.find_all("td")
    score = all_td[0].find("span", attrs={"class":"tMeterScore"}).text
    movie_name = all_td[1].a.text
    amount = all_td[2].a.text
    print(score, movie_name, amount)
