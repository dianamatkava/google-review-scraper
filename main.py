from __future__ import annotations
from xlswriter import generate_xls
from operations import GoogleReviewScraper




def run():
    review = GoogleReviewScraper()
    res = review.search("Aspria Berlin Ku’damm")
    if res.status_code == 200:
        review.scroll_all_reviews()
        google_reviews = review.scrap_data()
        generate_xls(google_reviews)


if __name__ == '__main__':
    run()

