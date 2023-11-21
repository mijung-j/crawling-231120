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

if __name__ == '__main__':
    qm = QrMaker()
    title = input('QR 생성할 파일명을 입력하세요.')
    qr_data = input('QR 생성할 도메인을 입력하세요.')
    qm.set_domain(qr_data)
    qm.save_qr_code(title)

