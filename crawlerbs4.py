import urllib.request as req
url="http://ncupress.ncu.edu.tw/"
request=req.Request(url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

import bs4
root=bs4.BeautifulSoup(data,"html.parser")
actives=root.find("div",class_="1i")
print(actives.1i.string)
