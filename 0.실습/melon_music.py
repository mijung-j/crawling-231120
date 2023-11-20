
import pandas as pd
from bs4 import BeautifulSoup   # 외부 라이프러리 임포트 시 from 절 붙음.
import requests                 # 내부 라이브러리 임포트 시 from 절 없음.

# https://www.melon.com/chart/index.htm?dayTime=20231120

class MelonMusic:
    pass


class MelonMusic:
    def __init__(self):
        self.domain = 'https://www.melon.com/chart/index.htm?dayTime='
        self.url = ''  # 해당 클래스에서 사용할 수 있는 전역변수
        self.headers = {'User-Agent': 'Mozilla/5.0'}
        self.class_name = []
        self.title_ls = []
        self.artist_ls = []
        self.dict = {}
        self.df = None

    def set_url(self, url):  # 함수 (사용자함수?)
        # self.url = f'{self.domain}/{url}' # 기계어 + 인간어 혼용할 때 f 사용
        self.url = requests.get(f'{self.domain}/{url}', headers=self.headers).text

    def get_url(self):
        return self.url

    def get_title(self):
        soup = BeautifulSoup(self.url, 'lxml')
        ls1 = soup.find_all(name='div', attrs=({"class": 'ellipsis rank01'}))

        # ls1 = soup.find_all(name='p', attrs=({"class": self.class_name[1]}))
        # ls2 = soup.find_all(name='p', attrs=({"class": self.class_name[0]}))
        for i in ls1:
            self.title_ls.append(i.find("a").text)
        # for i in ls2:
        #     self.artist_ls.append(i.find("a").text)
        # print(f'데이터가 수집 되었습니다./ {self.title_ls}')
        return self.title_ls

    def get_artist(self):
        soup = BeautifulSoup(self.url, 'lxml')
        ls2 = soup.find_all(name='div', attrs=({"class": 'ellipsis rank02'}))

        # ls1 = soup.find_all(name='p', attrs=({"class": self.class_name[1]}))
        # ls2 = soup.find_all(name='p', attrs=({"class": self.class_name[0]}))
        for i in ls2:
            self.artist_ls.append(i.find("a").text)
        # for i in ls2:
        #     self.artist_ls.append(i.find("a").text)
        # print(f'데이터가 수집 되었습니다./ {self.title_ls}')
        return self.artist_ls

    def insert_dict(self):  # list [] 데이터를 dictionry {} 형태로 변환. (엑셀로 내려받기 위해)
        # 방법 1. range
        """
        for i in range(0, len(self.title_ls)):
            self.dict[self.title_ls[i]] = self.artist_ls[i]
        # 방법 2. zip
        for i, j in zip(self.title_ls, self.artist_ls):
            self.dict[i] = j
        """
        # 방법 3. enumerate (가장 좋은 방법)
        for i, j in enumerate(self.title_ls):
            self.dict[j] = self.artist_ls[i]
        print('데이터가 딕셔너리에 추가 되었습니다.')
        print('딕셔너리에 저장된 데이터는 다음과 같습니다')
        print(dict)

    def dict_to_dataframe(self):  # 데이터를 엑셀로 내려받음. (데이터프레임이 엑셀과 비슷함. 파일로 저장하면 엑셀이고 안하면 데이터프레임(클래스)임.)
        self.df = pd.DataFrame.from_dict(self.dict, orient='index')
        print('딕셔너리 데이터를 데이터프레임에 이전 했습니다.')
        print(self.df)

    def df_to_excel(self):
        path = './data/melon.xlsx'
        self.df.to_excel(path)
        print('데이터가 CSV 파일에 저장되었습니다.')

    def df_to_csv(self):
        path = './data/melon.csv'
        self.df.to_csv(path, sep=',', na_rep='NaN')
        print('데이터가 CSV 파일에 저장되었습니다.')


if __name__ == '__main__':
    b = MelonMusic()
    url = input('크롤링 대상 url을 입력하세요.')  # 변수
    # https://music.bugs.co.kr/chart/track/day/total
    b.set_url(url)
    u2 = b.get_url()

    # print(f'당신이 원하는 url은 {u2} 입니다.')

    ls1 = b.get_title()
    print(ls1)

    ls2 = b.get_artist()
    print(ls2)
    # print(ls2.__len__())    # 배열 개수 출력

    b.insert_dict()
    b.dict_to_dataframe()
    b.df_to_excel()