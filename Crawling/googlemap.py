from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
chrome_options.add_experimental_option("detach",True)
browser = webdriver.Chrome(ChromeDriverManager().install())

url = "https://www.google.co.kr/maps/"
browser.get(url)
browser.implicitly_wait(10)
browser.maximize_window()

regions = ['마포','서대문','성동','성북','서초','송파','강남','강동','강서','강북','관악','광진','양천','용산',
           '영등포','은평','중랑','중','종로','구로','금천','노원','동대문','도봉','동작'] 
place = ['카페']
count = 1   # 수집한 카페 개수를 알 수 있게 별도의 count변수를 생성

# 수집한 데이터를 저장할 리스트 생성
Region = []
Name = []
Average_star = []
Load_user_id = []
Review_date = []
Each_star = []
Review_text = []
Label = []   # 라벨링 데이터를 담을 리스트

for region in regions:
    time.sleep(0.5)
    # 검색창입력
    search = browser.find_element(By.CSS_SELECTOR, "input.tactile-searchbox-input")  # 검색창태그
    search.click()
    time.sleep(1)
    search.send_keys(str(region) + '구 ' + str(place[0]))
    time.sleep(1)
    search.send_keys(Keys.ENTER)
    time.sleep(2)

    # 먼저 기존에 있는 가게개수를 세기
    lis = browser.find_elements(By.CSS_SELECTOR, ".Nv2PK")
    before_len = len(lis)

    # 검색첫페이지에서 스크롤 내려 모든 가게 로딩하기
    while True:
        time.sleep(1.5)
        # 맨 아래로 스크롤 내린다
        scroll_div = browser.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]')
        browser.execute_script("arguments[0].scrollBy(0, 2000)", scroll_div)
        time.sleep(4)


        # 스크롤 후 로딩된 데이터 개수 확인
        lis = browser.find_elements(By.CSS_SELECTOR, ".Nv2PK")
        after_len = len(lis)
        print("스크롤 전", before_len, "스크롤 후", after_len)  # 확인용코드

        # 로딩된 데이터 개수가 같다면 반복 멈춤
        if before_len == after_len:
            break
        before_len = after_len
        time.sleep(0.5)
    all = after_len
    print('로딩된 전체 가게 개수',all)

    # 검색했을 때 나오는 전체가게
    div_stores = browser.find_elements(By.CSS_SELECTOR, "div.Nv2PK.THOPZb.CpccDe")

    # 가게 하나씩 크롤링
    for store in div_stores:
        # 가게 각자의 url
        sub_url = store.find_element(By.CSS_SELECTOR, 'a.hfpxzc')
        link = sub_url.get_attribute('href')

        # 가게마다 새탭에서 열기
        browser.execute_script('window.open("https://google.com")')
        browser.switch_to.window(browser.window_handles[-1])
        browser.get(link)
        browser.implicitly_wait(10)
        time.sleep(1)

        # 가게정보 얻어오기
        # 이름
        name = browser.find_element(By.CSS_SELECTOR,"h1.DUwDvf > span").text
        print(f"{count}. {name}")

        # '리뷰 []개' 부분 클릭해서 리뷰전체보기
        # 리뷰없는 경우 예외처리
        review_box = browser.find_elements(By.CSS_SELECTOR, "#QA0Szd > div > div > div.w6VYqd > div.bJzME.tTVLSc > div > div.e07Vkf.kA9KIf > div > div > div.TIHn2 > div.tAiQdd > div.lMbq3e > div.LBgpqf > div > div.fontBodyMedium.dmRWX > div.F7nice.mmu3tf > span:nth-child(2) > span:nth-child(1) > button")
                                                            
        if len(review_box) > 0:
            review_box[0].click()
            time.sleep(1.5)
            browser.implicitly_wait(10)

            # 평균별점
            average_star = browser.find_element(By.CSS_SELECTOR, "div.fontDisplayLarge").text

            # 로딩된 리뷰개수 확인
            reviews = browser.find_elements(By.CSS_SELECTOR, "div.jftiEf")
            before_len = len(reviews)

            # 끝까지 스크롤해서 리뷰로딩하기
            scroll_div = browser.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]')
            while True:
                time.sleep(1.5)
                browser.execute_script("arguments[0].scrollBy(0, 20000)", scroll_div)
                time.sleep(4)
                # 스크롤 후 로딩된 데이터 개수 확인
                reviews = browser.find_elements(By.CSS_SELECTOR,"div.jftiEf")
                after_len = len(reviews)
                print("스크롤 전", before_len, "스크롤 후", after_len, "리뷰개수", len(reviews))
                time.sleep(1)
                # 로딩된 데이터 개수가 같다면 반복 멈춤(모든 리뷰 크롤링하려면 주석처리한 부분으로 하기)
                if before_len == after_len:  
                    break
                before_len = after_len

            # 데이터 기다리는 시간을 0으로 만들기
            browser.implicitly_wait(0)

            # 로딩된 리뷰들을 하나하나 크롤링
            for i, review in enumerate(reviews, 1):
                # 리뷰어이름
                load_user_id = review.find_element(By.CSS_SELECTOR, "div.d4r55").text

                # 리뷰어마다 평점
                star = review.find_element(By.CSS_SELECTOR, "div.DU9Pgb > .kvMYJc")
                star = star.get_attribute('aria-label')
                each_star = star.replace("별표 ", '').replace("개", '')

                # 리뷰를 언제썼는지(xpath로 했을때는 오류남)
                review_date = review.find_element(By.CSS_SELECTOR, "span.rsqaWe").text

                # 리뷰text(더보기있으면 클릭. 없으면 그냥 진행)
                try:
                    review_more = browser.find_element(By.CSS_SELECTOR,".w8nwRe.kyuRq")
                    review_more.click()
                    time.sleep(1)
                    review_text = review.find_element(By.CSS_SELECTOR,"span.wiI7pd").text

                except:
                    review_text = review.find_element(By.CSS_SELECTOR,"span.wiI7pd").text

                # 데이터수집(수집한 데이터를 해당 리스트에 추가)
                Region.append(region)
                Name.append(name)
                Average_star.append(average_star)
                Load_user_id.append(load_user_id)
                Review_date.append(review_date)
                Each_star.append(float(each_star))   # 각 개인의 평점을 실수형으로 변환
                Review_text.append(review_text)
                if float(each_star) >= 3:    # 개인 평점이 3점 이상일 때는 1, 3점 미만일 떄는 0으로 라벨링
                    Label.append(1)
                else:
                    Label.append(0)


        else:
            print("리뷰없음")
            average_star = None
            load_user_id = None
            review_date = None
            each_star = None
            review_text = None

            # 데이터수집
            Region.append(region)
            Name.append(name)
            Average_star.append(average_star)
            Load_user_id.append(load_user_id)
            Review_date.append(review_date)
            Each_star.append(each_star)
            Review_text.append(review_text)
            Label.append(None)
        count += 1
        # 끝나면 새탭을 닫고 다시 이전 탭으로 이동
        browser.close()
        browser.switch_to.window(browser.window_handles[-1])
        time.sleep(1.5)        
        
#     #새롭게 검색하기 위해 검색결과 지우기
#     clear = browser.find_element(By.CSS_SELECTOR, "a.gsst_a")
#     clear.click()
#     time.sleep(8)

browser.close()


list_tuples = list(zip(Region, Name, Average_star, Load_user_id, Review_date, Each_star, Review_text, Label))
df = pd.DataFrame(list_tuples, columns=['Region','Name','Average_star','Load_user_id','Review_date','Each_star','Review_text','Label'])

df.to_csv('origin_data.csv',encoding = 'utf-8')

