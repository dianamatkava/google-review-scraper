from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

URL = 'https://www.google.com/maps/place'


class GoogleReviews:
    driver:     webdriver.Chrome
    html_body:  BeautifulSoup

    reviewer:   str
    content:    str
    link:       str
    rating:     float
    date_time:  str
    replied:    bool
    reply_text: str

    def __init__(self) -> None:
        self.driver = webdriver.Chrome('driver/chromedriver.exe')

    def search(self, text:str):
        try:
            self.driver.get('?q='.join([URL, text]))
            self.driver.implicitly_wait(10)
            link = self.driver.find_element(
                By.XPATH,
                "//div[@class='ObqRqd']/following-sibling::div/span[2]/span[1]/span"
            )
            link.click()
            rating = self.driver.find_element(
                By.XPATH,
                "//div[@class='jANrlb']/div"
            ).text

            scroll_pause_time = 1
            screen_height = self.driver.execute_script("return window.screen.height;")

            reviews = self.driver.find_element(
                By.XPATH,
                "//div[@class='m6QErb']"
            )

            print(rating)    # 4.3 rating
            print(link.text) # 745 comments
            print(reviews.__dict__)
            print(reviews.page_source)


            import time
            time.sleep(1000)
        except Exception as _ex:
            return _ex, 400
        # return status,

    def get_reviews(self):
        # check if contains any review
        pass