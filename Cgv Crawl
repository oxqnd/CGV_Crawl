import requests
import csv
import json
from tqdm import tqdm

# 요청 헤더 설정
url = 'http://www.cgv.co.kr/common/ajax/point.aspx/GetMoviePointVariableList'
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json; charset=UTF-8',
    'Cookie': 'ASP.NET_SessionId=eazep4gpqhkyvgaupqacqgej; WMONID=msRB35-vZL_; _gid=GA1.3.1289016099.1725886581; _gat=1; _gat_UA-47951671-5=1; _gat_UA-47951671-7=1; _gat_UA-47126437-1=1; _dc_gtm_UA-47951671-9=1; _ga_2MJKWDJ6EW=GS1.3.1725886692.1.0.1725886692.60.0.0; _ga=GA1.1.1940277856.1725886581; _ga_559DE9WSKZ=GS1.1.1725885626.2.1.1725886711.40.0.0; _ga_SSGE1ZCJKG=GS1.3.1725886581.1.1.1725886712.39.0.0; CgvCM=w2nXmoSKzfRysXc1C0dSgsXwFaAS1ig1EmWNzj+l72zVK6fOzGYFFNsZT9fsQ9tkSIguqKWCuCHE3/nokRgcPV6RE7fh5DdCAQtbwDQxE4thgRTpkOVJWToLnW/PYaiKAJ8ZVtfdmEZL/voijFyUrF5/S/D/HZNBO/A5deoLVjkQOcoVoPXdSxbpjCfxVExKlLpC1RMHPnAGKFNx2biQ0rzQgakGIksPs+2ACciFHPPIDnOA4HBl92QhjB/2AFsB',  # 여기에 쿠키 값을 추가하세요
    'Origin': 'http://www.cgv.co.kr',
    'Referer': 'http://www.cgv.co.kr/movies/detail-view/?midx=88337',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

# 영화 ID와 페이징 설정
movie_idx = 87554 # 영화 ID
page_size = 6  # 페이지당 리뷰 개수
max_pages = 9549  # 원하는 최대 페이지 수 설정 (필요에 따라 변경 가능)

# CSV 파일 생성 및 데이터 저장
with open('cgv_reviews.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['작성자', '리뷰내용'])  # CSV 헤더

    for page_index in tqdm(range(1, max_pages + 1), desc="Fetching Reviews"):
        # 요청에 필요한 데이터를 JSON 형태로 설정
        data = {
            'movieIdx': movie_idx,
            'pageIndex': page_index,
            'pageSize': page_size,
            'orderType': 0,
            'filterType': 1,
            'isTotalCount': False,
            'isMyPoint': 'false'
        }

        # 요청 보내기
        response = requests.post(url, headers=headers, json=data, verify=False)

        # 응답이 성공적인지 확인
        if response.status_code == 200:
            try:
                # JSON 데이터를 파싱
                reviews = response.json()
                
                # 'd' 키가 문자열로 된 JSON이므로 이를 다시 JSON으로 변환
                if 'd' in reviews:
                    reviews_list = json.loads(reviews['d'])['List']  # 'List' 내부 데이터 추출

                    # 리뷰 처리
                    if isinstance(reviews_list, list):
                        for review in reviews_list:
                            # 리뷰 데이터가 딕셔너리인지 확인
                            if isinstance(review, dict) and 'UserIdNicName' in review and 'CommentText' in review:
                                writer.writerow([review['UserIdNicName'], review['CommentText']])
                            else:
                                print("리뷰 형식이 예상과 다릅니다. 확인이 필요합니다.")
                    else:
                        print(f'페이지 {page_index}에 리뷰가 더 이상 없습니다.')
                        break
            except json.JSONDecodeError:
                print(f"페이지 {page_index}에서 JSON 파싱 오류가 발생했습니다.")
        else:
            print(f"페이지 {page_index} 요청에 실패했습니다. 상태 코드: {response.status_code}")
            break

print('CSV 파일에 모든 데이터가 성공적으로 저장되었습니다.')
