import qtconsole.svg

import qrcode

class QrMaker :
    def __init__(self):
        self.qr_data = ''

    def set_domain(self, qr_data):
        self.qr_data = qr_data

    def save_qr_code(self, title):
        qr_img = qrcode.make(self.qr_data)
        save_path = f"./{title}.png"
        qr_img.save(save_path)

    def save_multi_qr_code(self, fname):
        file_path = f'./{fname}'

        with open(file_path, 'rt', encoding='UTF8') as f:
            read_lines = f.readlines()

            for line in read_lines:
                line = line.strip()
                print(line)

                qr_data = line
                qr_img = qrcode.make(qr_data)

                save_path = f'./qrcode/4. QR코드 생성기{qr_data}.png'
                qr_img.save(save_path)

if __name__ == '__main__':
    qm = QrMaker()

    while 1 :
        menu = input('0.종료 1.QR 1개 생성 2.QR 다수 생성')
        if menu == '0':
            print('프로그램 종료')
            break
        elif menu == '1':
            title = input('QR 생성할 파일명을 입력하세요.')
            qr_data = input('QR 생성할 도메인을 입력하세요.')
            qm.set_domain(qr_data)
            qm.save_qr_code(title)
        elif menu =='2':
            fname = input('QR 생성할 파일명을 입력하세요.')
            qm.save_multi_qr_code(fname)


            title = input('QR 생성할 파일명을 입력하세요.')
            qr_data = input('QR 생성할 도메인을 입력하세요.')
            qm.set_domain(qr_data)
            qm.save_qr_code(title)
        else :
            print('메뉴에 없는 항목입니다')
            continue
