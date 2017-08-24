query = input("Enter the QUERY: ")
url = "https://search.naver.com/search.naver?where=post&query=%s" % query

html = urllib.request.urlopen(url)
source = html.read()
html.close()

soup = BeautifulSoup(source, "html.parser")
print(soup)

result_list = soup.find(id="elThumbnailResultArea")

all_li = result_list.find_all("li")

for li in all_li:
    title = li.find("dt")
    link = title.a['href']
    text = title.a['title']
    
    print(link, "\n", text)