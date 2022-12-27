from __future__ import annotations
import time
from config import review_fields
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = 'https://www.google.com/maps/place'


class ScraperException:
    status_code: int
    message: str

    def __init__(self, status_code, message) -> None:
        self.status_code = status_code
        self.message = message

    def __str__(self):
        return f'{self.status_code}: {self.message}'

class Review:
    fields:     list[str]
    raw_review: dict

    def __init__(self) -> None:
        self.fields = review_fields
        self.raw_review = dict()

    def __str__(self) -> str:
        return f'{self.raw_review}'


class GoogleReview:
    name:           str
    global_rating:  int
    len_review:     int
    reviews:        list[Review]

    def __init__(self, name, rating, length) -> None:
        self.name = name
        self.global_rating = rating
        self.len_review = length
        self.reviews = list()


class GoogleReviewScraper:
    driver:     webdriver.Chrome
    google_review: GoogleReview

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
            review_amount = link.text.split(' ')[0]
            link.click()
            time.sleep(2)
            rating = self.driver.find_element(
                By.XPATH,
                "//div[@class='jANrlb']/div"
            ).text
            self.google_review = GoogleReview(text, rating, int(review_amount))
            return ScraperException(200, 'OK')

        except Exception as _ex:
            return ScraperException(400, _ex)

    def scroll_all_reviews(self):
        while True:
            self.driver.execute_script(
                "document.getElementsByClassName('dS8AEf')[0].scrollTop = document.getElementsByClassName('dS8AEf')[0].scrollHeight"
            )
            time.sleep(2)
            reviews = self.driver.find_elements(By.CLASS_NAME, 'wiI7pd')
            print('Found #reviews', len(reviews))
            if len(reviews) >= 18:    #self.google_review.len_review
                break
        return

    def scrap_data(self):
        reviews = self.driver.find_elements(By.CLASS_NAME, 'jftiEf')
        review_data = list()
        for i in range(len(reviews)):
            more = reviews[i].find_elements(By.CLASS_NAME, 'w8nwRe')
            if more:
                more[0].click()
            reply = reviews[i].find_elements(By.CLASS_NAME, 'CDe7pd')
            review = Review()
            review_data = reviews[i].text.split('\n')
            for field, id in review.fields.items():
                if isinstance(id, list):
                    review.raw_review[field] = '\n'.join(review_data[id[0]:id[1]])
                elif id < len(review_data):
                    review.raw_review[field] = review_data[id]
            print('Parsing review of %s' % review.raw_review['reviewer_name'])
            if reply:
                reply_data = reply[0].text.split('\n')
                review.raw_review['replied_by'] = reply_data[0]
                review.raw_review['reply_content'] = '\n'.join(reply_data[1::])
            self.google_review.reviews.append(review)
        return self.google_review
