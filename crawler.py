
#  브라우저크롬
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import sys
import os

# 검색 키워드
keyword = sys.argv[1]

# 이미지 장 수
numImages = int(sys.argv[2])
print(numImages)
# 결과물을 저장할 폴더 이름
result_dir = sys.argv[3]
if result_dir not in os.listdir():
    os.mkdir(result_dir)

# (True - 고화질 / False - 섬네일)
#high_resolution = sys.argv[4]

#if high_resolution in "True true":
#    import pixabay_2x_crawling as pc
#elif high_resolution in "False false":
#    import pixabay_crawling as pc

# 크롤링을 수행합니다

def crawling(keyword, numImages, result_dir):
    # 웹드라이버 실행
    driver = webdriver.Chrome(ChromeDriverManager().install())
    # 이미지 검색 url
    url = 'https://pixabay.com/ko/images/search/'

    # 이미지 검색하기
    driver.get(url + keyword)

    # 이미지 검색 영역의 xpath
    xpath = '//*[@id="app"]/div[2]/div[3]/div/div/div[2]/div'
    print(xpath)
    # 100장 이하 이미지를 요구받은 경우
    if numImages <= 100:
        image_area = driver.find_element_by_xpath(xpath)
        image_elements = image_area.find_elements_by_tag_name("img")
        for i in range(numImages):
            image_elements[i].screenshot(result_dir + "/" + str(time.time()) + ".png")
    # 100장 이상을 요구받은 경우
    else:
        while numImages > 0:
            image_area = driver.find_element_by_xpath(xpath)
            image_elements = image_area.find_elements_by_tag_name("img")
            for i in range(len(image_elements)):
                image_elements[i].screenshot(result_dir + "/" + str(time.time()) + ".png")
                numImages -= 1
                if i == len(image_elements) - 1:
                    next_button = driver.find_element_by_partial_link_text("다음 페이지")
                    next_button.click()
                    time.sleep(3)

crawling(keyword, numImages, result_dir)
