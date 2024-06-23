# Introduction
## Install package
```shell
pip install browser_dog
```
## Preparation

- create file `linkedin_cookies.json`

- please use Chrome Extension `EditThisCookie` to export linkedin cookies to `linkedin_cookies.json`

##  Example Usage:

```python
from browser_dog.browser import BrowserDog

cat = BrowserDog('cookie.json', 'https://gitee.com', headless=True)
driver = cat.get_driver()

driver.get("https://gitee.com/login")
cat.long_wait()

# Get HTML
html = driver.page_source

```
