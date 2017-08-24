import urllib.request
from bs4 import BeautifulSoup


url = "https://www.rottentomatoes.com/"

html = urllib.request.urlopen(url)
source = html.read()
html.close()

soup = BeautifulSoup(source, "html.parser")

table = soup.find(id="Top-Box-Office")

all_tr = table.find_all("tr")

for tr in all_tr:
    all_td = tr.find_all("td")
    score = all_td[0].find("span", attrs={"class":"tMeterScore"}).text.strip("%")
    movie_name = all_td[1].a.text
    amount = all_td[2].a.text.strip().strip("$")
    
    print("0." + score, movie_name, amount)