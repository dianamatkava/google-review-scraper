from __future__ import annotations
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from operations import GoogleReviews




def run():
    review = GoogleReviews()
    review.search("Aspria Berlin Ku’damm")
    pass



if __name__ == '__main__':
    run()

