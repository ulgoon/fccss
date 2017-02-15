# Fastcampus 
## Computer Science SCHOOL
### Network Basic (2)
2017.2.15

---
## A/S

python urlopen pycharm https problem

---
<!-- page_number:true -->
## Web Programming

---
### Web architecture

![](http://www.tutorialspoint.com/nodejs/images/web_architecture.jpg)

---
### 웹 개발 패턴의 변화

- 1991 ~ 1999: Sir Timothy John "Tim" Berners-Lee가 하이퍼텍스트 기반의 프로젝트를 제안한 이후 정적인 컨텐츠들을 중심으로 한 웹 기술이 발달
- 1999 ~ 2009: Linux, Apache, Mysql, Php 중심의 동적인 서버, 정적인 클라이언트 모델이 지속됨
- 2010 ~ 현재: javaScript!! (Dynamic Web Client)

---
## Web Browser

---
## Mosaic(1993)
![](https://image-proxy.namuwikiusercontent.com/r/http%3A%2F%2Fwww.wired.com%2Fimages_blogs%2Fthisdayintech%2F2010%2F04%2Fmos-10.jpg)

---
## Netscape(1994)
![](https://cdn.namuwikiusercontent.com/87/8756d0b9cf93d7465d8a9a7352f38612867c8c4917fefb7beecaaed568312064.png?e=1496053969&k=bJwxanlnVaBipJCwlHiCeA)

---
## Internet Explorer(1995)
![](https://cdn.namuwikiusercontent.com/c8/c818cb3186d258e2e29e17d307ab2c9206e4c4260888377ab927f3291433021f.png?e=1494793821&k=G8ktMKZrvriY1tYhGUN5NA)

---
## FireFox(2004)
![](https://cdn.namuwikiusercontent.com/88/88354691c8920f3ba11354f542039dd131cafe9fc897744c2feb15440d5eb36a.jpg?e=1490823670&k=RSpfp0LWCTnkw2HuZKBbtw)

---
## Chrome(2008)
![](https://techlog360.com/wp-content/uploads/2016/11/Simple-Hacks-And-Best-Tools-To-Limit-Memory-Usage-In-Google-Chrome.jpg)

---
## 웹 개발의 현재
### javaScript

---
## Client-side
- HTML/CSS, javaScript
- jQuery, AJAX
- Front-end Web Framework
	- AngularJS 2
	- React.js
	- Vue.js
- CSS Framework
	- Bootstrap
	- Foundation

---
## Server-side
- Depends on Language
	- PHP: Laravel
	- javaScript: Node.js(Express.js)
	- Java: Spring
	- C++, C#: ASP.net
	- Python: Django, Flask
	- Golang: itself
	- Ruby: Ruby on Rails

---
## Database
- RDBMS
	- MySQL
	- PostgreSQL
	- MariaDB
- noSQL
	- MongoDB
	- CouchDB
	- Redis


---
## etc
- celery (for Distributed Task Queue)
- github, Bitbucket, gitlab (for SCM)
- travis CI or jenkins (for Continuous Integration)
- slack, trello


---
## URI, URL, URN

### URI 
- Uniform Resource Information
- `https://www.example.com/post/how-to-make-url`
### URL 
- Uniform Resource Locator
- `https://www.example.com/post/`

### URN 
- Uniform Resource Name
- `www.example.com/post/how-to-make-url`

---
## REST API
`RE`presentational `S`tate `T`ransfer 
`A`pplication `P`rogramming `I`nterface

`Resource` - URI
`Verb` - HTTP method
`Representations` - 표현

---
## CRUD

### Create
### Read
### Update
### Delete

---
#### REST API 설계시 주의할 점

- 버전관리 https://api.foo.com/v1/bar
- 명사형 사용 https://foo.com/showid/ --> https://foo.com/user/
- 반응형 https://foo.com/m/user/, https://m.foo.com/user/ (x)
- 언어코드 https://foo.com/kr/, https://kr.foo.com/ (x)
- 응답상태 코드 (200, 400, 500)

---
## HTTP Response code

[wikipedia](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)

200, 201 - Success
400, 404 - Not found
500 - Server error

---
![](https://www.troyhunt.com/content/images/2016/02/41694168readImage2.png)

---
## Simple Server Framework: Flask
`$ pip install flask`
```python
from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
	return 'hello world!'
    
if __name__ == '__main__':
	app.run(host='0.0.0.0')
```

---
## Simple Server Framework: Flask
```python
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index(name=None):
	return render_template('index.html', name=name)

@app.route('/about')
def index(name=None):
	return render_template('about.html', name=name)

if __name__ == '__main__':
	app.run(host='0.0.0.0')
```

---
## Simple Server Framework: Flask

```
/
  simpleserver.py
  /templates
    index.html
    about.html
```

---
## Web Crawling with Python


---
## Scraping vs Crawling vs Parsing

Scraping: 데이터를 수집하는 행위

![](http://webdata-scraping.com/media/2013/11/web-scraping-services.png)

---
## Scraping vs Crawling vs Parsing
 
Crawling: 조직적 자동화된 방법으로 월드 와이드 웹을 탐색하는 것

![](https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/WebCrawlerArchitecture.svg/500px-WebCrawlerArchitecture.svg.png)

---
## Scraping vs Crawling vs Parsing

Parsing: 문장 혹은 문서를 구성 성분으로 분해하고 위계관계를 분석하여 문장의 구조를 결정하는 것

![](http://www.booooooom.com/wp-content/uploads/2013/11/michelgondry-tallhappy.jpg)

---
## Beautiful Soup

---
## Web Scraping with Beautiful Soup

`$ pip install beautifulsoup4`
![](img/css_bs4_2.png)

---
## Web Scraping with Beautiful Soup
![](img/css_bs4_3.png)

---
## Web Scraping with Beautiful Soup
![](img/css_bs4_4.png)

---
## Web Scraping with Beautiful Soup

```
import urllib
from bs4 import BeautifulSoup
html = """

uglified html code

"""
soup = BeautifulSoup(html, "html.parser")
print(soup.prettify())
```


---
## Web Scraping with Beautiful Soup
```
curl https://www.rottentomatoes.com
```

```python
import urllib.request
from bs4 import BeautifulSoup


url = "https://www.rottentomatoes.com"
html = urllib.request.urlopen(url)
source = html.read()
html.close()

soup = BeautifulSoup(source, "html.parser")
print(soup)

table = soup.find(id="Top-Box-Office")
print(table)
```

---
## Web Scraping with Beautiful Soup

```python
all_tr = table.find_all("tr")

for tr in all_tr:
     all_td = tr.find_all("td")
     score = all_td[0].find("span", attrs={"class":"tMeterScore"}).text
     movie_name = all_td[1].a.text
     amount = all_td[2].a.text
     print(score, movie_name, amount)
```


---
## Web Scraping with Beautiful Soup

![](img/css_bs4_5.png)

---
## Web Scraping with Beautiful Soup

![](img/css_bs4_6.png)

---
## So, Let's Scrap Naver