import urllib.request as req
url="https://ncu.edu.tw/rd/tw/index/index.php?root=6"
request=req.Request(url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")


import bs4
root=bs4.BeautifulSoup(data,"html.parser")
titles=root.find_all("td",class_="d2 d22")
for title in titles:
    print(title.a.string)