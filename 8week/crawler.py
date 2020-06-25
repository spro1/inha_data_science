# 12193962 김윤석
# 파일생성을 위한 라이브러리 추가
import os
# 웹 크롤링을 위한 라이브러리 추가
import requests
# 데이터 파싱을 위한 라이브러리 추가
from bs4 import BeautifulSoup

# 이미지 저장 경로
folder = "./img/"

# 폴더 없을 시 생성
if not os.path.isdir(folder):
    os.makedirs(folder)

# parsing url
url = "https://en.wikipedia.org/wiki/Piano"

# user agent 추가
header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'}

# request get url
req = requests.get(url, headers=header)

# req status check
# print(req.status_code)


# html body data parsing
soup = BeautifulSoup(req.text, 'html.parser')

# 이미지 url 리스트 생성
img_url_list = []

# 본문과 관련된 사진만 파싱
# div id="content" > a class="image" > img 태그 파싱
# div 태그의 id값과 a 태그의 class값을 지정해주지 않으면 본문 content 외 img 값들이 파싱에 포함
img_url_list = soup.select('div#content a.image img')

# 본문안에 삽입되어 있는 영상의 썸네일 이미지는 태그 트리 구조가 다름
# div class="PopUpMediaTransform" > img 태그 파싱
# 오디오 썸네일 이미지도 본문과 관련된 이미지라 판단하여 추가
img_url_list += soup.select('div.PopUpMediaTransform > img')

for i in img_url_list:
    # 이미지 경로
    # print(i['src'])

    # 이미지 경로 URL
    img_url = "https:"+i['src']

    # alt 값이 빈 경우가 있어 split을 이용해 파일명 지정
    # / 로 split 해주고 가장 마지막 값을 가져옴
    img_name = i['src'].split("/")[-1]

    # 이미지 URL
    print(img_url)
    # 이미지 파일명
    print(img_name)

    # 이미지 다운로드
    # 이미지 데이터 get
    img_res = requests.get(img_url)

    # img_res status check
    # print(img_res.status_code)

    # 데이터 파일 저장
    # folder 경로 + 파일명
    open(folder + img_name, 'wb').write(img_res.content)

print("finish")
# 12193962 김윤석