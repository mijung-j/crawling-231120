import requests
import pandas as pd
from bs4 import BeautifulSoup
class NaverStock:

    def __init__(self):
        self.code = pd.DataFrame({'name':[], 'code':[]})
        self.url = ''

    def krx_crawl(self):
        h = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13', header=0, encoding='euc-kr')[0]
        print(f'h {h}')
        h['종목코드'] = h['종목코드'].map('{:06d}'.format) # 005930 -> 5930 막는다
        k = h[['회사명', '종목코드']]
        print(f'k {k}')
        self.code = k.rename(columns={'회사명': 'name', '종목코드': 'code'})


    def get_url(self, item_name):
        code = self.code.query("name=='{}'".format(item_name))['code'].to_string(index=False)
        self.url = f'http://finance.naver.com/item/sise_day.naver?code={code}'  # 'code'로 대체
        print('요청 URL = {}'.format(self.url))


    def naver_crawl(self):

        # url = f'https://finance.naver.com/item/sise_day.naver?code=005930'
        headers = {'User-agent': 'Mozilla/5.0'}  # 네이버주식 서버에서 요청함
        req = requests.get(self.url, headers=headers)
        html = BeautifulSoup(req.text, 'lxml')
        pgrr = html.find('td', class_='pgRR')
        print(pgrr.a['href'])
        s = pgrr.a['href'].split('=')
        print(f'{s}')
        last_page = s[-1]
        print(f'last page : {last_page}')
        temp_page = 10

        df = None

        for page in range(1, int(temp_page) + 1):
            if (page < 5):
                print(f'크롤링 중인 페이지 : {page}')
            req = requests.get(f'{self.url}&page={page}', headers=headers)
            df = pd.concat([df, pd.read_html(req.text, encoding='euc-kr')[0]])

        df.dropna(inplace=True)
        df.reset_index(drop=True, inplace=True)
        df.to_excel('./data/samsung_price.xlsx')



if __name__ == '__main__':
    n = NaverStock()
    while 1:
        menu = input(f'''0. EXIT\n
              '1. Kind에서 종목 코드 와 url 얻기\n
              '2. 원하는 종목의 시세를 엑셀파일로 저장하기\n''')
        if menu == '0':
            break
        elif menu == '1':
            n.krx_crawl()
            m = input('종목명 입력: ')
            n.get_url(m)
        elif menu == '2':
            n.naver_crawl()