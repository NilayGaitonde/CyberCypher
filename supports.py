from math import floor
import time
from collections import Counter
from selenium import webdriver
from itertools import combinations
from selenium.webdriver.common.keys import Keys
def check_spoiler(movieName,review):
    driver= webdriver.Chrome('/opt/homebrew/bin/chromedriver')
    driver.get('https://www.google.com/')
    searchBox=driver.find_element_by_tag_name('input')
    searchBox.send_keys(movieName)
    searchBox.send_keys(Keys.ENTER)
    pageLinks=driver.find_elements_by_class_name('NY3LVe')
    imdb=pageLinks[0]
    imdb.click()
    synopsis=driver.find_element_by_xpath('//*[@id="__next"]/main/div/section[1]/div/section/div/div[1]/section[7]/div[2]/ul[1]/li[2]/a')
    time.sleep(5)
    synopsis.click()
    time.sleep(5)
    synopsis=driver.find_element_by_xpath('//*[@id="main"]/section/div[3]/ul/li[2]/a')
    synopsis.click()
    print(synopsis.text)
    # synopsis=''.join(driver.find_element_by_class_name('ipl-zebra-list__item').text)
    synopsis=''.join(driver.find_element_by_xpath('//*[@id="synopsis-py4495824"]').text)
    print(floor(len(synopsis)/2))
    synopsis=synopsis[floor(len(synopsis)/2):]
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for ele in synopsis:
        if ele in punc:
            synopsis = synopsis.replace(ele, "")
    driver.quit()
    counts={}
    synopsisLst=synopsis.split()
    counts=Counter(synopsisLst)
    reviewCount=dict()
    combs=list(combinations(review.split(),2))
    for i in combs:
        sum=0
        for j in i:
            if(j in counts):
                sum+=counts[j]
            reviewCount.update({i:sum})
    for i in sorted(reviewCount.items(), key=lambda x: x[1],reverse=True):
        if(0<(i[1])<=2):
            print('spoiler')
            return 'spoiler'
        # else:
        #     print('not spoiler')
    return 'not spoiler'
    print(synopsis)
    print(reviewCount)
if __name__=='__main__':
    print('hello world')