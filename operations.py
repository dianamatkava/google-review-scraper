import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

URL = 'https://www.google.com/maps/place'


class ScraperException:
    

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

            # def get_reviews():
            rating = self.driver.find_element(
                By.XPATH,
                "//div[@class='jANrlb']/div"
            ).text
        except Exception as _ex:
            return _ex,

        def scroll(self, review_count):
            while True:
                self.driver.execute_script(
                    "document.getElementsByClassName('dS8AEf')[0].scrollTop = document.getElementsByClassName('dS8AEf')[0].scrollHeight"
                )
                time.sleep(2)
                reviews = self.driver.find_elements(By.CLASS_NAME, 'wiI7pd')
                print(len(reviews))
                if len(reviews) >= review_count:
                    break
            return self.driver



            scroll()
            print(rating)    # 4.3 rating
            # print(link.text) # 745 comments scrollable_div.scrollTop = scrollable_div.scrollHeight


        except Exception as _ex:
            return _ex, 400
        # return status,

    def get_reviews(self):
        # check if contains any review
        pass