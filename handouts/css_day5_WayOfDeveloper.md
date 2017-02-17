# Fastcampus 
## Computer Science SCHOOL
### The Way of Developer
2017.2.17

---
<!-- page_number:true -->
## Advanced Web Crawling

---
## Selenium

---
## Web Crawling with Selenium
`$ pip install selenium`

---
## Web Crawling with Selenium
```python
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
```

---
## Web Crawling with Selenium
```python
ff_driver = webdriver.Firefox()
ff_driver.get("https://www.google.co.kr/")

query = ff_driver.find_element_by_id("lst-ib")
query.send_keys("패스트캠퍼스")

ff_driver.find_element_by_name("btnK").click()
ff_driver.implicitly_wait(10)
```


---
## Web Crawling with Selenium
```python
RESULTS_LOCATOR = "//div/h3/a"
WebDriverWait(ff_driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, RESULTS_LOCATOR)))
page1_results = ff_driver.find_elements(By.XPATH, RESULTS_LOCATOR)
for item in page1_results:
    print(item.text)
```

---
## Way of Developer

---
## Developer
![](https://s3.amazonaws.com/quantstart/media/images/article-images/Mailbag-How-Do-You-Move-From-Quant-Developer-To-Quant-Trader.jpg)

---
## Developer
- 시스템 분석가의 요구에 맞게 컴퓨터 프로그래밍을 하거나 시스템 설계를 하는 사람

### Difference between Developer, Programmer, Coder
- Developer: can design `system`
- Programmer: can design `algorithm`
- Coder: can produce `code` from `pseudo code`


---
## 개발자가 갖춰야 할 덕목

---
### Geekiness
![](http://www.arghink.com/wp-content/uploads/2015/06/geek_wallpaper____by_bigteddyrawr-d5us99o.png)

---
### Curiosity
![](https://c1.staticflickr.com/9/8205/8162305237_7c5fe5aa8a_b.jpg)

---
### Computational Thinking
![](https://upload.wikimedia.org/wikipedia/commons/1/17/ArtificialFictionBrain.png)

---
## 개발자가 알아야 할 언어

---
## 개발자가 알아야 할 언어
![](https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/Old_English_typeface.svg/1280px-Old_English_typeface.svg.png)

---
## 개발자가 함께 일 할 사람
![](http://www.thebluediamondgallery.com/wooden-tile/images/designer.jpg)

---
## 개발자가 함께 일 할 사람
![](https://c1.staticflickr.com/1/235/31545842551_92964229ff_b.jpg)

---
## 개발자가 함께 일 할 사람
![](https://c1.staticflickr.com/9/8506/8366351491_6edb945910.jpg)

---
## Mobile App Programming


---
## Web Programming

