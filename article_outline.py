class ArticleOutline:
    def __init__(self,title,link,org_date):
        super().__init__()

        self.title = title
        self.link = link
        self.org_date = org_date

    def printArticleOutline(self):
        print({"title": self.title,"link": self.link,"org_date": self.org_date})

    def toJSON(self):
        return{"title":self.title,"link":self.link,"org_date":self.org_date}