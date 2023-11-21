from currency_converter import CurrencyConverter
import requests
from bs4 import BeautifulSoup

class Exchange:
    def __init__(self):
        pass
    def get_all_currencies(self):
        cc = CurrencyConverter()
        return cc.currencies

    def change_usd_to_krw(self):
        cc = CurrencyConverter('http://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip')
        return cc.convert(1, 'USD', 'KRW')

    def change_realtime_usd_to_krw(self, target1, target2):

        headers = {
            'User-Agent': 'Mozilla/5.0',
            'Content-Type': 'text/html; charset=utf-8'
        }
        #https://kr.investing.com/currencies/usd-krw
        response = requests.get(f'https://kr.investing.com/currencies/{target1}-{target2}', headers=headers)
        content = BeautifulSoup(response.content, 'html.parser')
        print(f'111{content}')
        #containers = content.find('span', {'data-test': 'instrument-price-last'})
        containers = content.find('span', {'class': 'text-2xl'})
        print(f'222{containers}')
        print(f'333{containers.text}')
        return containers.text

if __name__ == '__main__':
    e = Exchange()

    while 1:
        menu = input('0-종료 1-전체화폐단위 2-원달러 3-실시간 환율 변환')
        if menu == '0':
            print('프로그램 종료')
            break
        elif menu == '1':
            c = e.get_all_currencies()
            print(f'전체화폐 단위 : {c}')
        elif menu == '2':
            c = e.change_usd_to_krw()
            print(f'원달러 환율 : {c}')
        elif menu == '3':
            target1 = input('바꾸려고 하는 화폐 단위 : ')
            target2 = input('바뀌는 화폐 단위 : ')
            c = e.change_realtime_usd_to_krw(target1, target2)
            print(f'실시간 환율 : {c}')
        else:
            print('메뉴에 없는 항목입니다')
            continue

