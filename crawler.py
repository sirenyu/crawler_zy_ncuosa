from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from article_outline import ArticleOutlin
from firebase_service import FirebaseService

def fetchArticleOutline(driver, index):
    global firebaseService


    title = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,f"/html/body/div/table[2]/tbody/tr[2]/td/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[{index}]/td/table/tbody/tr/td[2]/a")))

    link = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,f"/html/body/div/table[2]/tbody/tr[2]/td/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[{index}]/td/table/tbody/tr/td[2]/a")))

    org_date = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,f"/html/body/div/table[2]/tbody/tr[2]/td/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[{index}]/td/table/tbody/tr/td[2]/font")))

    articleOutline = ArticleOutline(title.text, link.get_attribute("href"),org_date.text)

        #articleOutline.printJSON()
    firebaseService.addArticleOutline(articleOutline)


def crawl():
    global firebaseService
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_experimental_option(
        "excludeSwitches",["enable-logging"])

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://osa.ncu.edu.tw/")

    for index in range(1, 10):
        fetchArticleOutline(driver, index)
    firebaseService.fetchData()
    driver.quit()

if __name__ == "__main__":
    firebaseService = FirebaseService()


    crawl()

